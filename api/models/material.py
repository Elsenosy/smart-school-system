from django.db import models
from api.models.subject import Subject
from django.conf import settings

def subject_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return '{0}/subject_{1}/{2}'.format('material', instance.subject, filename) 

class Material(models.Model):
	TEXT			= 'TXT'
	VIDEO			= 'VID'
	AUDIO			= 'AUD'
	material_type 	= [
						(AUDIO, 'Audio'),
						(TEXT, 'TEXT/PDF'),
						(VIDEO, 'Video')
						] 
	media_type 		= models.CharField(max_length = 3, choices = material_type)
	path 			= models.FileField(upload_to = subject_directory_path, blank=True,null=True)
	title 			= models.CharField(max_length = 30)
	subject 		= models.ForeignKey(Subject, on_delete = models.CASCADE)


	def __str__(self):
		return self.title