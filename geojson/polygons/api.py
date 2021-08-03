from rest_framework import viewsets

from django_filters import rest_framework as filters

from .models import Polygon
from .filters import PolygonListFilter
from .serializers import PolygonSerializer

class PolygonViewSet(viewsets.ModelViewSet):
    serializer_class = PolygonSerializer
    queryset = Polygon.objects.filter(is_active=True)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PolygonListFilter

