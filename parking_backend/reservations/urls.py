from django.urls import path
from .views import ParkingSpotList, CreateReservation

urlpatterns = [
    path('spots/', ParkingSpotList.as_view(), name='parking-spots'),
    path('reserve/', CreateReservation.as_view(), name='create-reservation'),
]
