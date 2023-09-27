from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Booking
from .serializers import BookingSerializer, ReponsedriverSerializer, CreatebokingSerializer
from rest_framework.response import Response
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import MyPermision

class BookingViews(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [MyPermision]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ReponsedriverSerializer
        elif self.request.method == "POST":
            return CreatebokingSerializer
        return BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(statut= "En entente")
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    
    def perform_update(self, serializer):
        return serializer.save(user = self.request.user)
    

# Create your views here.
