from rest_framework import serializers
from .models import ParkingSpot, Reservation


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "user", "parking_spot", "start_time",
                  "end_time", "total_price", "is_paid"]
