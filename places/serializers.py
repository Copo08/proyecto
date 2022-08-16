from rest_framework import serializers
from .models import Place
from coments.models import Coment
from coments.serializers import ComentPlaceListSerializer

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:  #cual modelo y campos que quiero que tenga

        model=Place
        fields ='__all__' #Trabaje con todos los atributos que 
        
class PlacelistComentSerializer(serializers.ModelSerializer):

    coment = serializers.SerializerMethodField()

    class Meta:
        model=Place
        field=(
            'id',
            'name',
            'coment',
        
        )

    def get_coment(self, obj):
        selected_coment = Coment.objects.filter(place_id=obj.id)
        return ComentPlaceListSerializer(selected_coment, many=True).data

