from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register("booking", views.BookingViews, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
]
