# Generated by Django 5.0 on 2024-01-13 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order_orderentry_order_order_entries_profile_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderentry',
            options={'verbose_name': 'Добавлено ы корзину', 'verbose_name_plural': 'Добавлено в корзину'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профили', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterField(
            model_name='orderentry',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.product'),
        ),
    ]
