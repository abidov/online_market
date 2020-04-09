from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'productitem', views.ProductItemViewSet, basename='productitem')


urlpatterns = [
    path('product/<int:pk>/categories/', views.ProductViewSet.as_view({'get': 'get_categories_of_product'}), name='product-category-list'),
]

urlpatterns += router.urls