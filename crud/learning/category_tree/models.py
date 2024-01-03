from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.


class CategoryTree(models.Model):
    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Pending", "Pending"),
        ("Inactive", "Inactive"),
    )
    
    category_name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    gst_ret = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")
    image = models.CharField(max_length=100, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="category_tree_created"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="category_tree_updated"
    )
    deleted = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        db_table = "category_tree"
