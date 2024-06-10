class Instruccion:
    '''This is an abstract class'''


class Display(Instruccion):
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self, cad):
        self.cad = cad


class Under(Instruccion):
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expcomparativa, instrucciones=[]):
        self.expcomparativa = expcomparativa
        self.instrucciones = instrucciones


class Definition(Instruccion):
    '''
        Esta clase representa la instrucción de definición de variables.
        Recibe como parámetro el tipo de datos y nombre del identificador a definir 
    '''

    def __init__(self,tipo_dato,id):
        self.tipo_dato = tipo_dato
        self.id = id
    
class Asignation(Instruccion):
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''

    def __init__(self, id, expresion):
        self.id = id
        self.expresion = expresion

class Valid(Instruccion):
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expcomparativa, instrucciones=[]):
        self.expcomparativa = expcomparativa
        self.instrucciones = instrucciones


class Invalid(Instruccion):
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expcomparativa, instrIfVerdadero=[], instrIfFalso=[]):
        self.expcomparativa = expcomparativa
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso


class Repeat(Instruccion):
    '''
           Esta clase representa la instrucción for.
           La instrucción repeat recibe como parámetro el id de una variable, una expresión comparativa, una numerica  y la lista
           de instrucciones a ejecutar.
     '''

    def __init__(self, id, expcomparativa, expNumerica, instrucciones=[]):
        self.id = id
        self.expcomparativa = expcomparativa
        self.expNumerica = expNumerica
        self.instrucciones = instrucciones

class Go_under(Instruccion):
    '''
             Esta clase representa la instrucción do while.
             La instrucción go under  recibe como parámetro una expresión comparativa, una numerica  y la lista
             de instrucciones a ejecutar.
    '''

    def __init__(self,expcomparativa, instrucciones=[]):
        self.expcomparativa = expcomparativa
        self.instrucciones = instrucciones

class Functie(Instruccion):
    '''
             Esta clase representa la una funcion
             La instrucción functie  recibe como parámetro el id de la funcion, paramtros y la lista
             de instrucciones a ejecutar.
    '''
    def __init__(self,id,parameters,instrucciones=[]):
        self.id = id
        self.parameters = parameters
        self.instrucciones = instrucciones

class callFunctie(Functie,Instruccion):
    '''
        Esta clase representa la llamada a una funcion
        La instrucción functie  recibe como parámetro el id de la funcion, paramtros y la lista
        de instrucciones a ejecutar.
    '''
    def __init__(self,id,parameters,instrucciones=[]):
      self.id = id
      self.parameters = parameters
      self.instrucciones = instrucciones