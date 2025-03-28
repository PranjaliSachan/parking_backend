from django.db import models
from django.contrib.auth.models import User


class ParkingSpot(models.Model):
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.location} - ${self.price_per_hour}/hr"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation by {self.user.username} at {self.parking_spot.location}"
