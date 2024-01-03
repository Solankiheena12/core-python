from rest_framework import serializers

from category_tree.models import CategoryTree


class CategoryTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTree
        fields = ["id", "category_name", "description", "gst_ret", "status", "image", "created_by", "updated_by"]

        extra_kwargs = {
            "created_by": {"write_only": True},
            "updated_by": {"write_only": True},
        }


class CategoryTreeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTree
        fields = ["status"]


class CategoryTreeDeleteViewSet(serializers.ModelSerializer):
    deleted = serializers.ListField(write_only=True)

    class Meta:
        model = CategoryTree
        fields = ["deleted"]

    def create(self, validated_data):
        deleted_ids = validated_data.pop("deleted", [])
        for deleted_id in deleted_ids:
            try:
                categorytree = CategoryTree.objects.get(id=deleted_id)
                categorytree.deleted = 1
                categorytree.save()
            except CategoryTree.DoesNotExist:
                raise serializers.ValidationError("Category Tree Does Not Exist")

        return categorytree
