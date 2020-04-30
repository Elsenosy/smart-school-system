from rest_framework import serializers
from rest_framework.authtoken.models import Token
from api.models import User

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

        return user

    def get_fields(self, *args, **kwargs):
        fields = super(UserSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            fields['username'].required = False
            fields['password'].required = False
        return fields