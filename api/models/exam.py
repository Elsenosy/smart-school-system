from django.db import models
from . import Subject, User 

class Exam(models.Model):
    # Relations
    user = models.ManyToManyField(User, null=True)
    subject = models.ManyToManyField(Subject, null=True)
    
    # Fields
    title    = models.CharField(max_length=200)
    duration = models.FloatField()
    mark     = models.IntegerField()
    notes    = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title