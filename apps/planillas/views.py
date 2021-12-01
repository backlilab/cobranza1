from rest_framework import viewsets
from .serializers import PlanillaSerializer
from .models import Planilla


class PlanillaViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Planilla.objects.all()
    serializer_class = PlanillaSerializer
    #filterset_fields = ('cliente', 'estado_abono')