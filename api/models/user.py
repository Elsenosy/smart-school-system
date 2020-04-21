from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

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
    birth_date          = models.DateField(verbose_name="Birth date", blank=True, default=timezone.now().date())
    user_type           = models.CharField(max_length=4, choices=USER_TYPES, blank=True)
