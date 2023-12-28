from rest_framework import serializers
from pincode.models import Pincode


class PincodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pincode
        fields = ["id", "zone_name", "pincode_number", "created_by", "updated_by"]
