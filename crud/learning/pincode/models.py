from django.db import models
from django.conf import settings
from django.utils.timezone import now

from zone.models import Zone

# Create your models here.


class Pincode(models.Model):
    zone_name = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True)
    pincode_number = models.CharField(max_length=100)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="pincode_created",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="pincode_updated",
    )
    deleted = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.pincode_number}"

    class Meta:
        db_table = "pincode"
