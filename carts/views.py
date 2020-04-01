from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import CartSerializer
from market.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from .models import Cart


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = (IsOwner, IsAuthenticated)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(methods=['DELETE'], detail=False)
    def delete_cart(self, request, pk=None):
        Cart.objects.get(user=self.request.user).delete()