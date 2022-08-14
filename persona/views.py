from django.shortcuts import render

# Create your views here.
from ast import Delete
from functools import partial
from persona import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from persona.models import Persona
from persona.serializers import PersonaSerializers

#primera vista para visualizar y añadir lugares

class PersonaView(APIView):
    def get(self, request):
        personas= Persona.objects.all()
        print(personas)
        serializer=PersonaSerializers(personas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=PersonaSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PersonaSingleView(APIView):
    def put(self,request,id):
        persona=Persona.objects.get(id=id)
        serializer=PersonaSerializers(persona,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,id):
        persona=Persona.objects.get(id=id)
        persona.delete()
        return Response({"message":"Persona eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)