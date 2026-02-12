from __future__ import annotations


def fizzbuzz_linhas(n: int = 100) -> list[str]:
    """
    Gera a saída do FizzBuzz de 1 até n.

    Decisão: checar múltiplo de 15 primeiro simplifica a lógica (3 e 5 ao mesmo tempo).
    """
    if not isinstance(n, int):
        raise TypeError("n deve ser int")
    if n < 1:
        return []

    saida: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            saida.append("FizzBuzz")
        elif i % 3 == 0:
            saida.append("Fizz")
        elif i % 5 == 0:
            saida.append("Buzz")
        else:
            saida.append(str(i))
    return saida


def main() -> None:
    # Enunciado pede imprimir de 1 a 100.
    for linha in fizzbuzz_linhas(100):
        print(linha)


if __name__ == "__main__":
    main()
