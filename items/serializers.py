
from rest_framework import serializers
from .models import Items, Order






class OrderSerializer(serializers.ModelSerializer):
    # order = serializers.StringRelatedField(many=True)
    # order = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Order
        fields = [
            "id",
            "cus_name",
        ]


class ItemSerializer(serializers.ModelSerializer):
    # order = OrderSerializer()
    class Meta:
        model = Items
        fields = [
            "id",
            "product_name",
            "quantity",
            "order"
        ]
        depth = 1
        