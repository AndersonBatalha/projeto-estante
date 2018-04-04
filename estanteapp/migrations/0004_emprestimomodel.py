# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estanteapp', '0003_autormodel_livromodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmprestimoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_emprestimo', models.DateField(auto_now_add=True)),
                ('dia_devolucao', models.DateField(blank=True, null=True)),
                ('devolvido', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estanteapp.AlunoModel')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estanteapp.LivroModel')),
            ],
        ),
    ]
