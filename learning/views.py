import json
import os

import google.generativeai as genai
from dotenv import load_dotenv
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from learning.models import StudyMaterial, FlashCard
from learning.serializers import StudyMaterialSerializer

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_real_flashcards(material):
    # We use the flash model because it is fast and cost-effective
    model = genai.GenerativeModel('gemini-3.6-flash')

    # We write a strict prompt so the AI replies in perfect JSON format
    # Notice we explicitly tell it to handle Kurdish or English!
    prompt = f"""
    You are an expert tutor. Read the following study material, which may be in English or Kurdish.
    Generate 3 distinct flashcards highlighting the most important concepts.

    You MUST return the result strictly as a JSON list of dictionaries. 
    Do not include any markdown formatting like ```json or ```. Just the raw JSON array.
    Each dictionary must have exactly two keys: "question" and "answer".

    Text:
    {material.source_text}
    """

    try:
        # 1. Send the text to the AI
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        # 2. Convert the AI's string response into a Python list of dictionaries
        flashcards_data = json.loads(response.text.strip())

        # 3. Save the real AI data to your database
        for item in flashcards_data:
            FlashCard.objects.create(
                study_material=material,
                question=item.get("question", "Error generating question"),
                answer=item.get("answer", "Error generating answer")
            )

    except Exception as e:
        print(f"AI Generation Error: {e}")
        # Fallback just in case the AI fails or formatting breaks
        FlashCard.objects.create(
            study_material=material,
            question="AI could not process this text.",
            answer="Please try again or edit the source text."
        )

class StudyMaterialViewSet(viewsets.ModelViewSet):
    serializer_class = StudyMaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyMaterial.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        material = serializer.save(student=self.request.user)
        generate_real_flashcards(material)

    @action(detail=True, methods=['get', 'post'])
    def regenerate(self, request, pk=None):
        material = self.get_object()
        material.flash_cards.all().delete()
        generate_real_flashcards(material)

        serializer = self.get_serializer(material)
        return Response(serializer.data)
