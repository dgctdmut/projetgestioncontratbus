# Generated by Django 4.1.7 on 2023-08-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrats', '0004_alter_contrat_contrat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrat',
            name='contrat_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
