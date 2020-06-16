from rest_framework import serializers
from api.models import Material

class MaterialSerializer(serializers.ModelSerializer):
    material_url = serializers.SerializerMethodField('get_material_url')
    
    class Meta:
        model  = Material
        fields = "__all__"
    
    def get_material_url(self, obj):
        return obj.path.url