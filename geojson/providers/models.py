from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from core.common import TimestampedModel, ActiveModel


class Provider(TimestampedModel, ActiveModel):
    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_("Email Address"))
    phone_number = PhoneNumberField(verbose_name=_("Mobile Number"))
    language = models.CharField(_("Language Code"), max_length=4)
    curency = models.CharField(_("Currency Code"), max_length=3)

    class Meta:
        db_table = "provider"

    def __str__(self):
        return self.name
