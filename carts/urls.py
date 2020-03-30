from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/create/', views.CartCreateView.as_view(), name='cart-create'),
]