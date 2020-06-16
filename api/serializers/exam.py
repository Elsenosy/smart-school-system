from rest_framework import serializers
from api.models import Exam

class ExamSerializer(serializers.ModelSerializer):
        
    class Meta:
        model  = Exam
        fields = "__all__"