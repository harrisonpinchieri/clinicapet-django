# Generated by Django 4.2.7 on 2023-12-03 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('motivo_consulta', models.CharField(max_length=200)),
                ('peso_atual', models.FloatField()),
                ('medicamento_atual', models.TextField(blank=True)),
                ('medicamentos_prescritos', models.TextField(blank=True)),
                ('exames_prescritos', models.TextField(blank=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pet')),
            ],
        ),
    ]
