# Generated by Django 5.0 on 2024-01-15 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_orderentry_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterModelOptions(
            name='orderentry',
            options={},
        ),
        migrations.AlterField(
            model_name='orderentry',
            name='count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='orderentry',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
