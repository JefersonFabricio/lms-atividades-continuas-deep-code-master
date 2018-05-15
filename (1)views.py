from django.db import models
from disciplinas import Disciplina
from professores import Professor
from Pessoa import Pessoa
# p1.adicionaDisciplina(d1)
# print('Carga horária professor:', 
#             p1.retornaCargaHoraria())


# print('Valor/hora disciplina: ',
#             d1.retornaValorHora()) 


class Pessoa(models.Model):
        nome = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        celular = models.CharField(max_length=9)
        logon = models.CharField(max_length=15)
        senha = models.CharField(max_length=15)
        data_expircao = models.DateField(default=TimeZone)

    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])
    

    def retornaCargaHoraria(self):
        return "Metodo nao implementado"
    class Meta:
        abstract = True

class Professor:

    def __init__(self, nome='', email='', ra='',
        celular=''):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular        
        self.__disciplinas = []

    def getNome(self):
        return self.__nome        
    def setNome(self, nome):
        self.__nome = nome
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email
    def getRa(self):
        return self.__ra
    def setRa(self, ra):
        self.__ra = ra

    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])

    def adicionaDisciplina(self, disciplina):
        if disciplina.getProfessor().getRa() == self.__ra:
            self.__disciplinas.append(disciplina)
        else:
            return 'Professor não associado a disciplina'

    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplinas:
            soma_carga += d.getCargaHoraria()/20
        return soma_carga



# class Disciplina:

#     def __init__(self, nome='', cargaHoraria=0, 
#         mensalidade=0.0, professor=None):
#         self.__nome = nome
#         self.__cargaHoraria = cargaHoraria
#         self.__mensalidade = mensalidade
#         self.__professor = professor

#     def getNome(self):
#         return self.__nome
    
#     def setNome(self, nome):
#         self.__nome = nome

#     def getCargaHoraria(self):
#         return self.__cargaHoraria

#     def setCargaHoraria(self, cargaHoraria):
#         self.__cargaHoraria = cargaHoraria

#     def getMensalidade(self):
#         return self.__mensalidade

#     def setMensalidade(self, mensalidade):
#         self.__mensalidade = mensalidade

#     def getProfessor(self):
#         return self.__professor

#     def setProfessor(self, professor):
#         self.__professor = professor

    # def retornaValorHora(self):
    #     valor = self.__mensalidade * 6 / self.__cargaHoraria
    #     return valor


class Professor:
    def retornaCargaHoraria(self):
        cargaTotal=0
        for disc in self.__disciplinas
            cargaTotal += dosc.getCargaHoraria() /20
        return cargaTotal
