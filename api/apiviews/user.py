from rest_framework import generics, status
from rest_framework.response import Response
from api.models import Subject
from api.serializers import SubjectSerializer

class UserSubjects(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Subject.objects.filter(user=self.kwargs['pk'])
        return queryset
    serializer_class = SubjectSerializer
