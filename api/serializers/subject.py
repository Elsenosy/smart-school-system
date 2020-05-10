from rest_framework import serializers
from api.models import Subject
from . import StageSerializer, CategorySerializer

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__' 

class SubjectReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    stage    = StageSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = '__all__' 
