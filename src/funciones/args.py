# ejercicio usando la tecnica *args crear un afuncion que me permita identificar numeros pares de n cantidad de numeros pasados por argumento la funcion debera retornar una lista con los numeros pares identificados.

def identificar_pares(*args)->list[int]:
    pares = []
    for numero in args:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
resultado = identificar_pares(10, 15, 20, 7, 8, 11, 24, 30)

print("Los números pares son:", resultado)
