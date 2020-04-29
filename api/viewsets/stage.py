from rest_framework import viewsets
from api.serializers import StageSerializer
from api.models import Stage

# Stage viewSet
class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer