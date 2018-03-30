from django.db import models
from django.db.models import Model

from estanteapp.models import ProfessorModel
from estanteapp.models.autor_model import AutorModel


class LivroModel(Model):

    titulo = models.CharField(max_length=100)
    resumo = models.TextField(max_length=255)

    autor = models.ForeignKey(AutorModel)
    dono = models.ForeignKey(ProfessorModel)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo
