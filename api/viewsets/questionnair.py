from rest_framework import viewsets
from api.serializers import QuestionnairSerializer
from api.models import Questionnair

# Questionnair viewSet
class QuestionnairViewSet(viewsets.ModelViewSet):
    queryset = Questionnair.objects.all()
    serializer_class = QuestionnairSerializer

