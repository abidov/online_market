from django.urls import path
from . import views

urlpatterns = [
    path('product-items/', views.ProductItemListView.as_view(), name='product-item-list'),
    path('product-items/<int:pk>/', views.ProductItemDetailView.as_view(), name='product-item-detail'),
    path('products/<int:pk>/product-item-create/', views.ProductItemCreateView.as_view(), name='product-item-create'),
]