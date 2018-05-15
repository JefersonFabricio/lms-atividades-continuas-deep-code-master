from django.db import models


class Curso(models.Model):
    #id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=3)  # Field name made lowercase.
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Curso'


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
    idcoordenador = models.IntegerField(db_column='IdCoordenador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disciplina'


class Disciplinaofertada(models.Model):
    #id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    idcoordenador = models.IntegerField(db_column='IdCoordenador')  # Field name made lowercase.
    dtiniciomatricula = models.DateField(db_column='DtInicioMatricula')  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='DtFimMatricula')  # Field name made lowercase.
    iddisciplina = models.IntegerField(db_column='IdDisciplina')  # Field name made lowercase.
    idcurso = models.IntegerField(db_column='IdCurso')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre')  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=1)  # Field name made lowercase.
    idprofessor = models.IntegerField(db_column='IdProfessor', blank=True, null=True)  # Field name made lowercase.
    metodoligia = models.CharField(db_column='Metodoligia', max_length=500, blank=True, null=True)  # Field name made lowercase.
    recursos = models.CharField(db_column='Recursos', max_length=500, blank=True, null=True)  # Field name made lowercase.
    criterioavaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=500, blank=True, null=True)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='PlanoDeAulas', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisciplinaOfertada'


# Create your models here.
