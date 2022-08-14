from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import Response
# Create your views here.
class HelloDrf(APIView):
    def get(self, request,format=None):
        return Response({"message":'Hola'})