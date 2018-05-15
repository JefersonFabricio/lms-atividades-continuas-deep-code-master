from django.db import models


class Curso(models.Model):
    #id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curso'
