# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estanteapp', '0002_alunomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LivroModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('resumo', models.TextField(max_length=255)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estanteapp.AutorModel')),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estanteapp.ProfessorModel')),
            ],
        ),
    ]
