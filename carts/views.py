from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import CartSerializer, CartItemSerializer, CartItemCreateSerializer
from market.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from products.models import ProductItem
from rest_framework.response import Response


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = (IsOwner, IsAuthenticated)

    def retrieve(self, request, *args, **kwargs):
        serializer = CartSerializer(self.request.user.cart, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemCreateSerializer
    queryset = CartItem.objects.all()
    
    @action(methods=['POST'], detail=True)
    def add_product_item(self, request, pk):
        serializer = CartItemCreateSerializer(data=request.data, context={'request': request, 'pk': pk})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        product = ProductItem.objects.get(pk=self.kwargs['pk'])
        serializer.save(cart=self.request.user.cart, product=product)

