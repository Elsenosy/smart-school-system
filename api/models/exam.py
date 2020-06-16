from django.db import models
from . import Subject, User 

class Exam(models.Model):
    # Relations
    user = models.ManyToManyField(User)
    subject = models.ManyToManyField(Subject)
    
    # Fields
    title    = models.CharField(max_length=200)
    duration = models.IntegerField()
    mark     = models.IntegerField()
    notes    = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title