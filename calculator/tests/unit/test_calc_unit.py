from calculator.calculator import calculate
import pytest

def test_soma():
    assert calculate(2, 3, "+") == 5

def test_potencia():
    assert calculate(2, 3, "^") == 8

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        calculate(10, 0, "/")
