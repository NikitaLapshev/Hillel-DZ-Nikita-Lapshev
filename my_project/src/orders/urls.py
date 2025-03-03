from django.urls import path, include
from rest_framework.routers import DefaultRouter
from config.views import OrdersViewSet

router = DefaultRouter()
router.register(r'orders', OrdersViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
