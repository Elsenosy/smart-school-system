from rest_framework import serializers
from api.models.stage import Stage

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}   
