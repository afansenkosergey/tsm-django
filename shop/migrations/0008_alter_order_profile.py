# Generated by Django 5.0 on 2024-01-14 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_orderentry_options_alter_profile_shopping_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.profile'),
        ),
    ]
