from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "about_me",
            "last_login",
            "email",
            "designation",
            "phone",
            "message",
            "is_active",
            "status",
            "emergency_contact",
            "current_address",
            "permanent_address",
        ]

        
