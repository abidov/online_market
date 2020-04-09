from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'order', views.OrderViewSet, basename='order')


urlpatterns = [
    path('cart/add_to_order/', views.OrderViewSet.as_view({'post': 'add_to_order'})),
]

urlpatterns += router.urls