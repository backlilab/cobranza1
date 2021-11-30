from rest_framework import serializers
from .models import Abono


class AbonoSerializer(serializers.ModelSerializer):
    estado_abono = serializers.ReadOnlyField(source='estado_abono.nombre')
    cuenta_bancaria = serializers.ReadOnlyField(source='cuenta_bancaria.banco.nombre')
    cliente = serializers.ReadOnlyField(source='cliente.nombre')
    moneda = serializers.ReadOnlyField(source='cuenta_bancaria.get_tipo_moneda_display')

    class Meta:
        model = Abono
        fields = [
            'estado_abono', 'cliente', 'cuenta_bancaria', 'moneda',
            'fecha', 'referencia', 'importe', 'numero_operacion', 'saldo'
        ]
