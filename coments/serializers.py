from rest_framework import serializers
from .models import Coment

class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coment
        fields=(
            'id',
            'place',
            'coment',
            'created',
        )

    def to_representatio(self,instance):
        return{
            'id':instance.id,
            'place':{
                'id':instance.place.id,
                'name':instance.place.name
                },
            'coment':instance.coment,
            'created':instance.created

        }