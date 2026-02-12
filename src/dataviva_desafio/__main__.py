from __future__ import annotations

"""
Ponto de entrada do pacote.

Permite rodar:
    python -m dataviva_desafio

Decisão de design (explicada):
- Os imports dos desafios ficam dentro da função main() para evitar problemas de ordem de imports
  (E402) e para manter a inicialização simples.
"""

def main() -> None:
    # Imports locais (intencional) para evitar E402 e deixar o arquivo mais robusto.
    from dataviva_desafio.desafio1_fizzbuzz import main as main_fizzbuzz
    from dataviva_desafio.desafio2_palindromo import main as main_palindromo
    from dataviva_desafio.desafio3_duplicados import main as main_duplicados
    from dataviva_desafio.desafio4_parenteses import main as main_parenteses
    from dataviva_desafio.desafio5_agrupamento import main as main_agrupamento

    print("=== Desafio 1: FizzBuzz ===")
    main_fizzbuzz()
    print()

    print("=== Desafio 2: Palíndromo ===")
    main_palindromo()
    print()

    print("=== Desafio 3: Duplicados ===")
    main_duplicados()
    print()

    print("=== Desafio 4: Validação de Parênteses ===")
    main_parenteses()
    print()

    print("=== Desafio 5: Agrupamento por Categoria ===")
    main_agrupamento()


if __name__ == "__main__":
    main()
