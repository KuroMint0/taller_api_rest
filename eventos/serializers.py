from rest_framework import serializers
from .models import Evento, Inscripcion

class EventoSerializer(serializers.ModelSerializer):
    cupos_disponibles = serializers.ReadOnlyField()

    class Meta:
        model = Evento
        fields = ["id", "nombre", "lugar", "descripcion", "valor", "cupos", "cupos_disponibles"]

    def validate_cupos(self, valor):
        if valor < 1:
            raise serializers.ValidationError("Debe tener al menos 1 cupo.")
        return valor

