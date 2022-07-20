from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .models import Booking, Flight
from .serializers import ListSerializer


class FlightsApiList(ListAPIView):
    queryset = Flight.objects.all()
    # queryset = Flight.objects.all().filter(name='Pikachu')
    serializer_class = ListSerializer


class BookingApiList(ListAPIView):
    queryset = Booking.objects.all()
    # queryset = Flight.objects.all().filter(name='Pikachu')
    serializer_class = ListSerializer
