# FUNCION EN PYTHON
las funciones nos permiten ordenar mejor el codigo y reutilizar cuando sea necesario
```py
# ejemplo deseamos crear un programa python que nos pe4rmita sumar los numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
```

como hacemos reutilisable el ejercxicio anterior y mas lejilble.
para eso utilisamos funciones.
la caracteristica de una funcion en python es la siguiente:
1. debe comenzar xon la palabra reservada`def`
2. debe tener un nombre que de a entender que realizara la funcion,
3. debera tener parametros estos estaran encerrados en parentesis `()`.
   no todas las fumciones resibiran parametros aun asi debera tener los `()`
4. las funciones deberan retornar datos a travez de la palabra reservada `return`

```py
# crear un programa que me permita sumar dos numeros
def sumar(a:int,b:int):
    return a+b
print(sumar(78,56))
print(sumar(45,5))
```







## Conociendo mas sobre funciones

sobre los parametros/argumentos nominales es ampliamente usado para distintas configuraciones ya que se puede pasar solo los argumentos que se usaran y dejar los parametros por defecto si no se van a amortificar 
```py
# tenemos un programa que nos permite accceder a internet que tiene parametros por  defecto sin embargo si se actualiza uno de los accesos se podra modificar el valor.

## primer caso accesos por defecto

def config(user="admin", pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"
config()

## segundo caso el BSSID cambio por el de "laboratorio1"

 def config(user="admin", pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"
config(BSSID="laboratorio1")

## reyner desea conectardse al wifi de ana luz, pregunta como se llama tu wifi y cual es la contraseña, respuesta le dice el wifi es A56 y su contraseña es 12345678

def config(user="admin", pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"
config(BSSID="A56",pass="12345678")
 
```

### Conociendo *args y **kwargs (espaquetado y desempaquetado de argumentos pocisionales):

### desempaquetando argumentos pocisionales.

esta tecnica nos permite empaquetar nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar, imaginemos que nos piden una funcion para sumar n cantidad de numeros lqa solucion seria empaquetar los argumentos y luego desmpaquetar para ello en la definicion de la funcion dentro de los parametros debemos usar el operedor `*` delante del pararametro pocicional  esto ara que todos los argumentos se almacenen en una tupla (es una lista) esto nos permite recorrer dentro de sus elementos para poder desempaquetarlo y realisar las operaciones necesarias

```py
# deseamos crear una funcion que nos permite sumar n cantidad de numeros
# n es un numero varibale puede ser 3, 7, 8 ..... n

def suma(*arg):
    # *arg =(2,5,7,8,9)
    acumulado=()
    for i in arg:
        acumulado += 1
    return acumulado
print (suma(2,5,7,8,9))
```

### desempaquetando argumentos nominales:

 en ese caso como en el anterior utlisaramos el operador `*` lka casuistica es el mismo sin embargo para desmpaquetar argumentos nomianles usaremos `**` delante del nombre del parametro nominal a diferencia del anteriro esto se empaquetara en un diccionario (`{clave:valor}`)
 ```py
# debemos crear una funcion que me permita saber encontrar la persona con mayor calificacion:

def mejor_alumno(**kwargs):
    # este kwargs={clave:valor}
    nota_maxima =-1
    for alumno, nota in kwargs.items():
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_alumno = alumno
    return mejor_alumno
 mejor_alumno(noemi=20,eduardo=18,david=19)
 ```

 ## Funciones anonimas
 las funciones anonimas en python son llamadas `lambda` estas funciones tienen las siguientes propiedades:
 1. se escribe en una unica sentencia`(linea)`.
 2. no tiene nombre`(anonima)`.
 3. su cuerpo conlleva un `return` duplicito.
 4. puede recibir cualquier numero de parametro.
 
 la estructura pra definir una funcion `lambda` es la siguiente:
 1. escribir la palabra reservada `lambda`. 
 2. especificar la cantidad de parametros.
 3. indicar los datos de retorno
```py
lambda a,b: a+b 
```

> [!TIP] puesto que esta funcion es aninima para ejecutarla debemos almacenar la funcion en una variable

```py
lambda a,b: a+b 
suma (3+6)

```

## Documentacion
python nos permite documentar la funcion  con el objetivo de explicar mejor determinadas zonas de nuestro codigo para esto usamos una cadena de texto despues de la definicon de una funcion, a esta cadena de texto se le conoce como `docstring` y esta terminado por triples `"""`.
```py
def suma(a,b)
    """
    funcion para realisar la suma de 2 numeros
    """
## los docs streems tambien nos permite explicar los parametros que reciben y los datos de salida 
def resta(a,b)
"""
a= es un numero entero
b= a un numero entero
en ambos casos a,b no deben recibir valores menores a 0.
retornara un dato entero <int>y positivo
"""
return a-b

```

> [!WARING] en el proceso de documentacion tener en cuenta de incluir a lo menos lo siguiente: 
> 1. especificaiones y caracteristicas de los parametros incluyendo sus tipos. 
> 2. restriciiones de la funcion. 
> 3. el valor que retorna y sus caracteristicas.

## type-hints(anotacionesde tipo)
Nos permite indicar que tipo de datos tendra una variable, parametro y el valor de retorno de una funcion.
Para utilisarlos debemos de indicar el tipo de dato despues del separador `:`, en el caso del valor de retorno usaremos `->` luego el tipo de dato y finalmente el separador`:` que indica el inicio del bloque de codigo de la funcion.
Las `anotaciones de tipo` son una herramienta que nos permite complementar la documentacion de nuestro codigo
**tenemos los sigueintes**

+ **simple**

- int-> numeros enteros
- float-> numeros decimales
- bool -> datos boleanos,(verdad o falso)
- str -> datos de texto o cadena
- list -> listas`[]`
- tuple -> tuplas `()`
- dict -> diccionarios `{}`

+ **compuestos**

existen casos en los que necesitamos mas exclusividad en la *anotacion de tipos* ¿que ocurre si queremos indicar una *lista de cadenas* o un *conjunto de enteros*?
- list[str]-> lista de cadenasde texto
- list[int]-> lista de numeros enteros
- dic[str,float]-> diccionario donde las claves son cadenas de texto y los valores son flotantes/decimales

+ **multiples**
en el caso que queramos indicar de un  determinado parametro ouede ser de un `tipo o de otro` tenemos que especificarlo usando el operador `|`
- tuple|dict-> puede ser dato de tipo tupla o diccionario
- list[str|int]-> lista cuyos elementos pueden ser cadena de texto o enteros
- dict[str|float|int]-> diccionario cuya clave puede ser texto,decimnal o entero, y valor lo mismo.