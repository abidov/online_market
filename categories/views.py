from .models import Category
from .serializers import CategorySerializer
from products.serializers import ProductSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=['GET'], detail=True)
    def get_products_of_category(self, request, pk=None):
        products = Category.objects.get(pk=pk).get_all_products()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)