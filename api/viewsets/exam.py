from rest_framework import viewsets
from api.serializers import ExamSerializer
from api.models import Exam


# Exam viewSet
class ExamViewSet(viewsets.ModelViewSet):
    queryset         = Exam.objects.all()
    serializer_class = ExamSerializer
