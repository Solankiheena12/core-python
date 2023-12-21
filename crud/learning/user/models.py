from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.


class User(models.Model):

    STATUS_CHOICE = (
        ("active", "active"),
        ("pending", "pending"),
        ("inactive", "inacive"),
    )

    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    status = models.CharField(choices= STATUS_CHOICE, default= "pending", max_length=30)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="user_created"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="user_updated"
    )

    deleted = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.username}{self.email}"

    class Meta:
        db_table = "user"
