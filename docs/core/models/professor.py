from django.db import models


class Professor(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=30)  # Field name made lowercase.
    senha = models.IntegerField(db_column='Senha')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    celular = models.IntegerField(db_column='Celular')  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=30)  # Field name made lowercase.
    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.novo_nome=nome
        self.nome=self.novo_nome

    def getEmail(self):
        return self.email

    def setEmail(self,email):
        self.novo_email=email
        self.email=self.novo_email

    def getRa(self):
        return self.ra

    def setRa(self,ra):
        self.novo_ra=ra
        self.ra=self.ra

    def getCelular(self):
        return self.celular

    def setCelular(self,celular):
        self.novo_celular=celular
        self.celular=self.novo_celular

    
    def retornaSobrenome(self):
        return ' '.join(self.nome.split(' ')[1:])

    
  
    class Meta:
        managed = False
        db_table = 'Professor'