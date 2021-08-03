from django.contrib import admin

from .models import Provider


class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
    )


admin.site.register(Provider, ProviderAdmin)
