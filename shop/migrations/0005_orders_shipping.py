# Generated by Django 4.1 on 2023-04-27 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_orders_payment_shipping_remove_orderitem_order_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="shipping",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.shipping",
            ),
        ),
    ]