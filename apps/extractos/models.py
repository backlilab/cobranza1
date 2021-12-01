from django.db import models
from apps.common.models import BaseModel, BaseMeta
from apps.clientes.models import Cliente
from apps.bancos.models import CuentaBancaria

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.cuenta_bancaria.id, instance.fecha.id, ext)
    return os.path.join('extracto', 'fecha', filename)


class Extracto(BaseModel):
    fecha = models.DateField(auto_now_add=False)
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, on_delete=models.DO_NOTHING)
    archivo = models.FileField(upload_to=content_file_name)

    class Meta(BaseMeta):
        db_table = 'cobranza_extracto'
        verbose_name = 'Extracto'
        verbose_name_plural = 'Extractos'

    def __str__(self):
        return '{} - {}'.format(self.cuenta_bancaria.banco.nombre, self.fecha)



class Transaccion(BaseModel):
    extracto = models.ForeignKey(Extracto, on_delete=models.DO_NOTHING, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=True, blank=True)
    fecha = models.DateField(auto_now_add=False)
    referencia = models.CharField(max_length=250)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    numero_operacion = models.CharField(max_length=50)
    pertenece_cobranza = models.BooleanField(default=False)
    itf = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sucursal = models.CharField(max_length=50, null=True, blank=True)
    referencia2 = models.CharField(max_length=250, null=True, blank=True)
    detalle = models.CharField(max_length=250, null=True, blank=True)
    cargo = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    numero_doc = models.CharField(max_length=250, null=True, blank=True)
    # usuario

    class Meta(BaseMeta):
        db_table = 'cobranza_transaccion'
        verbose_name = 'Transaccion'
        verbose_name_plural = 'Transacciones'

    def __str__(self):
        return '{} - {}'.format(self.referencia, self.fecha)
