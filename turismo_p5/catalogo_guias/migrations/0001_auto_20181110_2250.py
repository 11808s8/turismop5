# Generated by Django 2.1.3 on 2018-11-10 22:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogo_guias', 'instancia_postgis_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagens', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('infos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa_Fisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=80)),
                ('telefone', models.PositiveIntegerField()),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=14)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoa_Juridica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=80)),
                ('telefone', models.PositiveIntegerField()),
                ('cnpj', models.CharField(max_length=14)),
                ('razao_social', models.CharField(max_length=150)),
                ('avaliacao', models.FloatField()),
                ('numeroRegistro', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponto', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_conta', models.IntegerField()),
                ('descricao', models.TextField()),
                ('quantia', models.FloatField()),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Roteiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('avaliacao', models.FloatField()),
                ('guias', models.ForeignKey(on_delete=None, to='catalogo_guias.Pessoa_Juridica')),
                ('rota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_guias.Destino')),
            ],
        ),
        migrations.AddField(
            model_name='mapa',
            name='pontos',
            field=models.ForeignKey(on_delete=None, to='catalogo_guias.Ponto'),
        ),
        migrations.AddField(
            model_name='destino',
            name='ponto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_guias.Ponto'),
        ),
    ]