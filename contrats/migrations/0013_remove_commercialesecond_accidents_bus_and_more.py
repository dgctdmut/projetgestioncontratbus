# Generated by Django 4.2.3 on 2023-08-12 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrats', '0012_commercialesecond_accidents_bus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercialesecond',
            name='accidents_bus',
        ),
        migrations.RemoveField(
            model_name='commercialesecond',
            name='pannes_bus',
        ),
    ]