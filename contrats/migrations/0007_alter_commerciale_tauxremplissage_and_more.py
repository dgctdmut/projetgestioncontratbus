# Generated by Django 4.2.3 on 2023-08-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrats', '0006_commerciale_commercialesecond'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commerciale',
            name='tauxremplissage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='commerciale',
            name='tauxtransportvide',
            field=models.IntegerField(),
        ),
    ]
