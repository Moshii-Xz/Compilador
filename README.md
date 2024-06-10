# Manera de usar 
**`Ejecutar App.py`
---
# Desglose de Sintaxis y Componentes 

Claro, desglosar la sintaxis de un lenguaje de programación es fundamental para entender cómo funciona y cómo usarlo eficazmente. Vamos a revisar el ejemplo que has proporcionado y desglosar cada componente y función del lenguaje paso a paso.

## Sintaxis y Componentes del Lenguaje

El ejemplo dado parece tener un lenguaje de programación propio con una sintaxis específica para definir variables, estructuras de control y operaciones básicas. Aquí se desglosan los elementos clave del lenguaje:

### 1. Declaración de Variables

- **`number a;`**: Declara una variable `a` de tipo `number` (número).
- **`text n;`**: Declara una variable `n` de tipo `text` (texto).

### 2. Asignación de Valores

- **`a~2;`**: Asigna el valor `2` a la variable `a`.
- **`n~"hola mundo";`**: Asigna la cadena de texto `"hola mundo"` a la variable `n`.

### 3. Funciones de Visualización

- **`display(n);`**: Muestra el valor de `n` en la consola o en la salida.
- **`display("Tablas de" & " multiplicar");`**: Muestra la cadena concatenada `"Tablas de multiplicar"` en la consola.

### 4. Estructuras de Control

- **`go { ... } under a<10 ;`**: Similar a un bucle `do-while`. Ejecuta el bloque de código dentro de `go { ... }` mientras la condición `a < 10` sea verdadera.
- **`under:a<4+c{ ... }`**: Similar a un bucle `while`. Ejecuta el bloque de código mientras `a` sea menor que `4 + c`.

### 5. Estructuras Condicionales

- **`valid:a>10{ ... }`**: Similar a un `if`. Ejecuta el bloque si la condición `a > 10` es verdadera.
- **`invalid{ ... }`**: Similar a un `else`. Ejecuta el bloque si la condición anterior no es verdadera.

### 6. Comentarios

- **`#`**: Se utiliza para escribir comentarios. El texto después de `#` hasta el final de la línea no se ejecuta.

### 7. Concatenación de Textos

- **`&`**: Operador de concatenación. Combina dos cadenas de texto.

### 8. Operaciones Aritméticas

- **`+`**: Suma.
- **`-`**: Resta.
- **`*`**: Multiplicación.
- **`/`**: División.

## Desglose y Ejemplo de Cada Componente

### Declaración de Variables y Asignación de Valores

```plaintext
number a;
text n;
n~"hola mundo";
display(n);
a~2;
```

**Descripción**:
- Declara una variable `a` de tipo número.
- Declara una variable `n` de tipo texto y le asigna la cadena `"hola mundo"`.
- Muestra el valor de `n` que es `"hola mundo"`.
- Asigna el valor `2` a `a`.

**Ejemplo**:
```plaintext
number x;
text greeting;
greeting~"Hello, World!";
display(greeting);
x~10;
```

...

---
