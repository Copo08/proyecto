from rest_framework import serializers
from .models import Place

class PlaceSerializers(serializers.ModelSerializer):

    class Meta:  #cual modelo y campos que quiero que tenga

        model=Place
        fields ='__all__' #Trabaje con todos los atributos que definí