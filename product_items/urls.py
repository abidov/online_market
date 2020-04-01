from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'productitem', views.ProductItemViewSet, basename='productitem')

urlpatterns = []
urlpatterns += router.urls