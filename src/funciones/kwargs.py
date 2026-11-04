# crear una funcion que me permita ssaber de una lista de ingredientes cual es el de mayor precio
# ejemplo:
#entada: ajo=2, papa=3, aceite=8
#salida: el ingrediente de mayor precio es aceite

def ingrediente_mayor_precio(**kwargs):
    ingrediente_caro = max(kwargs, key=kwargs.get)
    return ingrediente_caro
resultado = ingrediente_mayor_precio(ajo=2, papa=3, aceite=8)

print("El ingrediente de mayor precio es:", resultado)