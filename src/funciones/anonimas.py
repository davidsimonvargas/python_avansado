# haciendo uso de lambda crear una funcion que me de un mensaje personalisado.

mensaje_personalisado = lambda nombre:f"¡Hola, {nombre}! Bienvenido/a. Esperamos que tengas un excelente día."
nombre= input("Ingresa tu nombre: ")
print(mensaje_personalisado(nombre))

# crear una funcion para calcular el area de un rectangulo siendo la formula la siguiente area=base*altura.

area = lambda Base, Altura: Base * Altura
Base = float(input("Ingrese la medida de la base del rectángulo: "))
Altura = float(input("Ingrese la medida de la altura del rectángulo: "))
resultado = area(Base, Altura)
print("El área del rectángulo es:", resultado)

# crear una funcion que verifique si un numeo es par o impar

verificacion = lambda numero: "Par" if numero %2==0 else "Impar"
numero = int(input("Ingrese un número para comparar: "))
print("El número ingresado es:", verificacion(numero))

# -----
es_par=lambda n: n%2==0
if es_par(4):
    print("es par")
else:
    print("es impar")