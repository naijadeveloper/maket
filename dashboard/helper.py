from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_range(value):
  if value < 1 or value > 5:
    raise ValidationError(
      _("%(value)s is either less than 1 or greater than 5"),
      params={"value": value},
    )


def validate_range_banner(value):
  if value < 1 or value > 4:
    raise ValidationError(
      _("%(value)s is either less than 1 or greater than 4"),
      params={"value": value},
    )