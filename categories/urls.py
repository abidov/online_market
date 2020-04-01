from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('category/<int:pk>/products/', views.CategoryViewSet.as_view({'get': 'get_products_of_category'}), name='category-product-list'),
]

urlpatterns += router.urls