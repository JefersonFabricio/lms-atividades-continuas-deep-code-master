from django.db import models
from .aluno import Aluno
from .atividadevinculada import Atividadevinculada
from .professor import Professor
from.disciplinaofertada import Disciplinaofertada
from.solicitacaomatricula import Solicitacaomatricula

class Entrega(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='IdAtividadeVinculada')  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=50)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=500)  # Field name made lowercase.
    dtentrega = models.DateField(db_column='DtEntrega')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor', blank=True, null=True)  # Field name made lowercase.
    nota = models.TextField(db_column='Nota', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dtavaliacao = models.DateField(db_column='DtAvaliacao', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=300, blank=True, null=True)  # Field name made lowercase.
    def get_alunoAtividadeEntregue(self):
        if self.idaluno==Aluno.id and self.status == "Entregue":
            return Aluno.nome
    def get_alunoAtividadeNaoEntregue(self):
        if self.idaluno==Aluno.id and self.status != "Entregue":
            return Aluno.nome

    def get_atividadeEntregue(self):
        listaAtividade=[]
        matricula = Solicitacaomatricula()
        for disci in matricula:
            if disci.idaluno == self.idaluno and disci.status == "Aprovado":
                if self.status == "Entregue":
                    listaAtividade = self.idatividadevinculada
        def get_atividadeNaoEntregue(self):
            listaAtividade=[]
            matricula = Solicitacaomatricula()
            for disci in matricula:
                if disci.idaluno == self.idaluno and disci.status == "Aprovado":
                    if self.status !="Entregue":
                        listaAtividade = self.idatividadevinculada

    class Meta:
        managed = False
        db_table = 'Entrega'
