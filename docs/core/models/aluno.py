from django.db import models
from .disciplinaofertada import Disciplinaofertada

class Aluno(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=30)  # Field name made lowercase.
    senha = models.IntegerField(db_column='Senha')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    celular = models.IntegerField(db_column='Celular')  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA')  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.nome = nome

    def getEmail(self):
        return self.email

    def setEmail(self,email):
        self.email = email

    def getRa(self):
        return self.ra

    def setRa(self,ra):
        self.ra = ra

    def getCelular(self):
        return self.celular

    def setCelular(self,celular):
        self.__celular = celular
    def getDesconto(self):
        return self.desconto

    def setDesconto(self,desconto):
        self.__desconto = desconto
    
    def retornaSobrenome(self):
        return ' '.join(self.nome.split(' ')[1:])
    
    def aumentarDesconto(self,desconto):
        if desconto > self.desconto:
            self.desconto = desconto
        else:
            return print("Desconto inserido é menor que desconto atual")
    def diminuiDesconto(self,desconto):
        if desconto < self.desconto:
            self.desconto = desconto
        else:
            return print("Desconto inserido é maior que desconto atual")
    
    
    class Meta:
        managed = False
        db_table = 'Aluno'
