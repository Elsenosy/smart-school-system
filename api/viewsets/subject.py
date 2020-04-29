from rest_framework import viewsets
from api.serializers import SubjectSerializer
from api.models import Subject

# Subject viewSet
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

