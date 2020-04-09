from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from carts.models import CartItem
from .models import Order
from .serializers import OrderSerializer
from categories.serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from django.db.models import Sum


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail=False)
    def add_to_order(self, request):
        cart = self.request.user.cart
        order = Order.objects.create(user=cart.user, cart=cart.cart_items.all(), price=0)
        serializer = OrderSerializer(order, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)