from rest_framework import serializers

from learning.models import FlashCard, StudyMaterial


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'


class StudyMaterialSerializer(serializers.ModelSerializer):
    flash_cards = FlashCardSerializer(many=True, read_only=True)

    class Meta:
        model = StudyMaterial
        fields = ['id', 'student', 'title', 'source_text', 'created_at', 'flash_cards']