from rest_framework import serializers
from .user import UserSerializer
from .admin import AdminSerializer
from api.models import Parent

# Serializer: Parent
class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True, required=False)
    added_by = AdminSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Parent
        fields = '__all__'