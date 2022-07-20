from rest_framework import serializers
from .models import Booking, Flight


class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        # fields = '__all__'
        fields = ['id', 'destination', 'time', 'price']
        """
        to exclude one item only
        exclude = ('type')
        """


class BookingListSerializer1(serializers.ModelSerializer):
    class Meta:

        model = Booking
        fields = ['id', 'flight', 'date']
