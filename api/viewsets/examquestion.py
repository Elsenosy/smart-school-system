from rest_framework import viewsets
from api.serializers import ExamQuestionSerializer
from api.models import ExamQuestion


# ExamQuestion viewSet
class ExamQuestionViewSet(viewsets.ModelViewSet):
    queryset         = ExamQuestion.objects.all()
    serializer_class = ExamQuestionSerializer
