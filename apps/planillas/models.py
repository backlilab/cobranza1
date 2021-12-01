from django.db import models
from apps.common.models import BaseModel, BaseMeta
from apps.clientes.models import Cliente
from apps.bancos.models import CuentaBancaria
from apps.extractos.models import Extracto


class Planilla(BaseModel):
    extracto = models.ForeignKey(Extracto, on_delete=models.DO_NOTHING, null=True, blank=True)
    fecha = models.DateField(auto_now_add=False)
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, on_delete=models.DO_NOTHING)
    total_inhabilitado = models.DecimalField(max_digits=12, decimal_places=2)
    total_identificado = models.DecimalField(max_digits=12, decimal_places=2)
    total_por_identificar = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta(BaseMeta):
        db_table = 'cobranza_planilla'
        verbose_name = 'planilla'
        verbose_name_plural = 'panillas'

    def __str__(self):
        return '{} - {}'.format(self.cuenta_bancaria.banco.nombre, self.fecha)


class EstadoAbono(BaseModel):
    nombre = models.CharField(max_length=50)

    class Meta(BaseMeta):
        db_table = 'cobranza_estado_abono'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nombre


class Abono(BaseModel):
    planilla = models.ForeignKey(Planilla, on_delete=models.DO_NOTHING, null=True, blank=True)
    estado_abono = models.ForeignKey(EstadoAbono, on_delete=models.DO_NOTHING, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=True, blank=True)
    fecha = models.DateField(auto_now_add=False)
    importe = models.DecimalField(max_digits=12, decimal_places=2)
    numero_operacion = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta(BaseMeta):
        db_table = 'cobranza_abono'
        verbose_name = 'abono'
        verbose_name_plural = 'abonos'

    def __str__(self):
        return '{} - {}'.format(self.referencia, self.fecha)