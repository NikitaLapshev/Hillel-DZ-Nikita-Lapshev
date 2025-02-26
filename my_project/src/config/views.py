from rest_framework import viewsets
from django.contrib.auth import get_user_model
from orders.models import Orders
from orders.serializers import OrdersSerializer
from products.models import Products
from products.serializers import ProductsSerializer
from users.serializers import UsersSerializer

User = get_user_model()


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
