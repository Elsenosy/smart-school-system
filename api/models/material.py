from django.db import models
from . import Subject 
from django.conf import settings

# define an path to upload image to
def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / material_<id>/<filename> 
    return 'material_{0}/{1}'.format(instance.subject, filename) 

class Material(models.Model):
    # Relations
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    # Fields
    material_type  = models.CharField(max_length=200)
    path           = models.FileField(upload_to=user_directory_path, max_length=500)
    title          = models.CharField(max_length=200)
    notes          = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title