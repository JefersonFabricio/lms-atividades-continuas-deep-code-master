from django.db import models
from .aluno import Aluno
from .coordenador import Coordenador
from .disciplinaofertada import Disciplinaofertada


class Solicitacaomatricula(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    dtsolicitacao = models.DateField(db_column='DtSolicitacao')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='IdCoordenador', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolicitacaoMatricula'
