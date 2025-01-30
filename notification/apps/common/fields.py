from django.db import models
from django.utils import timezone
from ulid import ULID


class ULIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 26
        kwargs["unique"] = True
        kwargs["editable"] = True
        kwargs["default"] = self._generate_ulid
        super().__init__(*args, **kwargs)

    def _generate_ulid(self):
        return str(ULID.from_datetime(timezone.now()))
