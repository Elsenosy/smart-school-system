from django.db import models
from api.models.user import User
from api.models.subject import Subject 

class Questionnair(models.Model):
    title   = models.CharField(max_length=200)
    date    = models.DateField(auto_now=True)
    subject = models.ManyToManyField(Subject)
    user 	= models.ManyToManyField(User)
    
    def __str__(self):
        return self.title