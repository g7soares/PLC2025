from lex import lexer

token_atual = None

def erro_sintaxe(token):
    print("Erro de sintaxe: símbolo inesperado ->", token)

def consumir(esperado):
    """Avança o token se corresponder ao esperado."""
    global token_atual
    if token_atual and token_atual.type == esperado:
        token_atual = lexer.token()
    else:
        erro_sintaxe(token_atual)


'''
Expressao       >> Termo ExpressaoResto
ExpressaoResto  >> + Termo ExpressaoResto 
                | - Termo ExpressaoResto 
                | ε
Termo           >> Fator TermoResto
TermoResto      >> * Fator TermoResto 
                | / Fator TermoResto 
                | ε
Fator           >> NUMBER 
                | ( Expressao )
'''


def analisar_expressao():
    print("Derivando por: Expressao -> Termo ExpressaoResto")
    analisar_termo()
    analisar_expressao_resto()
    print("Reconheci: Expressao -> Termo ExpressaoResto")

def analisar_expressao_resto():
    global token_atual
    if token_atual and token_atual.type == 'ADD':
        print("Derivando por: ExpressaoResto -> + Termo ExpressaoResto")
        consumir('ADD')
        analisar_termo()
        analisar_expressao_resto()
        print("Reconheci: ExpressaoResto -> + Termo ExpressaoResto")
    elif token_atual and token_atual.type == 'SUB':
        print("Derivando por: ExpressaoResto -> - Termo ExpressaoResto")
        consumir('SUB')
        analisar_termo()
        analisar_expressao_resto()
        print("Reconheci: ExpressaoResto -> - Termo ExpressaoResto")
    else:
        print("Derivando por: ExpressaoResto -> ε (vazio)")

def analisar_termo():
    print("Derivando por: Termo -> Fator TermoResto")
    analisar_fator()
    analisar_termo_resto()
    print("Reconheci: Termo -> Fator TermoResto")

def analisar_termo_resto():
    global token_atual
    if token_atual and token_atual.type == 'TIMES':
        print("Derivando por: TermoResto -> * Fator TermoResto")
        consumir('TIMES')
        analisar_fator()
        analisar_termo_resto()
        print("Reconheci: TermoResto -> * Fator TermoResto")
    elif token_atual and token_atual.type == 'DIVIDE':
        print("Derivando por: TermoResto -> / Fator TermoResto")
        consumir('DIVIDE')
        analisar_fator()
        analisar_termo_resto()
        print("Reconheci: TermoResto -> / Fator TermoResto")
    else:
        print("Derivando por: TermoResto -Z ε (vazio)")

def analisar_fator():
    global token_atual
    if token_atual is None:
        erro_sintaxe(token_atual)
        return
    if token_atual.type == 'NUMBER':
        print("Derivando por: Fator -> NUMBER")
        consumir('NUMBER')
        print("Reconheci: Fator -> NUMBER")
    elif token_atual.type == 'LPAREN':
        print("Derivando por: Fator -> ( Expressao )")
        consumir('LPAREN')
        analisar_expressao()
        consumir('RPAREN')
        print("Reconheci: Fator -> ( Expressao )")
    else:
        erro_sintaxe(token_atual)

def analisar_codigo(fonte):
    global token_atual
    lexer.input(fonte)
    token_atual = lexer.token()
    analisar_expressao()
    print("Análise sintática terminada.")
