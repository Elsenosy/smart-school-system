from rest_framework import serializers
from api.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    stage = serializers.StringRelatedField(many=False)

    class Meta:
        model = Subject
        fields = "__all__" 