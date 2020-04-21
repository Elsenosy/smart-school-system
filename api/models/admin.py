from django.db import models
from django.conf import settings

class Admin(models.Model):
    user                = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_title           = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username