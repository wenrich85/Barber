from django.db import models

class Appointment(models.Model):
    # SERVICE_CHOICES = [('MC', 'Male Cut'), ('FC', 'Female Cut')]
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.DateTimeField()
    phone = models.IntegerField()
    email = models.EmailField(max_length = 254, blank = True)
    service = models.ManyToManyField('Service')

class Service(models.Model):
    name = models.CharField(max_length = 100)
    price =  models.DecimalField(max_digits=5, decimal_places=2)

class Availability(models.Model):
    start = models.TimeField()
    end = models.TimeField()

