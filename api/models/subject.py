from django.db import models
from api.models.stage import Stage
from api.models.user import User
from api.models.category import Category
from django.core.validators import MinValueValidator, MaxValueValidator


class Subject(models.Model):
    name         = models.CharField(max_length=200)
    credit_hours = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    stage        = models.ForeignKey(Stage, on_delete=models.CASCADE)
    category     = models.ManyToManyField(Category, blank=True)
    Teacher 	 = models.ForeignKey(User, limit_choices_to={'user_type':'TECH'}, 
    								related_name='User',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

        