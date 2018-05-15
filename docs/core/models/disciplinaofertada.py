from django.db import models
from .atividade import Atividade
from .disciplina import Disciplina
from .professor import Professor
from .coordenador import Coordenador
from .curso import Curso

class Disciplinaofertada(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='IdCoordenador')  # Field name made lowercase.
    dtiniciomatricula = models.DateField(db_column='DtInicioMatricula')  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='DtFimMatricula')  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre')  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=1)  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor', blank=True, null=True)  # Field name made lowercase.
    metodoligia = models.CharField(db_column='Metodoligia', max_length=500, blank=True, null=True)  # Field name made lowercase.
    recursos = models.CharField(db_column='Recursos', max_length=500, blank=True, null=True)  # Field name made lowercase.
    criterioavaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=500, blank=True, null=True)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='PlanoDeAulas', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisciplinaOfertada'

