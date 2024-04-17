from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.


class DriverListView(APIView):
    permission_classes=[permissions.ISAuthenticated]

    #list all the drivers in the system

    def get(self, request, *args, **kwargs):
        drivers=Driver.objects.filter(driver=request.user.id)
        serializer=DriverSerializer(drivers,status=status.HTTP_200_OK)


class TripListView(APIView):
    permission_classes=[permissions.ISAuthenticated]


    #list all the drivers
    def get(self, request, *args, **kwargs):
        trips=Trips.objects.filter(trip=request.trip.id)
        serializer=TripsSerializer(trips, status=status.HTTP_200_OK)


class PaymentListView(APIView):
    permission_classes=[permissions.ISAuthenticated]

    #list the payments made
    def get(self, request, *args, **kwargs):
        payments=Payments.objects.filter(payment=request.Payments.id)
        serializer=PaymentSerializer(payments, status=status.HTTP_200_OK)

class ClientListView(APIView):
    permission_classes=[permissions.ISAuthenticated]

    #list all the clients
    def get(self, request, *args, **kwargs):
        clients=Clients.objects.filter(client=request.Clients.id)
        serializer=ClientSerializer(clients, status=status.HTTP_200_OK)