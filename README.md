# Desafio Técnico – Bolsa de Pesquisa (DataViva)


Objetivo:
- raciocínio de programação
- uso de estruturas de dados adequadas
- decisões explícitas de design (com trade-offs)
- código organizado e testável
- validação automatizada (tests + lint + CI)

---

## ✅ Requisitos

- **Python 3.10+**
- Windows / Linux / macOS
- Git

> No Windows, eu recomendo rodar todos os comandos com `python -m ...`  
> (isso evita problemas de bloqueio do `pip.exe` por políticas corporativas).

---

## 📁 Estrutura do projeto

<img width="667" height="583" alt="image" src="https://github.com/user-attachments/assets/c8e90b30-0ccb-430e-b140-4265810be10c" />



---

## 🧠 Como eu pensei (visão geral)

A proposta do desafio é simples, então a forma de se destacar é:

1. **Organização clara:** 1 arquivo por desafio.
2. **Funções pequenas e focadas:** cada solução é uma função principal + (quando necessário) helpers.
3. **Validação explícita de tipos:** se a entrada for inválida, levanto `TypeError` / `ValueError`.
4. **Testes cobrindo comportamento e bordas:** feliz + triste + casos extremos.
5. **Reprodutibilidade:** qualquer pessoa consegue rodar localmente com poucos comandos.
6. **Qualidade automática:** `ruff` e `pytest` rodando também no GitHub Actions (CI).

---

## 🚀 Instalação (modo desenvolvimento)

### 1) Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd dataviva-desafio

2) Criar e ativar ambiente virtual

Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

Windows (cmd)
python -m venv .venv
.\.venv\Scripts\activate.bat

Linux/macOS
python -m venv .venv
source .venv/bin/activate

3) Instalar dependências de desenvolvimento

python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt

4) Instalar o pacote em modo editável

python -m pip install -e .
Isso permite importar dataviva_desafio como pacote, e rodar python -m dataviva_desafio.

###▶️ Como executar

python -m dataviva_desafio
Isso roda um “resumo” chamando o main() de cada desafio e imprime exemplos no terminal.

Executar um desafio isoladamente

python -m dataviva_desafio.desafio1_fizzbuzz
python -m dataviva_desafio.desafio2_palindromo
python -m dataviva_desafio.desafio3_duplicados
python -m dataviva_desafio.desafio4_parenteses
python -m dataviva_desafio.desafio5_agrupamento

###✅ Como testar (pytest)

Rodar testes rápidos:

python -m pytest -q
Rodar testes com cobertura e relatório:

python -m pytest -q --cov=dataviva_desafio --cov-report=term-missing --cov-fail-under=95
A cobertura mínima exigida é 95%, mas o projeto foi preparado para atingir alta cobertura incluindo caminhos reais de execução.

###🧹 Lint / Qualidade (ruff)
Verificar lint:

python -m ruff check .
Tentar corrigir automaticamente o que for possível:

python -m ruff check . --fix
###🤖 CI (GitHub Actions)
O repositório possui um workflow em .github/workflows/ci.yml que executa:

ruff check .

pytest + cobertura (com mínimo configurado)

O objetivo é garantir que:

o código continua consistente

os testes não quebram

a qualidade não depende de “rodar na minha máquina”

###✅ Soluções (explicação por desafio)
Desafio 1 – FizzBuzz
Problema: imprimir números de 1 a 100 substituindo:

múltiplos de 3 → Fizz

múltiplos de 5 → Buzz

múltiplos de 3 e 5 → FizzBuzz

Decisão de design:
Eu implemento a lógica em uma função que retorna uma lista de strings (fizzbuzz_lines()), pois:

fica fácil testar (não dependo de print)

main() apenas imprime

Complexidade:

Tempo: O(n)

Memória: O(n) (lista de saída)

Desafio 2 – Verificador de Palíndromo
Problema: retornar True se uma palavra é palíndromo.

Decisões “chatas” (e intencionais):

O enunciado fala em “palavra”, então considero a string inteira sem remover pontuação/espaços.

Uso casefold() para tornar a checagem case-insensitive ("Arara" → True).

Isso é um detalhe que melhora robustez sem alterar a essência do problema.

Validação:

se não for str, levanto TypeError

Complexidade:

Tempo: O(n)

Memória: O(n) (cópia/reverso)

Desafio 3 – Encontrar Duplicados
Problema: dado um array de inteiros, retornar um número duplicado.

Decisão de design:

Retorno o primeiro duplicado encontrado durante uma varredura.

Se não existir duplicado, retorno None.

Estrutura usada:

set para rastrear valores já vistos.

Validação:

input deve ser list[int] (se vier string ou lista com itens não inteiros → TypeError)

Complexidade:

Tempo: O(n)

Memória: O(n)

Desafio 4 – Validação de Parênteses
Problema: string com ()[]{} deve ser válida se:

fecha o mesmo tipo

fecha na ordem correta

Estrutura usada:

stack (lista como pilha)

Validação:

input deve ser str

caracteres fora do conjunto esperado tornam inválido (decisão explícita)

Complexidade:

Tempo: O(n)

Memória: O(n) no pior caso

Desafio 5 (Bônus) – Agrupamento de Transações
Problema: somar valores por categoria em uma lista de objetos.

Decisão de design:

Retorno dict[str, number] (no Python: dict[str, int/float])

Se algum item não tiver categoria ou valor → ValueError

Se estrutura for inválida → TypeError

Complexidade:

Tempo: O(n)

Memória: O(k), onde k é número de categorias

###✅ Observações finais
O projeto foi estruturado para ser executável por terceiros:

python -m dataviva_desafio

Há testes automatizados cobrindo:

comportamento esperado

bordas

entradas inválidas (TypeError/ValueError)

Qualidade verificada por CI, evitando “funciona só localmente”

###📌 Comandos rápidos
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pip install -e .
python -m ruff check .
python -m pytest -q
python -m pytest -q --cov=dataviva_desafio --cov-report=term-missing --cov-fail-under=95
python -m dataviva_desafio

---
