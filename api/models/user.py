from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from api.models import Stage 
from api.models import Category 
from django.conf import settings

# define an path to upload image to
def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return '{0}/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.id, filename) 

# Create your models here.
class User(AbstractUser):
    ADMIN               = 'ADM'
    STUDENT             = 'STD'
    PARENT              = 'PAR'
    TEACHER             = 'TECH'
    USER_TYPES          = [
                            (ADMIN,   'Admin'),
                            (STUDENT, 'Student'), 
                            (PARENT,  'Parent'), 
                            (TEACHER, 'Teacher'),
                        ]
    address             = models.CharField(max_length=200, blank=True)
    phone               = models.CharField(max_length=30, blank=True)
    birth_date          = models.DateField(verbose_name="Birth date", blank=True, default=datetime.date.today, null=True)
    user_type           = models.CharField(max_length=4, choices=USER_TYPES, blank=True)
    picture             = models.ImageField(upload_to = user_directory_path, null=True)
    hire_date           = models.DateField(verbose_name="Hire date", blank=True, default=datetime.date.today, null=True)
    job                 = models.CharField(max_length=100, blank=True, null=True)
    stage               = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subject             = models.ManyToManyField(to="api.Subject", blank=True)
