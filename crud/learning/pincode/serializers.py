from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from pincode.models import Pincode


class PincodeSerializer(serializers.ModelSerializer):
    zone_name = serializers.CharField(source="zone_id.zone_name", required=False)

    class Meta:
        model = Pincode
        fields = ["id", "zone_id", "zone_name", "pincode_number", "created_by", "updated_by"]

        extra_kwargs = {
            "created_by": {"write_only": True},
            "updated_by": {"write_only": True},
        }

    def validate(self, data):
        pincode_number = data.get("pincode_number")
        if self.instance and self.instance.pincode_number == pincode_number:
            return data

        if Pincode.objects.filter(pincode_number=pincode_number).exists():
            raise ValidationError(f"This Pincode {pincode_number} Already Exists")

        return data


# Pincode Multiple Delete :

class PincodeDeleteSerializer(serializers.ModelSerializer):
    deleted = serializers.ListField(write_only=True)

    class Meta:
        model = Pincode
        fields = ["deleted"]

    def create(self, validated_data):
        deleted_ids = validated_data.pop("deleted", [])
        for deleted_id in deleted_ids:
            try:
                pincode = Pincode.objects.get(id=deleted_id)
                pincode.deleted = 1
                pincode.save()
            except Pincode.DoesNotExist:
                raise serializers.ValidationError("Pincode does not exists")
            
        return pincode
    

# Pincode Multiple Archive :

class PincodeArchiveSerializer(serializers.ModelSerializer):
    deleted = serializers.ListField(write_only=True)
    
    class Meta:
        model = Pincode
        fields = ['deleted']

    def create(self, validated_data):
        deleted_ids = validated_data.pop("deleted", [])
        for deleted_id in deleted_ids:
            try:
                pincode = Pincode.objects.get(id=deleted_id)
                pincode.deleted = 0
                pincode.save()

            except Pincode.DoesNotExist:
                raise serializers.ValidationError("Pincode Does not exists")
            
        return pincode
