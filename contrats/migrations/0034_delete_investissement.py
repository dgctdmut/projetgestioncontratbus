# Generated by Django 4.2.3 on 2023-08-16 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrats', '0033_alter_investissement_partenaire_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Investissement',
        ),
    ]