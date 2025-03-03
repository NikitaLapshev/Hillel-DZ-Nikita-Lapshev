from django.db import models

class Products(models.Model):
    name_product = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'Citizen: {self.name_product}'
