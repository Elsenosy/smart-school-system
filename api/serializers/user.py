from rest_framework import serializers
from rest_framework.authtoken.models import Token
from api.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}   

    # Specific code for creating user, to generate token for each user
    def create(self, validated_data):
        picture     = validated_data['picture']
        hire_date   = validated_data['hire_date']
        job         = validated_data['job']
        stage       = validated_data['stage']
        category    = validated_data['category']
        
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            user_type=validated_data['user_type'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            birth_date=validated_data['birth_date'],
            picture=picture,
            hire_date=hire_date,
            job=job,
            stage=stage,
            category=category,        
            )
        user.set_password(validated_data['password'])
        user.save()
        # Create auth key for the user
        token = Token.objects.create(user=user)

        return user

    def get_fields(self, *args, **kwargs):
        fields = super(UserSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            fields['username'].required = False
            fields['password'].required = False
        return fields