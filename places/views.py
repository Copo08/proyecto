from ast import Delete
from functools import partial
from places import serializers
import places
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from places.models import Place
from places.serializers import PlaceSerializer, PlacelistComentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
#primera vista para visualizar y añadir lugares

class PlaceView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        places= Place.objects.all()
        print(places)
        serializer=PlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        print(request.data)
        try:
            file= request.data['image']
            request.data['image']=file

        except KeyError:
            file=None
        
        serializer=PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PlaceAPIUpdateDeleteView(APIView):

    def get(self, request, id):
        place=Place.objects.filter(id=id).first()
        if place is None:
            return Response({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer=PlacelistComentSerializer(place)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        place=Place.objects.filter(id=id).first()
        if place is None:
            return Response ({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer=PlaceSerializer(place,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status=status.HTTP_200_OK)

    def delete(self,request, id):
        place=Place.objects.filter(id=id).first()
        if place is None:
            return Response({'error':'Bas request'},status=status.HTTP_400_BAD_REQUEST)
        place.delete()
        return Response({'message':'Lugar eliminado satisfactoriamente'},status=status.HTTP_200_OK)

        






