from rest_framework import viewsets
from api.serializers import ParentSerializer
from api.models import Parent

# Parent viewSet
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer