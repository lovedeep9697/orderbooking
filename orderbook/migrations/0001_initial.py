# Generated by Django 5.1.7 on 2025-03-28 10:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.IntegerField()),
                (
                    "order_type",
                    models.CharField(
                        choices=[("bid", "bid"), ("ask", "ask")], max_length=10
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[("open", "open"), ("executed", "executed")],
                        default="open",
                        max_length=10,
                    ),
                ),
                ("executed_timestamp", models.DateTimeField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "token",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="orders",
                        to="orderbook.token",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.IntegerField()),
                ("timestamp", models.DateTimeField()),
                (
                    "ask_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ask_orders",
                        to="orderbook.order",
                    ),
                ),
                (
                    "bid_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="bid_orders",
                        to="orderbook.order",
                    ),
                ),
                (
                    "token",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="trades",
                        to="orderbook.token",
                    ),
                ),
            ],
        ),
    ]
