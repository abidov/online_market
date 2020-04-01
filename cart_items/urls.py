from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cartitem', views.CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('productitem/<int:pk>/add/', views.CartItemViewSet.as_view({'get': 'add_product_item'}), name='cart-item-create'),
]

urlpatterns += router.urls