# Generated by Django 3.1.5 on 2021-01-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20210105_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
