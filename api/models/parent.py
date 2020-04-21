from django.db import models
from django.conf import settings
from . import Admin

class Parent(models.Model):
    user                = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job                 = models.CharField(max_length=100, blank=True)
    added_by            = models.ForeignKey(Admin, models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
