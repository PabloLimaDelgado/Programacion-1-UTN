import pytest
from tp5_parte2 import *

@pytest.mark.parametrize("a, res",[
    ("43829992",True),
    ("3132",False),
])
def test_DNI(a, res):
    assert DNI(a) == res


@pytest.mark.parametrize("a, b, res",[
    (30, 10, 20),
    (33, 15, 24),
])
def test_cal_temp(a, b, res):
    assert cal_temp(a, b) == res


@pytest.mark.parametrize("a, res", [
     (20, "El área es: 1256 y el perímetro es 125."),
     (40.4, "El área es: 5127 y el perímetro es 253."),
])
def test_funcion_radio(a, res):
    assert funcion_radio(a) == res


@pytest.mark.parametrize("a, b, c, d, res", [
     ("usuario1", "asdasd", 1, 3, True),
     ("pablolima", "coctobdas3", 1, 3, False),
     ("usuario1", "asdasd", 3, 3, "Se agotaron el número de intentos"),
])
def test_login(a, b, c, d, res):
    assert login(a, b, c, d) == res


@pytest.mark.parametrize("a, res", [
     (20, False),
     (7, True),
])
def test_cousin(a, res):
    assert cousin(a) == res