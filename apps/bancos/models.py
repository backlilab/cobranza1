from django.db import models
from apps.common.models import BaseModel, BaseMeta


class Banco(BaseModel):
    nombre = models.CharField(max_length=50)

    class Meta(BaseMeta):
        db_table = 'cobranza_banco'
        verbose_name = 'Banco'
        verbose_name = 'Bancos'

    def __str__(self):
        return self.nombre


class CuentaBancaria(BaseModel):
    banco = models.ForeignKey(Banco, on_delete=models.DO_NOTHING)
    numero = models.CharField(max_length=50, unique=True)
    CURRENCY_CHOICES = [
        ('PEN', 'Soles'),
        ('USD', 'Dolares'),
    ]
    tipo_moneda = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='PEN',
    )

    class Meta(BaseMeta):
        db_table = 'cobranza_cuenta_bancaria'
        verbose_name = 'Numero de cuenta'
        verbose_name = 'Numeros de cuenta'

    def __str__(self):
        return self.banco
