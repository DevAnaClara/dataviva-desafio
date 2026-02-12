from __future__ import annotations


def encontrar_primeiro_duplicado(numeros: list[int]) -> int | None:
    """
    Retorna o primeiro número que aparece repetido durante a varredura.

    Por que set?
    - Consulta O(1) em média para saber se já vimos o número.
    - Mantém a solução simples e eficiente.

    Se não houver duplicados, retorno None (contrato explícito).
    """
    if not isinstance(numeros, list):
        raise TypeError("numeros deve ser list[int]")

    vistos: set[int] = set()
    for x in numeros:
        if not isinstance(x, int):
            raise TypeError("todos os elementos devem ser int")

        if x in vistos:
            return x
        vistos.add(x)

    return None


def main() -> None:
    print(encontrar_primeiro_duplicado([1, 2, 3, 4, 2, 5]))


if __name__ == "__main__":
    main()
