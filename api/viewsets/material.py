from rest_framework import viewsets
from api.serializers.material import MaterialSerializer
from api.models.material import Material

# Qanswer viewSet
class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

