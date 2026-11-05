# crear un programa que asigne un puntaje a cada letra del abcdario y
#  que su funcion me permita saber la letra que tenga menor puntaje mayor y 
# a media
def puntajes(*args):
    abcedario = "abcdefghijklmnopqrstuvwxyz"

    menor = min(args)
    mayor = max(args)
    medio = sorted(args)[len(args)//2]

    print("Menor puntaje:", abcedario[args.index(menor)], menor)
    print("Mayor puntaje:", abcedario[args.index(mayor)], mayor)
    print("Puntaje medio:", abcedario[args.index(medio)], medio)


puntajes(5, 8, 3, 9, 2, 7, 4, 6, 10, 1,
         12, 15, 11, 14, 13, 16, 18, 17, 20, 19,
         22, 21, 24, 23, 26, 25)