from django.urls import path
from . import views

urlpatterns = [
    path('product-items/<int:pk>/add/', views.CartItemCreateView.as_view(), name='cart-item-create'),
    path('cart-items/detail/<int:pk>/', views.CartItemDetailView.as_view(), name='cart-item-detail'),
]