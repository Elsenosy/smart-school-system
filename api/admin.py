from django.contrib import admin
from .models import User, Category, Stage, Questionnair, Qanswer, Subject
from api.models.material import Material

# Register your models here.
admin.site.register(User)
admin.site.register(Stage)
admin.site.register(Category)
admin.site.register(Questionnair)
admin.site.register(Qanswer)
admin.site.register(Subject)
admin.site.register(Material)
