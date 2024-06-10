import ts as TS
from expresiones import *
from instrucciones import *

output =""

def procesar_display(instr, ts):
    global output
    output +='>> '+ resolver_cadena(instr.cad, ts) +"\n"

def procesar_definition(instr, ts):
    defectValue = {
        'NUMBER': 0,
        'TEXT': "",
        'BINARY': False,
    }
    tipo_dato = instr.tipo_dato.upper()
    val = defectValue[tipo_dato]
    simbolo = TS.Simbolo(instr.id,tipo_dato,val) 
    ts.agregar(simbolo)

def procesar_asignation(instr, ts):   
   if isinstance(instr.expresion,ExpresionDobleComilla):
        val=resolver_cadena(instr.expresion,ts)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.TEXT, val)
   elif isinstance(instr.expresion, ExpresionBool):
        val = resolver_booleano(instr.expresion, ts) 
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BINARY, val)
   else:
        val = resolver_expresion_aritmetica(instr.expresion, ts)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMBER, val)
   ts.actualizar(simbolo)

def procesar_under(instr, ts):
    while  resolver_expresion_comparativa(instr.expcomparativa, ts):
       ts_local = TS.TablaDeSimbolos(ts.simbolos)
       procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_go_under(instr, ts):
    while resolver_expresion_comparativa(instr.expcomparativa, ts):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)
        if resolver_expresion_comparativa(instr.expcomparativa, ts):
            break;

def procesar_valid(instr, ts):
    val = resolver_expresion_comparativa(instr.expcomparativa, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)


def procesar_invalid(instr, ts):
    val = resolver_expresion_comparativa(instr.expcomparativa, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfVerdadero, ts_local)
    else:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfFalso, ts_local)

def procesar_repeat(instr, ts):
    while(resolver_expresion_comparativa(instr.expcomparativa, ts)):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local) 
        val=resolver_expresion_aritmetica(instr.expNumerica, ts)
        ts_local.actualizar(TS.Simbolo(instr.id, TS.TIPO_DATO.NUMBER, val))
        
def resolver_cadena(expCad, ts):
    global output
    if isinstance(expCad, ExpresionConcatenar):
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla):
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico):
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else:
     output+='Error: Expresión cadena no válida \n'

def resolver_booleano(exp_booleana, ts):
    return exp_booleana.val

def resolver_expresion_comparativa(expCom, ts):
    exp1 = resolver_expresion_aritmetica(expCom.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expCom.exp2, ts)
    if expCom.operador == OPERACION_COMPARATIVA.MAYOR_QUE: return exp1 > exp2
    if expCom.operador == OPERACION_COMPARATIVA.MENOR_QUE: return exp1 < exp2
    if expCom.operador == OPERACION_COMPARATIVA.IGUAL: return exp1 == exp2
    if expCom.operador == OPERACION_COMPARATIVA.DIFERENTE: return exp1 != exp2
    if expCom.operador == OPERACION_COMPARATIVA.MAYOR_IGUAL_QUE: return exp1 >= exp2
    if expCom.operador == OPERACION_COMPARATIVA.MENOR_IGUAL_QUE: return exp1 <= exp2

def resolver_expresion_aritmetica(expNum, ts):
    if isinstance(expNum, ExpresionBinaria):
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS: return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS: return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR: return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO: return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.MODULO: return exp1 % exp2
        if expNum.operador == OPERACION_ARITMETICA.POTENCIA: return exp1 ** exp2
    elif isinstance(expNum, ExpresionNegativo):
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero):
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador):
        return ts.obtener(expNum.id).valor

def procesar_callfunctie(instr, ts):
    ts_local = TS.TablaDeSimbolos(ts.simbolos)
    procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_instrucciones(instrucciones, ts):
    '''listado de instrucciones recolectadas'''
    global output
    try:
        for instr in instrucciones:
            if isinstance(instr,Display):
                procesar_display(instr, ts)
            elif isinstance(instr, Definition):
                procesar_definition(instr, ts)
            elif isinstance(instr, Asignation):
                procesar_asignation(instr, ts)
            elif isinstance(instr, Under):
                procesar_under(instr, ts)
            elif isinstance(instr, Valid):
                procesar_valid(instr, ts)
            elif isinstance(instr, Invalid):
                procesar_invalid(instr, ts)
            elif isinstance(instr, Repeat):
                procesar_repeat(instr, ts)
            elif isinstance(instr,Go_under):
                procesar_go_under(instr, ts)
            elif isinstance(instr,callFunctie):
                procesar_callfunctie(instr, ts)
            elif isinstance(instr,Functie):
                pass
            else:
                output+='Error: instrucción no válida \n'
    except:
        from ts import output as outputTs
        from gramatica import output as outputG
        output += outputTs + outputG+ "\n"
