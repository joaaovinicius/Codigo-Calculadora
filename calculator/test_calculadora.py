from calculator.calculator import somar, subtrair, multiplicar, dividir


def test_somar():
    assert calculadora.somar(2, 3) == 5
    assert calculadora.somar(-1, 1) == 0
    assert calculadora.somar(10.5, 0.5) == 11

def test_subtrair():
    assert calculadora.subtrair(5, 3) == 2
    assert calculadora.subtrair(1, 1) == 0
    assert calculadora.subtrair(-2, -3) == 1

def test_multiplicar():
    assert calculadora.multiplicar(2, 3) == 6
    assert calculadora.multiplicar(0, 10) == 0
    assert calculadora.multiplicar(-2, 4) == -8

def test_dividir():
    assert calculadora.dividir(6, 3) == 2
    assert calculadora.dividir(10, 2) == 5

def test_dividir_por_zero():
    assert calculadora.dividir(5, 0) == "Erro: divisão por zero!"
