from django.contrib import admin

from .models import Polygon


class PolygonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
    )


admin.site.register(Polygon, PolygonAdmin)
