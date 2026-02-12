from __future__ import annotations

import runpy
import warnings
from collections.abc import Callable

import pytest


def _get_func_por_nome(mod, nomes: list[str]):
    """Pega uma função pelo nome (lista de alternativas)."""
    for n in nomes:
        if hasattr(mod, n):
            return getattr(mod, n)
    return None


def _descobrir_func_bool(mod, nomes_preferidos: list[str], exemplo: str) -> Callable[[str], bool]:
    """
    Acha uma função que:
    - Recebe string
    - Retorna bool
    Isso evita teste quebrar só por diferença de nome.
    """
    # 1) tenta nomes preferidos primeiro
    f = _get_func_por_nome(mod, nomes_preferidos)
    if callable(f):
        r = f(exemplo)
        if isinstance(r, bool):
            return f

    # 2) fallback: varrer callables do módulo e testar com "exemplo"
    for nome in dir(mod):
        if nome.startswith("_") or nome == "main":
            continue
        obj = getattr(mod, nome)
        if not callable(obj):
            continue
        try:
            r = obj(exemplo)
        except Exception:
            continue
        if isinstance(r, bool):
            return obj

    raise AssertionError(
        f"Não encontrei função que receba str e retorne bool em {mod.__name__}."
    )


# --------------------------------
# Execução como módulo (entrypoint)
# --------------------------------

def test_entrypoint_importa_sem_executar():
    import dataviva_desafio.__main__ as m

    assert callable(m.main)


def test_entrypoint_roda_como_main(capsys):
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    runpy.run_module("dataviva_desafio.__main__", run_name="__main__")

    out = capsys.readouterr().out
    assert "Desafio 1" in out
    assert "Desafio 5" in out


@pytest.mark.parametrize(
    "modname",
    [
        "dataviva_desafio.desafio1_fizzbuzz",
        "dataviva_desafio.desafio2_palindromo",
        "dataviva_desafio.desafio3_duplicados",
        "dataviva_desafio.desafio4_parenteses",
        "dataviva_desafio.desafio5_agrupamento",
    ],
)
def test_modulos_rodam_como_main(modname: str, capsys):
    # Isso cobre as linhas do tipo: if __name__ == "__main__": main()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    runpy.run_module(modname, run_name="__main__")

    out = capsys.readouterr().out
    assert out.strip() != ""


# ----------------------------
# Desafio 1 - FizzBuzz
# ----------------------------

def test_fizzbuzz_valores_chave():
    import dataviva_desafio.desafio1_fizzbuzz as d1

    fizzbuzz_lines = _get_func_por_nome(d1, ["fizzbuzz_lines", "fizzbuzz_linhas"])
    assert callable(fizzbuzz_lines)

    linhas = fizzbuzz_lines()
    assert linhas[0] == "1"
    assert linhas[2] == "Fizz"
    assert linhas[4] == "Buzz"
    assert linhas[14] == "FizzBuzz"
    assert linhas[99] == "Buzz"


def test_fizzbuzz_main_roda(capsys):
    import dataviva_desafio.desafio1_fizzbuzz as d1

    d1.main()
    out = capsys.readouterr().out
    assert "Fizz" in out


# ----------------------------
# Desafio 2 - Palíndromo
# ----------------------------

def test_palindromo_borda_e_casefold():
    from dataviva_desafio.desafio2_palindromo import eh_palindromo

    assert eh_palindromo("arara") is True
    assert eh_palindromo("Arara") is True
    assert eh_palindromo("") is True
    assert eh_palindromo("casa") is False


def test_palindromo_type_error():
    from dataviva_desafio.desafio2_palindromo import eh_palindromo

    with pytest.raises(TypeError):
        eh_palindromo(123)  # type: ignore[arg-type]


def test_palindromo_main_roda(capsys):
    import dataviva_desafio.desafio2_palindromo as d2

    d2.main()
    out = capsys.readouterr().out
    assert "arara" in out.lower()


# ----------------------------
# Desafio 3 - Duplicados
# ----------------------------

def test_duplicados_encontra_e_sem_duplicado():
    import dataviva_desafio.desafio3_duplicados as d3

    func = _get_func_por_nome(
        d3,
        [
            "encontrar_duplicado",
            "encontrar_primeiro_duplicado",
            "find_first_duplicate",
        ],
    )
    assert callable(func)

    assert func([1, 2, 3, 4, 2, 5]) == 2
    assert func([1, 2, 3]) is None


def test_duplicados_type_error():
    import dataviva_desafio.desafio3_duplicados as d3

    func = _get_func_por_nome(
        d3,
        [
            "encontrar_duplicado",
            "encontrar_primeiro_duplicado",
            "find_first_duplicate",
        ],
    )
    assert callable(func)

    with pytest.raises(TypeError):
        func("123")  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        func([1, "2", 3])  # type: ignore[list-item]


def test_duplicados_main_roda(capsys):
    import dataviva_desafio.desafio3_duplicados as d3

    d3.main()
    out = capsys.readouterr().out
    assert "2" in out


# ----------------------------
# Desafio 4 - Parênteses
# ----------------------------

def test_parenteses_validos_e_invalidos():
    import dataviva_desafio.desafio4_parenteses as d4

    func = _descobrir_func_bool(
        d4,
        ["validar_parenteses", "is_valid_parentheses", "eh_valida_parenteses"],
        "{[()]}",
    )

    assert func("{[()]}") is True
    assert func("{[(])}") is False
    assert func("{{[[(]]}}") is False


def test_parenteses_type_error():
    import dataviva_desafio.desafio4_parenteses as d4

    func = _descobrir_func_bool(
        d4,
        ["validar_parenteses", "is_valid_parentheses", "eh_valida_parenteses"],
        "{[()]}",
    )

    with pytest.raises(TypeError):
        func(123)  # type: ignore[arg-type]


def test_parenteses_main_roda(capsys):
    import dataviva_desafio.desafio4_parenteses as d4

    d4.main()
    out = capsys.readouterr().out
    assert "-> True" in out or "-> False" in out


# ----------------------------
# Desafio 5 - Agrupamento
# ----------------------------

def test_agrupamento_exemplo_base():
    import dataviva_desafio.desafio5_agrupamento as d5

    func = _get_func_por_nome(d5, ["somar_por_categoria", "sum_by_category"])
    assert callable(func)

    dados = [
        {"categoria": "Alimentação", "valor": 10},
        {"categoria": "Transporte", "valor": 5},
        {"categoria": "Alimentação", "valor": 20},
        {"categoria": "Lazer", "valor": 50},
    ]
    assert func(dados) == {"Alimentação": 30, "Transporte": 5, "Lazer": 50}


def test_agrupamento_erros():
    import dataviva_desafio.desafio5_agrupamento as d5

    func = _get_func_por_nome(d5, ["somar_por_categoria", "sum_by_category"])
    assert callable(func)

    with pytest.raises(TypeError):
        func("x")  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        func([1, 2])  # type: ignore[list-item]

    with pytest.raises(ValueError):
        func([{"categoria": "A"}])


def test_agrupamento_main_roda(capsys):
    import dataviva_desafio.desafio5_agrupamento as d5

    d5.main()
    out = capsys.readouterr().out
    assert "alimentação" in out.lower()
