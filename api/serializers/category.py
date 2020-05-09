from rest_framework import serializers
from api.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}   