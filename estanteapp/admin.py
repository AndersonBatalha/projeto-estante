# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from estanteapp.models import ProfessorModel, AlunoModel, AutorModel, LivroModel

# Register your models here.

admin.site.register(ProfessorModel)
admin.site.register(AlunoModel)
admin.site.register(AutorModel)
admin.site.register(LivroModel)
