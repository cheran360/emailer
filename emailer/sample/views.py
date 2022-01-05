from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import status
import requests

# Create your views here.

@api_view(['GET'])
def home(request):
  return Response({"message":"worked"}, status=status.HTTP_200_OK)
