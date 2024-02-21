from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor, Product, Vehicle, QualityCheck
from .serializer import VendorSerializer, ProductSerializer, VehicleSerializer, QualityCheckSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

@api_view(['POST'])
def initiate_checkout(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        # Implement the check-out process logic here
        return Response({"message": "Check-out process initiated successfully."})
    except Vehicle.DoesNotExist:
        return Response({"message": "Vehicle not found."}, status=404)

@api_view(['GET'])
def vehicle_detail(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    serializer = VehicleSerializer(vehicle)
    return Response(serializer.data)
