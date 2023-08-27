# Generated by Django 4.2.3 on 2023-08-27 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contrats', '0036_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Effectif_Rh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Conducteurs', models.IntegerField()),
                ('contrat_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contrats.contrat')),
            ],
        ),
        migrations.CreateModel(
            name='Materiel_roulant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.DecimalField(decimal_places=2, max_digits=5)),
                ('capacite', models.CharField()),
                ('etet_satisfaction', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Patrimoine',
            fields=[
                ('id_patrimoine', models.AutoField(primary_key=True, serialize=False)),
                ('contrat_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contrats.contrat')),
            ],
        ),
        migrations.CreateModel(
            name='Type_MF',
            fields=[
                ('id_patrimoine', models.AutoField(primary_key=True, serialize=False)),
                ('contrat_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type_MR',
            fields=[
                ('id_categoie', models.AutoField(primary_key=True, serialize=False)),
                ('nom_categoie', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.AddField(
            model_name='patrimoine',
            name='id_Fixe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contrats.type_mf'),
        ),
        migrations.AddField(
            model_name='patrimoine',
            name='id_MR',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contrats.type_mr'),
        ),
        migrations.AddField(
            model_name='materiel_roulant',
            name='id_Fixe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contrats.type_mf'),
        ),
    ]
