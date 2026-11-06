# en la siguiente funcion deberan escribir la documentacion segun la convencion para el docstring de funciones.

def area_rectangulo(b,h):
    """"calcula el area del rectangulo

    args:
 b= (int|float) este argumento sera la base del rectangulo
 h= (int|float) este argumento sera la altura del rectangulo

 reises:
 en los 2 casos b,h no deberian de recibir valores que sea menor al numero 0.

 returns:
 int|float: el resultado de la operacion b*h (base * altura).
 """
    return b*h

# funcion para hayar la potencia de un numero 
def potencia(n:int,p:int)->int:   
    """calcula la potencia de un numero
    
        Args:
            n (int): este es el numero base de la potencia
            p (int): esta es la potencia 
        Returns:
            int: el resultado de la operacion en la que n se multiplica la  
            cantidad de veces que p le indique (n**p)
    """ 
    resultado:int=1
    for _ in range(p):
        resultado*=n
        return resultado