from rest_framework import serializers

from .models import Polygon
from providers.serializers import ProviderSerializer


class PolygonSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(read_only=True)

    class Meta:
        model = Polygon
        fields = "__all__"
