import orderbook.models as models
from rest_framework import serializers
import datetime
from orderbook.tasks import run_matching_task


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Token
        fields = ["name", "id"]
        read_only_fields = ["id"]


class OrderSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context["request"]

        new_order = models.Order.objects.create(
            user=request.user,
            token=validated_data["token"],
            price=validated_data["price"],
            quantity=validated_data["quantity"],
            order_type=validated_data["order_type"],
            timestamp=datetime.datetime.now(),
        )
        return new_order

    class Meta:
        model = models.Order
        fields = ["id", "token", "price", "quantity", "order_type", "timestamp"]
        read_only_fields = ["id", "timestamp"]


class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ["id", "token", "price", "quantity", "timestamp"]
        read_only_fields = ["id", "timestamp"]
