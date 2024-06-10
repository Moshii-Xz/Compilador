
output=""
reservadas = {
    'number':'NUMBER',        # tipo de dato numerico
    'text':'TEXT',            # tipo de dato cadena 
    'binary':'BINARY',        # tipo de dato booleano
    'true':'TRUE',
    'false':'FALSE',
    'display':'DISPLAY',      # escibir
    'under':'UNDER',          # condicional mientra que
    'valid': 'VALID',         # condicional si
    'invalid':'INVALID',      # condicional si no
    'repeat':'REPEAT',        # condicional for
    'in':'IN',                # propio del for
    'go':'GO',                # condicional do-while
                              # declaracion funciones
}

tokens = [
             'PTCOMA',
             'DUPOINT',
             'LLAVIZQ',
             'LLAVDER',
             'PARIZQ',
             'PARDER',
             'IGUAL',
             'MAS',
             'MENOS',
             'POR',
             'DIVIDIDO',
             'POTENCIA',
             'CONCAT',
             'MAYIGU',
             'MENIGU',
             'MENQUE',
             'MAYQUE',
             'IGUALQUE',
             'NIGUALQUE',
             'DECIMAL',
             'ENTERO',
             'CADENA',
             'ID',
             'MODULO',
         ] + list(reservadas.values())

# Tokens
t_PTCOMA=r';'
t_DUPOINT = r':'
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'~'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_POTENCIA = r'\^'
t_CONCAT = r'&'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_MAYIGU= r'>~'
t_MENIGU=r'<~'
t_IGUALQUE = r'~~'
t_NIGUALQUE = r'!~'
t_MODULO = r'%'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        output+=("Float value too large %d \n", t.value)
        print(output)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        output += "Integer value too large %d \n" % t.value
        print(output)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] 
    return t

# Comentario de múltiples líneas ---> <---
def t_COMENTARIO_MULTILINEA(t):
    r'--->(.|\n)*?---'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple #  ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    global output
    output += "caracter ilegal '%s' linea %s \n" % (t.value[0], t.lineno)
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left', 'CONCAT'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('left', 'POTENCIA', 'MODULO'),
    ('right', 'UMENOS'),
)

# Definición de la gramática

from expresiones import *
from instrucciones import *

def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion      : display_instr
                        | definicion_instr
                        | asignacion_instr
                        | under_instr
                        | valid_instr
                        | invalid_instr
                        | repeat_instr
                        | go_under_instr '''
    t[0] = t[1]

def p_instruccion_display(t):
    'display_instr     :  DISPLAY PARIZQ expresion_cadena PARDER PTCOMA'
    t[0] = Display(t[3])

def p_tipo_dato(t):
    '''tipo_dato : NUMBER
                 | TEXT
                 | BINARY'''
    t[0] = t[1]

def p_instruccion_definicion(t):  
    '''definicion_instr : tipo_dato ID PTCOMA '''
    t[0] = Definition(t[1], t[2])

def p_asignacion_instr(t):
    '''asignacion_instr   :  ID IGUAL expresion_numerica PTCOMA
                          |  ID IGUAL expresion_cadena   PTCOMA 
                          |  ID IGUAL expresion_booleana PTCOMA'''
    t[0] = Asignation(t[1], t[3])
   
def p_under_instr(t):
    'under_instr     : UNDER DUPOINT  expresion_comparativa  LLAVIZQ instrucciones LLAVDER'
    t[0] = Under(t[3], t[5])

def p_go_under_instr(t):
    'go_under_instr     : GO LLAVIZQ  instrucciones  LLAVDER UNDER  expresion_comparativa PTCOMA '
    t[0] = Go_under(t[6], t[3])

def p_valid_instr(t):
    'valid_instr  : VALID DUPOINT expresion_comparativa  LLAVIZQ instrucciones LLAVDER'
    t[0] = Valid(t[3], t[5])

def p_invalid_instr(t):
    'invalid_instr      : VALID DUPOINT expresion_comparativa  LLAVIZQ instrucciones LLAVDER INVALID LLAVIZQ instrucciones LLAVDER'
    t[0] = Invalid(t[3], t[5], t[9])

def p_repeat_instr(t):
    'repeat_instr     : REPEAT DUPOINT ID PTCOMA expresion_comparativa IN expresion_numerica LLAVIZQ instrucciones LLAVDER '
    t[0] = Repeat(t[3], t[5], t[7],t[9])

def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                          | expresion_numerica MENOS expresion_numerica
                          | expresion_numerica POR expresion_numerica
                          | expresion_numerica DIVIDIDO expresion_numerica
                          | expresion_numerica MODULO expresion_numerica
                          | expresion_numerica POTENCIA expresion_numerica '''
    if t[2] == '+':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MODULO)
    elif t[2] == '^':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POTENCIA)

def p_expresion_unaria(t):
    'expresion_numerica : MENOS expresion_numerica %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])


def p_expresion_agrupacion(t):
    'expresion_numerica : PARIZQ expresion_numerica PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion_numerica : ENTERO
                          | DECIMAL'''
    t[0] = ExpresionNumero(t[1])

def p_expresion_id(t):
    'expresion_numerica   : ID'
    t[0] = ExpresionIdentificador(t[1])

def p_expresion_concatenacion(t):
    'expresion_cadena     : expresion_cadena CONCAT expresion_cadena'
    t[0] = ExpresionConcatenar(t[1], t[3])

def p_expresion_cadena(t):
    'expresion_cadena     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])

def p_expresion_cadena_numerico(t):
    'expresion_cadena     : expresion_numerica'
    t[0] = ExpresionCadenaNumerico(t[1])

def p_expresion_booleana(t):
    '''expresion_booleana : TRUE
                          | FALSE'''
    t[0] = ExpresionBool(t[1])

def p_expresion_comparativa(t):
    '''expresion_comparativa : expresion_numerica MAYQUE expresion_numerica
                             | expresion_numerica MENQUE expresion_numerica
                             | expresion_numerica IGUALQUE expresion_numerica
                             | expresion_numerica MAYIGU expresion_numerica
                             | expresion_numerica MENIGU expresion_numerica
                             | expresion_numerica NIGUALQUE expresion_numerica'''
    if t[2] == '>':
         t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.MAYOR_QUE)
    elif t[2] == '<':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.MENOR_QUE)
    elif t[2] == '~~':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.IGUAL)
    elif t[2] == '!~':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.DIFERENTE)
    elif t[2] == '>~':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.MAYOR_IGUAL_QUE)
    elif t[2] == '<~':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.MENOR_IGUAL_QUE)

def p_error(t):
    global output
    output = "Error sintactico en '%s' linea %s" % (t.value, t.lineno)
    t.lexer.skip(1)


import ply.yacc as yacc

parser = yacc.yacc()

def parse(input):
    return parser.parse(input)
