from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(required=True)
    order_value = serializers.IntegerField(required=True)
    order_date = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance, given the validated data.
        """
        instance.order_id = validated_data.get('order_id', instance.order_id)
        instance.order_value = validated_data.get('order_value', instance.order_value)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.save()
        return instance