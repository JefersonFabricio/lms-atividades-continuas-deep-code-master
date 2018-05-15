from django.db import models


class Coordenador(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=30)  # Field name made lowercase.
    senha = models.IntegerField(db_column='Senha')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    celular = models.IntegerField(db_column='Celular')  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coordenador'
