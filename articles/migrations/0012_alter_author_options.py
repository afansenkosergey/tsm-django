# Generated by Django 5.0 on 2024-01-07 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_author_date_of_birth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name'], 'verbose_name': 'Авторы', 'verbose_name_plural': 'Авторы'},
        ),
    ]