from rest_framework import serializers
from .models import Planilla


class PlanillaSerializer(serializers.ModelSerializer):
    #estado_abono = serializers.ReadOnlyField(source='estado_abono.nombre')
    cuenta_bancaria = serializers.ReadOnlyField(source='cuenta_bancaria.banco.nombre')
    #cliente = serializers.ReadOnlyField(source='cliente.nombre')
    moneda = serializers.ReadOnlyField(source='cuenta_bancaria.get_tipo_moneda_display')

    class Meta:
        model = Planilla
        fields = [
            'fecha', 'cuenta_bancaria', 'moneda',
            'total_inhabilitado', 'total_identificado', 'total_por_identificar'
        ]
