import ply.lex as lex
import ply.yacc as yacc

#===================================
#========= REG EXPRESSIONS =========
#===================================

tokens = [
    'INT',
    'PLUS',
    'TIMES',
    'LPARENT',
    'RPARENT'
]

t_ignore = ' \t\n'

def t_PLUS(t):
    r'\+'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value) #  token começa como string por padrao
    return t

def t_LPARENT(t):
    r'\('
    return t

def t_RPARENT(t):
    r'\)'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])

def tokenize(lexer:lex):
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

#===================================
#======== ATTRIBUTE GRAMMAR ========
#===================================

def p_expression_plus_term(p):
    """
    expression : expression PLUS term
    """
    p[0] = p[1] + p[3]

def p_expression_term(p):
    """
    expression : term
    """
    p[0] = p[1]

def p_term_times_factor(p):
    """
    term : term TIMES factor
    """
    p[0] = p[1] * p[3]

def p_term_factor(p):
    """
    term : factor
    """
    p[0] = p[1]

def p_factor_expression(p):
    """
    factor : LPARENT expression RPARENT
    """
    p[0] = p[2]

def p_factor_int(p):
    """
    factor : INT
    """
    p[0] = p[1]

def p_error(p):
    print("Syntax error in '%s'" % p.value)

lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        inp = input('Soma ou multiplicacao: ')
    except EOFError:
        break
    if not inp: continue
    result = parser.parse(inp)
    print(result)