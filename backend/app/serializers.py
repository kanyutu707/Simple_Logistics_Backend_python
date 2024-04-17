from rest_framework import serializers
from .models import *


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driver
        fields=["driver_charges", "first_name", "last_name", "age", "password"]
class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model=vehicles
        fields=["number_plate", "max_weight", "drivers"]

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trips
        fields=["start_position", "end_point", "status", "vehicle"]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trips
        fields=["trip", "amount", "status"]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        models=Clients
        fields=["joining_date"]
    