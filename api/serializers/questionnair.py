from rest_framework import serializers
from api.models import Questionnair

class QuestionnairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnair
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}   