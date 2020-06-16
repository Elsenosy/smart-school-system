from rest_framework import serializers
from api.models import ExamQuestion

class ExamQuestionSerializer(serializers.ModelSerializer):
        
    class Meta:
        model  = ExamQuestion
        fields = "__all__"