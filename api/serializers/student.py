from rest_framework import serializers
from .user import UserSerializer
from .admin import AdminSerializer
from api.models import Student

# Serializer: Student
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True, required=False)
    added_by = AdminSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Student
        fields = '__all__'