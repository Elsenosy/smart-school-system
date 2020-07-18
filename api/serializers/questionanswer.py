from rest_framework import serializers
from api.models import ExamQuestionAnswer

class ExamQuestionAnswerSerializer(serializers.ModelSerializer):
        
    class Meta:
        model  = ExamQuestionAnswer
        fields = "__all__"