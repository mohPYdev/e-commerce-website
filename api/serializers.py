from rest_framework import serializers
from main.models import OrderItem , Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        depth = 1
        fields = (
            'quantity',
            'date_added',
            'product'
        )



