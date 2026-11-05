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

```

> [!TIP] puesto que esta funcion es aninima para ejecutarla debemos almacenar la funcion en una variable

```py

```
