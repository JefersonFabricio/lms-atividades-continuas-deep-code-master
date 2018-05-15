from core.utils.utils import calculaMediaFinal, geraNumeroRA, calculaMedia, descontaNota

def test_calculaMediaFinal():
    assert calculaMediaFinal(10,10) == 10
    assert calculaMediaFinal(10,0) == 6
    assert calculaMediaFinal(6,0) == 7.6
    assert calculaMediaFinal(10,4) == 8.4
    assert calculaMediaFinal(0,10) == 4
    assert calculaMediaFinal(8,4) == 6.4
    assert calculaMediaFinal(5,5) == 5
    assert calculaMediaFinal(11,11) == None
    assert calculaMediaFinal(-1,0) == None

def test_geraNumeroRA():
    assert geraNumeroRA(1800020) == 1800021
    assert geraNumeroRA(1701234) == 1800001
    assert geraNumeroRA('') == 1800001
    assert geraNumeroRA(1800999) == 1801000
    assert geraNumeroRA(1801234) == 1801235

def test_calculaMedia():
    assert calculaMedia(10.0,6.0,8.0) == 8.0
    assert calculaMedia(9.0,6.0,6.9,7.0) == 7.0
    assert calculaMedia(6.0,6.0,9.0,6.0,7.0,8.0,8.0) == 7.0
    assert calculaMedia(10.0,10.0,9.0,8.0,8.0,7.0,7.0,6.0,6.0) == 8.0

def test_descontaNota():
    assert descontaNota(8,30) == 5.6
    assert descontaNota(10,20) == 8.0
    assert descontaNota(7,25) == 5.25
    assert descontaNota(8,30) == 5.95
    assert descontaNota(6,20) == 4.8

