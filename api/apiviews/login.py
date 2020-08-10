from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.core import serializers
from rest_framework.response import Response

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        user_serialize = serializers.serialize('python', [user], ensure_ascii=False)

        # Pop password from user's data
        user_data = user_serialize[0].get('fields')
        user_data.pop('password')

        if user:
            result = {
                "user": user_data, 
                "id": user_serialize[0].get('pk'), 
                "token": user.auth_token.key,
            }
            return Response({"result": result})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
