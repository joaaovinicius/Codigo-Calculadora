from calculator import calculator
import pytest

def test_somar():
    assert calculator.somar(2, 3) == 5
    assert calculator.somar(-1, 1) == 0
    assert calculator.somar(10.5, 0.5) == 11

def test_subtrair():
    assert calculator.subtrair(5, 3) == 2
    assert calculator.subtrair(1, 1) == 0
    assert calculator.subtrair(-2, -3) == 1

def test_multiplicar():
    assert calculator.multiplicar(2, 3) == 6
    assert calculator.multiplicar(0, 10) == 0
    assert calculator.multiplicar(-2, 4) == -8

def test_dividir():
    assert calculator.dividir(6, 3) == 2
    assert calculator.dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        calculator.dividir(5, 0)
