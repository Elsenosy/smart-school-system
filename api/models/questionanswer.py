from django.db import models
from . import ExamQuestion

class ExamQuestionAnswer(models.Model):
    # Relations
    examquestion = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    
    # Fields
    content            = models.TextField(null=True, blank=True)
    is_right_answer    = models.BooleanField()
    
    def __str__(self):
        return self.examquestion