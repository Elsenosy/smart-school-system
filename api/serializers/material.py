from rest_framework import serializers
from api.models.material import Material 

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}   