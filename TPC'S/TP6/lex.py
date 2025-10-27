import ply.lex as lex

tokens = ('NUMBER', 'ADD', 'SUB', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')

t_ADD     = r'\+'
t_SUB     = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_NUMBER = r'\d+'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print('Símbolo inválido:', t.value[0], 'na linha', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()