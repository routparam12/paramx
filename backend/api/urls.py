from django.urls import path
from .views import health, echo

urlpatterns = [
    path("health/", health),
    path("echo/", echo),
]
