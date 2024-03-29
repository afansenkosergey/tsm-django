# Generated by Django 5.0 on 2023-12-22 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_options_remove_article_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Список статей', 'verbose_name_plural': 'Список статей'},
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 12, 22, 21, 12, 27, 976026, tzinfo=datetime.timezone.utc), verbose_name='Дата публикации'),
            preserve_default=False,
        ),
    ]
