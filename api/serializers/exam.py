from rest_framework import serializers
from api.models import Exam

class ExamSerializer(serializers.ModelSerializer):
        
    class Meta:
        model  = Exam
        fields = "__all__"
        extra_kwargs = {
            "user": {"write_only": True},
            "subject": {"write_only": True}
            }