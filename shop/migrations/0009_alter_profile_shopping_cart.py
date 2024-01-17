# Generated by Django 5.0 on 2024-01-14 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_order_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='shopping_cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shopping_cart', to='shop.order'),
        ),
    ]
