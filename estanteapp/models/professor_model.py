from django.contrib.auth.models import User
from django.db import models


class ProfessorModel(User):
    materia = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name
