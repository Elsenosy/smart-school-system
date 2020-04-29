from django.db import models
from django.utils import timezone
from django.conf import settings
from . import Admin, Category, Subject


class Teacher(models.Model):
    user      = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hire_date = models.DateField(verbose_name="Hire date", blank=True, default=timezone.now)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject   = models.ManyToManyField(Subject, null=True)
    added_by  = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username