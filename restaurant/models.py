from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateField()

    # Explicitly declare the default manager
    objects = models.Manager()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    # Explicitly declare the default manager
    objects = models.Manager()

    def __str__(self):
        return self.title


