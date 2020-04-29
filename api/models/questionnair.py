from django.db import models
from . import Subject, Student 

class Questionnair(models.Model):
    title   = models.CharField(max_length=200)
    date    = models.DateField(auto_now=True)
    subject = models.ManyToManyField(Subject)
    student = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.title