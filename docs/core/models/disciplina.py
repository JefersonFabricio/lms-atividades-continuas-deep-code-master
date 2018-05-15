from django.db import models
from .coordenador import Coordenador


class Disciplina(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    data = models.DateField(db_column='Data')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    planodeensino = models.CharField(db_column='PlanoDeEnsino', max_length=2000)  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    competencias = models.CharField(db_column='Competencias', max_length=500)  # Field name made lowercase.
    habilidades = models.CharField(db_column='Habilidades', max_length=500)  # Field name made lowercase.
    ementa = models.CharField(db_column='Ementa', max_length=500)  # Field name made lowercase.
    conteudoprogramatico = models.CharField(db_column='ConteudoProgramatico', max_length=500)  # Field name made lowercase.
    bibliografiabasica = models.CharField(db_column='BibliografiaBasica', max_length=500)  # Field name made lowercase.
    bibliografiacomplentar = models.CharField(db_column='BibliografiaComplentar', max_length=500)  # Field name made lowercase.
    percentualpratico = models.IntegerField(db_column='PercentualPratico')  # Field name made lowercase.
    percentualteorico = models.IntegerField(db_column='PercentualTeorico')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='IdCoordenador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disciplina'
