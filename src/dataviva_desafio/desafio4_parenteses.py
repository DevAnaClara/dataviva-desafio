from __future__ import annotations


def parenteses_validos(texto: str) -> bool:
    """
    Valida se a string de parênteses/chaves/colchetes é válida.

    Estrutura: pilha (stack).
    - Abriu: empilha.
    - Fechou: precisa bater com o topo; senão é inválido.
    """
    if not isinstance(texto, str):
        raise TypeError("texto deve ser str")

    pares = {")": "(", "}": "{", "]": "["}
    abertos = set(pares.values())

    pilha: list[str] = []
    for ch in texto:
        # Enunciado diz que a string contém apenas esses caracteres.
        # Se vier algo diferente, considero inválido (mais seguro e explícito).
        if ch in abertos:
            pilha.append(ch)
        elif ch in pares:
            if not pilha:
                return False
            topo = pilha.pop()
            if topo != pares[ch]:
                return False
        else:
            return False

    return len(pilha) == 0


def main() -> None:
    exemplos = ["{[()]}", "{[(])}", "{{[[(]]}}"]
    for e in exemplos:
        print(f"{e} -> {parenteses_validos(e)}")


if __name__ == "__main__":
    main()
