from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coment
from .serializers import ComentSerializer

# Create your views here.
class ComentView(APIView):
    def post(self,request):
        serializer=ComentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ComentSingleView(APIView):
    def delete(self, request,pk):
        place=get_object_or_404(Coment,pk=pk)
        place.delete()
        return Response('Comentario eliminado',status=status.HTTP_204_NO_CONTENT)