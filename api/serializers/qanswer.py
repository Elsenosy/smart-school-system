from rest_framework import serializers
from api.models import Qanswer

class QanswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qanswer
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}   