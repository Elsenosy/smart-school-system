from django.contrib import admin
from .models import User, Admin, Student, Teacher, Parent

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
