from django_filters import CharFilter, rest_framework as filters

from .models import Polygon


class PolygonListFilter(filters.FilterSet):
    class Meta:
        model = Polygon
        fields = ("lat", "lng")
