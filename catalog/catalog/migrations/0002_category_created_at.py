# Generated by Django 4.2.7 on 2023-11-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=1, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
