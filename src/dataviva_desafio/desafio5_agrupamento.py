from __future__ import annotations

from typing import Any


def somar_por_categoria(transacoes: list[dict[str, Any]]) -> dict[str, int]:
    """
    Soma os valores por categoria.

    Prompt-alinhado:
    - 'categoria' deve ser string não vazia
    - 'valor' deve ser inteiro (o exemplo do enunciado retorna inteiros)
    """
    if not isinstance(transacoes, list):
        raise TypeError("transacoes deve ser list[dict]")

    acumulado: dict[str, int] = {}
    for t in transacoes:
        if not isinstance(t, dict):
            raise TypeError("cada transação deve ser dict")

        categoria = t.get("categoria")
        valor = t.get("valor")

        if not isinstance(categoria, str) or not categoria:
            raise ValueError("categoria inválida")

        if not isinstance(valor, int):
            raise ValueError("valor inválido (deve ser int)")

        acumulado[categoria] = acumulado.get(categoria, 0) + valor

    return acumulado


def main() -> None:
    entrada = [
        {"categoria": "Alimentação", "valor": 10},
        {"categoria": "Transporte", "valor": 5},
        {"categoria": "Alimentação", "valor": 20},
        {"categoria": "Lazer", "valor": 50},
    ]
    print(somar_por_categoria(entrada))


if __name__ == "__main__":
    main()
