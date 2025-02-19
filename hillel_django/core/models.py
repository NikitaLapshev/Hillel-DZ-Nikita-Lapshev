from django.db import models

class Citizen(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    address = models.TextField(null=True, blank=True)
    employment_status = models.CharField(max_length=50)
    education_level = models.CharField(max_length=100)

    def __str__(self):
        return f'Citizen: {self.surname} {self.name}'

class PublicService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)



class ServiceUsage(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    service = models.ForeignKey(PublicService, on_delete=models.CASCADE)
    usage_date = models.DateField()
    frequency = models.IntegerField(default=1)



class Infrastructure(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    location = models.TextField(null=True, blank=True)
    last_maintenance_date = models.DateField(null=True, blank=True)
    scheduled_maintenance_date = models.DateField(null=True, blank=True)



class SocialProgram(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)



class ProgramEnrollment(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    program = models.ForeignKey(SocialProgram, on_delete=models.CASCADE)
    enrollment_date = models.DateField()


class GovEmployee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

