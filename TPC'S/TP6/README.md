# TP6 - Analisador Sintático de Expressões Aritméticas

## Objetivo
Implementar um analisador sintático descendente recursivo para expressões aritméticas.

## Estrutura

### lex.py - Analisador Léxico
Define os tokens da linguagem:
- `NUMBER`: números inteiros
- `ADD`, `SUB`: operadores de adição e subtração
- `TIMES`, `DIVIDE`: operadores de multiplicação e divisão
- `LPAREN`, `RPAREN`: parênteses

### ana.py - Analisador Sintático
Implementa um analisador descendente recursivo baseado na gramática:

```
Expressao       -> Termo ExpressaoResto
ExpressaoResto  -> + Termo ExpressaoResto 
                 | - Termo ExpressaoResto 
                 | ε
Termo           -> Fator TermoResto
TermoResto      -> * Fator TermoResto 
                 | / Fator TermoResto 
                 | ε
Fator           -> NUMBER 
                 | ( Expressao )
```

Funções principais:
- `analisar_expressao()`: analisa expressões
- `analisar_termo()`: analisa termos
- `analisar_fator()`: analisa fatores
- `consumir(token)`: consome tokens esperados
- `erro_sintaxe(token)`: reporta erros sintáticos

### main.py
Programa principal que recebe uma expressão aritmética do utilizador e executa a análise sintática.

## Execução
```bash
python main.py
```

Exemplo:
```
Introduza uma expressão aritmética: 2 + 3 * (4 - 1)
```

O programa apresenta as derivações e reconhecimentos de cada produção aplicada durante a análise.
