import re 
import ply.lex as lex

states = (
    ('moedas', 'exclusive'),
    ('selecionar', 'exclusive')
)

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'CODIGO',
    'SAIR',
    'VALOR_EURO',
    'VALOR_CENT',
    'FIM_MOEDA'
)

t_ANY_ignore = ' \t\n'

def t_LISTAR(t):
    r'LISTAR'
    return t

def t_MOEDA(t):
    r'MOEDA'
    t.lexer.begin('moedas')
    return t

def t_moedas_VALOR_EURO(t):
    r'\d+e'
    return t

def t_moedas_VALOR_CENT(t):
    r'\d+c'
    return t

def t_moedas_FIM_MOEDA(t):
    r'\.'
    t.lexer.begin('INITIAL')
    return t

t_moedas_ignore = ' \t\n,'

def t_SELECIONAR(t):
    r'SELECIONAR'
    t.lexer.begin('selecionar')
    return t

def t_selecionar_CODIGO(t):
    r'[A-Z]\d+'
    t.lexer.begin('INITIAL')
    return t

t_selecionar_ignore = ' \t\n'

def t_SAIR(t):
    r'SAIR'
    return t

def t_ANY_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
