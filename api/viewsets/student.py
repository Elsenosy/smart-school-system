from rest_framework import viewsets
from api.serializers import StudentSerializer
from api.models import Student

# Student viewSet
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
