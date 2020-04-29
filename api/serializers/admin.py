from rest_framework import serializers
from .user import UserSerializer
from api.models import Admin

# Serializer: Admin
class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Admin
        fields = '__all__'
    