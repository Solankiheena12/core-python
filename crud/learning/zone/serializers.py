from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from zone.models import Zone


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ["id", "zone_name", "created_by", "updated_by"]

        extra_kwargs = {
            "created_by": {"write_only": True},
            "updated_by": {"write_only": True},
        }


    def validate_zone_name(self, value):
        if Zone.objects.filter(zone_name=value).exists(): 
            raise ValidationError("Zonename already existing")
        return value
    

# Zone name Multiple Delete :
    
class ZoneNameDeleteSerializer(serializers.ModelSerializer):
    deleted = serializers.ListField(write_only=True)

    class Meta:
        model = Zone
        fields = ["deleted"]

    def create(self, validated_data):
        deleted_ids = validated_data.pop("deleted", [])
        for deleted_id in deleted_ids:
            try:
                zonename = Zone.objects.get(id=deleted_id)
                zonename.deleted = 1
                zonename.save()
            except Zone.DoesNotExist:
                raise serializers.ValidationError("Zone name Does not exists")
            
        return zonename
    

class ZoneNameArchiveSerializer(serializers.ModelSerializer):
    deleted = serializers.ListField(write_only=True)

    class Meta:
        model = Zone
        fields = ['deleted']

    def create(self, validated_data):
        deleted_ids = validated_data.pop("deleted", [])
        for deleted_id in deleted_ids:
            try:
                zonename = Zone.objects.get(id=deleted_id)
                zonename.deleted = 0
                zonename.save()

            except Zone.DoesNotExist:
                raise serializers.ValidationError("Zone  name Does not exists")
        
        return zonename