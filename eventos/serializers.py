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

class InscripcionSerializer(serializers.ModelSerializer):
    evento = serializers.PrimaryKeyRelatedField(
        queryset = Evento.objects.filter(activo=True)
    )
    evento_nombre = serializers.ReadOnlyField(source="evento.nombre")
    correo = serializers.EmailField(write_only=True)

    class Meta:
        model = Inscripcion
        field = ["id", "evento", "evento_nombre", "nombre", "correo", "cantidad", "creada"]

    def validate_cantidad(self, valor):
        if valor < 1 or valor > 5:
            raise serializers.ValidationError("Debe ser entre 1 y 5 entradas.")
        return valor

    def validate(self, datos):
        cantidad = datos.get("cantidad", 1)
        if cantidad > datos["evento"].cupos_disponibles():
            raise serializers.ValidationError(
                "No quedan cupos suficientes para este evento."
            )
        return datos