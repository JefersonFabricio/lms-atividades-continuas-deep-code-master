from django.db import models
from .professor import Professor


class Atividade(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=30)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=300, blank=True, null=True)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=20)  # Field name made lowercase.
    extras = models.CharField(db_column='Extras', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Atividade'

