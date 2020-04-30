from django.db import models
from .stage import Stage
from .user import User
from .category import Category

class Subject(models.Model):
    name         = models.CharField(max_length=200)
    credit_hours = models.IntegerField()
    stage        = models.ForeignKey(Stage, on_delete=models.CASCADE)
    category     = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name

        