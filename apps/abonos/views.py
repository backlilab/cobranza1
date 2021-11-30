from rest_framework import viewsets
from .serializers import AbonoSerializer
from .models import Abono


class AbonoViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Abono.objects.all()
    serializer_class = AbonoSerializer
    filterset_fields = ('cliente', 'estado_abono')
