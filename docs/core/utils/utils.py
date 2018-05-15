import datetime
from difflib import SequenceMatcher

def calculaMediaFinal(ac,prova):
    media=ac*0.6+prova*0.4
    if ac < 0 or prova<0:
        return None
    elif ac > 10 or prova > 10:
        return None
    else:
        return media

def geraNumeroRA(uRA):
    if (len(str(uRA))== 7 or (format(uRA/100000, '.0f') == datetime.datetime.now().strftime('%y'))):
        Novo_RA=uRA+1
        return Novo_RA
    elif(len(format(str(uRA)[2:]))!=5):
        return (datetime.datetime.now().strftime('%y') + '{:0>5}'.format(str(uRA)[-4:]))

def calculaMedia(listaNotas):
    total=0
    x = len(listaNotas)
    for i in listaNotas:
        total+= i
    y = total/x
    return y

def descontaNota(nota, procentagem):
    porc = procentagem/100
    resultado = nota - (nota*porc)
    return resultado

def Copia(texto1, texto2):
    total = SequenceMatcher(None, texto1, texto2).ratio()
    if total > 0.8:
        return True
    
    else:
        return  False
