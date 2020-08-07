from rest_framework import serializers
from api.models import ExamQuestion
from .questionanswer import ExamQuestionAnswerSerializer
import re

class ExamQuestionSerializer(serializers.ModelSerializer):
    answers = ExamQuestionAnswerSerializer(many=True, read_only=True)
    class Meta:
        model  = ExamQuestion
        fields = '__all__'

    def validate_content(self, value):
        if len(value) < 5:
            raise serializers.ValidationError({'status': False, 'error': 'Content length must be greater than 5 characters!'})

        return value