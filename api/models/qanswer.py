from django.db import models
from api.models.questionnair import Questionnair

class Qanswer(models.Model):
    question 	 = models.TextField()
    questionnair = models.ForeignKey(Questionnair, on_delete=models.CASCADE)