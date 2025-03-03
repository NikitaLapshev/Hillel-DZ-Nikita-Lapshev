from django.db import models
from food.models import Product

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name="orders")
    status = models.CharField(
        max_length=20, choices=[("pending", "in processing"), ("delivered", "Delivered")]
    )

    def __str__(self):
        return f"Order {self.id} - {self.status}"
