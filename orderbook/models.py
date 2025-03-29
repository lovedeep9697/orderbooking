from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    """
    Model to represent Tokens in orderbooking system.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Model to represent orders in orderbooking system.
    """

    ORDER_TYPE_CHOICES = [
        ("bid", "bid"),
        ("ask", "ask"),
        # There can be more order types in future.
    ]

    ORDER_STATUS_CHOICES = [
        ("open", "open"),
        ("executed", "executed"),
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    token = models.ForeignKey(Token, on_delete=models.PROTECT, related_name="orders")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES)
    timestamp = models.DateTimeField()
    status = models.CharField(
        max_length=10, choices=ORDER_STATUS_CHOICES, default="open"
    )
    executed_timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.user}-{self.token}-{self.price}-{self.quantity}-{self.order_type}-{self.status}"


class Trade(models.Model):
    """
    Model to represent trades in orderbooking system.
    """

    token = models.ForeignKey(Token, on_delete=models.PROTECT, related_name="trades")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()
    bid_order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="bid_orders"
    )
    ask_order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="ask_orders"
    )

    def __str__(self):
        return f"{self.token}-{self.price}-{self.quantity}-{self.bid_order}-{self.ask_order}"
