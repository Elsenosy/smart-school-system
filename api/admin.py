from django.contrib import admin
from .models import User, Category, Admin, Student, Teacher, Parent, Stage, Questionnair, Qanswer, Subject

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Stage)
admin.site.register(Category)
admin.site.register(Questionnair)
admin.site.register(Qanswer)
admin.site.register(Subject)
