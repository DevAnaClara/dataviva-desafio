import pytest

from dataviva_desafio.desafio1_fizzbuzz import fizzbuzz_linhas
from dataviva_desafio.desafio2_palindromo import eh_palindromo
from dataviva_desafio.desafio3_duplicados import encontrar_primeiro_duplicado
from dataviva_desafio.desafio4_parenteses import parenteses_validos
from dataviva_desafio.desafio5_agrupamento import somar_por_categoria


def test_fizzbuzz_regras_basicas():
    linhas = fizzbuzz_linhas(15)
    assert linhas[2] == "Fizz"         # 3
    assert linhas[4] == "Buzz"         # 5
    assert linhas[14] == "FizzBuzz"    # 15


def test_fizzbuzz_tipo_invalido():
    with pytest.raises(TypeError):
        fizzbuzz_linhas("100")  # type: ignore[arg-type]


def test_palindromo_exemplos_enunciado():
    assert eh_palindromo("arara") is True
    assert eh_palindromo("ovo") is True
    assert eh_palindromo("casa") is False


def test_palindromo_ignora_maiusculas():
    assert eh_palindromo("Arara") is True


def test_palindromo_tipo_invalido():
    with pytest.raises(TypeError):
        eh_palindromo(123)  # type: ignore[arg-type]


def test_duplicado_exemplo_enunciado():
    assert encontrar_primeiro_duplicado([1, 2, 3, 4, 2, 5]) == 2


def test_duplicado_quando_nao_existe():
    assert encontrar_primeiro_duplicado([1, 2, 3]) is None


def test_duplicado_tipo_invalido():
    with pytest.raises(TypeError):
        encontrar_primeiro_duplicado("123")  # type: ignore[arg-type]


def test_parenteses_exemplos_enunciado():
    assert parenteses_validos("{[()]}") is True
    assert parenteses_validos("{[(])}") is False
    assert parenteses_validos("{{[[(]]}}") is False


def test_parenteses_string_vazia_valida():
    assert parenteses_validos("") is True


def test_parenteses_tipo_invalido():
    with pytest.raises(TypeError):
        parenteses_validos(123)  # type: ignore[arg-type]


def test_agrupamento_exemplo_enunciado():
    entrada = [
        {"categoria": "Alimentação", "valor": 10},
        {"categoria": "Transporte", "valor": 5},
        {"categoria": "Alimentação", "valor": 20},
        {"categoria": "Lazer", "valor": 50},
    ]
    assert somar_por_categoria(entrada) == {"Alimentação": 30, "Transporte": 5, "Lazer": 50}


def test_agrupamento_invalidos():
    with pytest.raises(TypeError):
        somar_por_categoria("x")  # type: ignore[arg-type]

    with pytest.raises(ValueError):
        somar_por_categoria([{"categoria": "A"}])  # faltou valor

    with pytest.raises(ValueError):
        somar_por_categoria([{"categoria": "A", "valor": 2.5}])  # float não permitido
