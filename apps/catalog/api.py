from django.urls import path
from rest_framework import generics, serializers, filters
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','slug','category','price','mrp','stock','prescription_required','description']

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('products/', ProductList.as_view()),
]
