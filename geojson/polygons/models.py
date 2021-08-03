from django.db import models
from django.utils.translation import gettext_lazy as _

from djmoney.models.fields import MoneyField

from core.common import TimestampedModel, ActiveModel


class Polygon(TimestampedModel, ActiveModel):
    """
    notes: maybe I should use django-geojson here?
     but I just added a lat/lng fields instead
    """

    provider = models.ForeignKey(
        "providers.Provider", related_name="polygons", on_delete=models.DO_NOTHING
    )
    name = models.CharField(_("Name"), max_length=255)
    price = MoneyField(
        max_digits=14,
        decimal_places=3,
        default_currency="USD",
    )
    lng = models.FloatField()
    lat = models.FloatField()

    class Meta:
        db_table = "polygon"

    def __str__(self):
        return self.name
