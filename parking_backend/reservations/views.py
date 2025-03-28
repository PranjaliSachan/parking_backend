from rest_framework import generics, status
from rest_framework.response import Response
from .models import ParkingSpot, Reservation
from .serializers import ParkingSpotSerializer, ReservationSerializer
from django.contrib.auth.models import User
from datetime import datetime
from dateutil import parser
from django.utils.timezone import make_aware


class ParkingSpotList(generics.ListAPIView):
    # Get all spots (both available & reserved)
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer


class CreateReservation(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        try:
            user_id = request.data.get("user")
            spot_id = request.data.get("parking_spot")
            start_time = request.data.get("start_time")
            end_time = request.data.get("end_time")
            total_price = request.data.get("total_price")

            if not all([user_id, spot_id, start_time, end_time, total_price]):
                return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

            # Ensure the user exists
            # user = User.objects.get(id=user_id)

            # Get the parking spot
            spot = ParkingSpot.objects.get(id=spot_id)
            if not spot.is_available:
                return Response({"error": "Spot already reserved"}, status=status.HTTP_400_BAD_REQUEST)

            # Convert ISO 8601 string to datetime
            start_time = parser.isoparse(start_time)
            end_time = parser.isoparse(end_time)

            # Ensure datetime is timezone-aware
            if start_time.tzinfo is None:
                start_time = make_aware(start_time)
            if end_time.tzinfo is None:
                end_time = make_aware(end_time)

            # Create the reservation
            reservation = Reservation.objects.create(
                user=user_id,
                parking_spot=spot,
                start_time=start_time,
                end_time=end_time,
                total_price=total_price,
                is_paid=False,
            )

            # Mark spot as reserved
            spot.is_available = False
            spot.save()

            return Response({"message": "Reservation successful", "reservation_id": reservation.id},
                            status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except ParkingSpot.DoesNotExist:
            return Response({"error": "Spot not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Invalid datetime format"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
