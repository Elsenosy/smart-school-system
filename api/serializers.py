from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User, Admin, Student, Teacher, Parent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}   

    # Specific code for creating user, to generate token for each user
    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            user_type=validated_data['user_type'],
            )
        user.set_password(validated_data['password'])
        user.save()
        # Create auth key for the user
        token = Token.objects.create(user=user)

        # Create other objects
        if validated_data['user_type'] == 'ADM':
            pass
        
        return user

# Serializer: Admin
class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Admin
        fields = '__all__'
    

# Serializer: Student
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True, required=False)
    added_by = AdminSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Student
        fields = '__all__'

# Serializer: Teacher
class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True, required=False)
    added_by = AdminSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Teacher
        fields = '__all__'

# Serializer: Parent
class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True, required=False)
    added_by = AdminSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Parent
        fields = '__all__'

