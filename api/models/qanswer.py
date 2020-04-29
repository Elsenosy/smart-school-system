from django.db import models
from . import Questionnair 

class Qanswer(models.Model):
    question = models.TextField()
    questionnair = models.ForeignKey(Questionnair, on_delete=models.CASCADE)