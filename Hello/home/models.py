from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=15)
    trip_type = models.CharField(max_length=100)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.trip_type}"

class Package(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  # e.g. "3 Days, 2 Nights"

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name
