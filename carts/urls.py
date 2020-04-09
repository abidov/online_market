from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cartitem', views.CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('cart/', views.CartViewSet.as_view({'get': 'retrieve'}), name='cart-detail'),
    path('productitem/<int:pk>/add/', views.CartItemViewSet.as_view({'post': 'add_product_item'}), name='cartitem-create'),
    path('cartitem/<int:pk>/', views.CartItemViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='cartitem-detail'),
]


