from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('product/<int:pk>/categories/', views.ProductViewSet.as_view({'get': 'get_categories_of_product'}), name='product-category-list'),
]

urlpatterns += router.urls