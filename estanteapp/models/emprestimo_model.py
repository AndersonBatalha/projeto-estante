from django.db import models
from django.db.models import Model

from estanteapp.models import LivroModel, AlunoModel


class EmprestimoModel(Model):

    livro = models.ForeignKey(LivroModel)
    aluno = models.ForeignKey(AlunoModel)

    dia_emprestimo = models.DateField(auto_now_add=True)
    dia_devolucao = models.DateField(blank=True, null=True)

    devolvido = models.BooleanField(default=False)