from rest_framework import viewsets
from api.serializers import AdminSerializer
from api.models import Admin

# Admin viewSet
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

