from django.urls import path
from .views import health, echo, ask_question

urlpatterns = [
    path("health/", health),
    path("echo/", echo),
    path("ask/", ask_question),
]
