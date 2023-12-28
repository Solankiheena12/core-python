from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    STATUS_CHOICES = (
        ("pending", "pending"),
        ("active", "active"),
        ("inactive", "inactive"),
    )
    username = models.CharField(max_length=60, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="")
    about_me = models.CharField(max_length=100, null=True)
    last_login = models.DateTimeField(_("last login"), null=True)
    email = models.EmailField(_("email address"), unique=True)
    designation = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=15, null=True)
    message = models.CharField(max_length=200, default="")
    is_active = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default="Pending", max_length=25)
    emergency_contact = models.CharField(max_length=15, null=True)
    current_address = models.CharField(max_length=150, null=True)
    permanent_address = models.CharField(max_length=150, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"
        ordering = ["-id"]
