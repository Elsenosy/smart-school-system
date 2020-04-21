from django.db import models
from django.utils import timezone
from django.conf import settings
from . import Admin

class Teacher(models.Model):
    user                = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hire_date           = models.DateField(verbose_name="Hire date", blank=True, default=timezone.now)
    added_by            = models.ForeignKey(Admin, models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username