from django.urls import path, include
from rest_framework.routers import DefaultRouter
from config.views import UsersViewSet

router = DefaultRouter()
router.register(r'products', UsersViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
