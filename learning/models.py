from django.db import models
from django.contrib.auth.models import User




class StudyMaterial(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    source_text = models.TextField(help_text="The raw text pasted by the student to be analyzed.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FlashCard(models.Model):
    study_material = models.ForeignKey(StudyMaterial, on_delete=models.CASCADE, related_name='flash_cards')
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question