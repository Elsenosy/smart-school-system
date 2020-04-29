from rest_framework import viewsets
from api.serializers import CategorySerializer
from api.models import Category

# Category viewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer