from rest_framework import viewsets
from api.serializers import ExamQuestionAnswerSerializer
from api.models import ExamQuestionAnswer


# QuestionAnswer viewSet
class ExamQuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset         = ExamQuestionAnswer.objects.all()
    serializer_class = ExamQuestionAnswerSerializer
