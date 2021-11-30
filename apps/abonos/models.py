from django.db import models
from apps.common.models import BaseModel, BaseMeta
from apps.clientes.models import Cliente
from apps.bancos.models import CuentaBancaria


class EstadoAbono(BaseModel):
    nombre = models.CharField(max_length=50)

    class Meta(BaseMeta):
        db_table = 'cobranza_estado_abono'
        verbose_name = 'Estado'
        verbose_name = 'Estados'

    def __str__(self):
        return self.nombre


class Abono(BaseModel):
    estado_abono = models.ForeignKey(EstadoAbono, on_delete=models.DO_NOTHING, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=True, blank=True)
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, on_delete=models.DO_NOTHING)
    fecha = models.DateField(auto_now_add=False)
    referencia = models.CharField(max_length=250)
    importe = models.DecimalField(max_digits=12, decimal_places=2)
    numero_operacion = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta(BaseMeta):
        db_table = 'cobranza_abono'
        verbose_name = 'Abono'
        verbose_name = 'Abonos'

    def __str__(self):
        return self.cuenta_bancaria.numero
