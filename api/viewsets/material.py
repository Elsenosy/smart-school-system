from rest_framework import viewsets
from api.serializers import MaterialSerializer
from api.models import Material


# Material viewSet
class MaterialViewSet(viewsets.ModelViewSet):
    queryset         = Material.objects.all()
    serializer_class = MaterialSerializer
