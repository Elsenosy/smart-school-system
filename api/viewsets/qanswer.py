from rest_framework import viewsets
from api.serializers import QanswerSerializer
from api.models import Qanswer

# Qanswer viewSet
class QanswerViewSet(viewsets.ModelViewSet):
    queryset = Qanswer.objects.all()
    serializer_class = QanswerSerializer

