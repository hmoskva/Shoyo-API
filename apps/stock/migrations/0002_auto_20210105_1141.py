# Generated by Django 3.1.5 on 2021-01-05 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flavours', '0002_remove_flavour_stock'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='flavour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock', to='flavours.flavour'),
        ),
    ]
