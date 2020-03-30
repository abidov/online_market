from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from products.serializers import ProductSerializer
from rest_framework import generics
# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = Category.objects.get(pk=self.kwargs['pk'])
        return category.get_all_products()
