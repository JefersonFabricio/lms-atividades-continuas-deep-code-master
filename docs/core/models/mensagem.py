from django.db import models
from .aluno import Aluno
from .professor import Professor



class Mensagem(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.
    assunto = models.CharField(db_column='Assunto', max_length=50)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=300)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=2000)  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase. This field type is a guess.
    dtenvio = models.DateField(db_column='DtEnvio')  # Field name made lowercase.
    dtresposta = models.DateField(db_column='DtResposta', blank=True, null=True)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mensagem'
