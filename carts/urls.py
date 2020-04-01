from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cart/', views.CartViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'delete_cart'}), name='cart-list'),
]