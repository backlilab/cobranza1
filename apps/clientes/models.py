from django.db import models
from apps.common.models import BaseModel, BaseMeta


class Cliente(BaseModel):
    ruc = models.CharField(max_length=20)
    nombre = models.CharField(max_length=250)

    class Meta(BaseMeta):
        db_table = 'cobranza_cliente'
        verbose_name = 'Cliente'
        verbose_name = 'Clientes'

    def __str__(self):
        return self.nombre
