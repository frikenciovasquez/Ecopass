from ..models import Rute, Travel, Destiny
from rest_framework import serializers

from datetime import date, timedelta


class DestinySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Destiny
        fields= ('id','nombre','vacations_type','region','price')

class RutaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rute
        fields=('id', 'rute_name', 'viaje','ruta_destinos')

    def create(self, validated_data):
        destinos = validated_data.pop("ruta_destinos")
        instance = super().create({**validated_data})
        instance.ruta_destinos.set(destinos)
    
        return instance 

class RuteSerializer(serializers.ModelSerializer):
    ruta_destinos= DestinySerializer(many=True)
    class Meta:
        model = Rute
        fields = ('id', 'rute_name', 'viaje','ruta_destinos')



class TravelSerializer(serializers.ModelSerializer):
    ruta_de_viaje=RuteSerializer(many=True, read_only=True)
    class Meta:
        model = Travel
        fields = ('id', 'date_start', 'date_end', 'transporte','user','ruta_de_viaje')
    def validate_travel(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('usuario de viaje incorrecto')
        return value
  
    def create(self, validated_data):
        print(validated_data)
        if not "date_start" in validated_data or not "date_end" in validated_data:
            raise serializers.ValidationError('Falta fechas')
        usuario = self.context["request"].user
        validate_inicio= validated_data["date_start"]-date.today()
        validate_final= validated_data["date_end"]-validated_data["date_start"]
        if validate_inicio >= timedelta(days=7) and validate_final >=timedelta(days=1):
            instance = super().create(
                {**validated_data})
        
            return instance
        else:
             raise serializers.ValidationError('fechas invalidas, fecha de reservacion 8 dias previos, fecha minima de duracion de viaje 1 dia')

