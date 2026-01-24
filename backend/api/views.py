from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


@api_view(["POST"])
def echo(request):
    return Response({
        "message": request.data.get("message", "")
    })
