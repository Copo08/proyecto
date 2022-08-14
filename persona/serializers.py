from rest_framework import serializers
from .models import Persona

class PersonaSerializers(serializers.ModelSerializer):

    class Meta:  #cual modelo y campos que quiero que tenga

        model=Persona
        fields ='__all__' #Trabaje con todos los atributos que definí