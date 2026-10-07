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
