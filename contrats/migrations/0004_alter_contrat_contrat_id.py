# Generated by Django 4.1.7 on 2023-08-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrats', '0003_rename_délégataire_contrat_délégataire_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrat',
            name='contrat_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]