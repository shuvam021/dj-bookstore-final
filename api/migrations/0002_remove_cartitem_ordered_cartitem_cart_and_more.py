# Generated by Django 4.1.1 on 2022-10-04 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="ordered",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="api.cart"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cart",
            name="cart_items",
            field=models.ManyToManyField(related_name="cart_items", to="api.cartitem"),
        ),
    ]
