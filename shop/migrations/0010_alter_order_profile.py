# Generated by Django 5.0 on 2024-01-14 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_profile_shopping_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.profile'),
        ),
    ]
