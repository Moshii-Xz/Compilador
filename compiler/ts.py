from enum import Enum

class TIPO_DATO(Enum) :
    NUMBER = 1
    BINARY = 2
    TEXT = 3

output = ""
class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor) :
        self.id = id
        self.tipo = tipo
        self.valor = valor

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        global output
        if not id in self.simbolos :
            output+='Error: variable ', id, ' no definida \n'
        return self.simbolos[id]

    def actualizar(self, simbolo) :
        global output
        if not simbolo.id in self.simbolos :
            output+='Error: variable ', simbolo.id, ' no definida. \n'
        else :
            self.simbolos[simbolo.id] = simbolo