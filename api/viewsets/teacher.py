from rest_framework import viewsets
from api.serializers import TeacherSerializer
from api.models import Teacher

# Teacher viewSet
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer