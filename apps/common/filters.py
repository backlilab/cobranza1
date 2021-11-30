from django.db.models import F, Q
from django.db.models.functions import Concat, Coalesce

from django_filters import rest_framework as filters

from .models import BaseModel

from datetime import datetime, timedelta


class BaseModelSoftfactoringFilter(filters.FilterSet):
    fecha_inicio = filters.DateTimeFilter(label='Fecha inicio', method='filter_fecha_inicio')
    fecha_fin = filters.DateTimeFilter(label='Fecha fin', method='filter_fecha_fin')

    class Meta:
        model = BaseModel
        fields = {
            'fecha_inicio': ('gt',),
            'fecha_fin': ('gte',),
        }

    def filter_fecha_inicio(self, queryset, name, value):
        queryset = queryset.annotate(
                fecha_auditoria=Coalesce('fecha_actualizacion', 'fecha_creacion')
            ).filter(
                fecha_auditoria__gt=value
            ).order_by('fecha_auditoria')
        return queryset

    def filter_fecha_fin(self, queryset, name, value):
        queryset = queryset.filter(fecha_auditoria__lte=value)
        return queryset