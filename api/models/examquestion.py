from django.db import models
from . import  User, Exam

class ExamQuestion(models.Model):
    # Relations
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    
    # Fields
    mark    = models.IntegerField()
    content = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.exam