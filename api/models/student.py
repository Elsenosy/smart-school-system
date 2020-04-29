from django.db import models
from django.utils import timezone
from django.conf import settings
import os 
from . import Admin, Stage, Subject 

# define an path to upload image to
def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return '{0}/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename) 

# Student model
class Student(models.Model):
    user     = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stage    = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True)
    added_by = models.ForeignKey(Admin, models.SET_NULL, null=True)
    picture  = models.ImageField(upload_to = user_directory_path, null=True)
    subject  = models.ManyToManyField(Subject, null=True)

    def __str__(self):
        return self.user.username
