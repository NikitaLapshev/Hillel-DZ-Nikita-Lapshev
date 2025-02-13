from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    phone_number = models.IntegerField(default=0)
    mail_address = models.CharField(max_length=30)

    def __str__(self):
        return f'Person: {self.surname} {self.name}'

class Order(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order: {self.id} for {self.person.name}'
