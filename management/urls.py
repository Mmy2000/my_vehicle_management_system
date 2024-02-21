
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, ProductViewSet, VehicleViewSet, initiate_checkout, vehicle_detail

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'products', ProductViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('initiate-checkout/<int:vehicle_id>/', initiate_checkout),
    path('vehicle-detail/<int:vehicle_id>/', vehicle_detail),
]
