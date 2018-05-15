from django.db import models
from .atividade import Atividade
from .professor import Professor
from .disciplinaofertada import Disciplinaofertada

class Atividadevinculada(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='IdAtividade')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    rotulo = models.CharField(db_column='Rotulo', max_length=5)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    dtiniciorespostas = models.DateField(db_column='DtInicioRespostas')  # Field name made lowercase.
    dtfimrespostas = models.DateField(db_column='DtFimRespostas')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AtividadeVinculada'
