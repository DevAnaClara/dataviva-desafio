from __future__ import annotations


def eh_palindromo(palavra: str) -> bool:
    """
    Retorna True se a palavra for palíndromo, False caso contrário.

    Decisão de design (explicada):
    - O enunciado fala "palavra". Então o padrão é estrito (não removo espaços/pontuação).
    - Porém, uso casefold() para ignorar maiúsculas/minúsculas (ex.: "Arara" -> True),
      porque isso é um detalhe comum e não muda o conceito de palíndromo para palavras.
    """
    if not isinstance(palavra, str):
        raise TypeError("palavra deve ser str")

    p = palavra.casefold()
    return p == p[::-1]


def main() -> None:
    exemplos = ["arara", "ovo", "casa", "Arara"]
    for e in exemplos:
        print(f"{e!r} -> {eh_palindromo(e)}")


if __name__ == "__main__":
    main()
