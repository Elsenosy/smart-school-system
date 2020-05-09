from rest_framework import serializers
from api.models.subject import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}   