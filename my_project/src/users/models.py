from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    mail_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Citizen: {self.surname} {self.name}'
