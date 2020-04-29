from rest_framework import serializers
from . import UserSerializer, AdminSerializer, \
                            CategorySerializer, SubjectSerializer
from api.models import Teacher

# Serializer: Teacher
class TeacherSerializer(serializers.ModelSerializer):
    user     = UserSerializer(many=False, read_only=True, required=False)
    category = CategorySerializer(many=False, read_only=True, required=False)
    subject  = SubjectSerializer(many=True, read_only=False, required=False)
    added_by = AdminSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Teacher
        fields = '__all__'
