# crear un programa que me permita desarrollar las 4 operaciones basicas (suma,resata,division,multiplicacion)

def operaciones(a,operacion,b):
    if operacion=='+':
        return a+b
    if operacion=='-':
        return a-b
    if operacion=='*':
        return a*b
    if operacion =='/':
        return a/b
a=float(input("primer_numero: ")) 
operacion = input("selecione la operacion(+ - * /):")
b=float(input("segundo_numero: ")) 
print("resultado: ", operaciones(a,operacion,b))