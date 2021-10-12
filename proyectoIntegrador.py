#PENDIENTES
#Avanzar en la función que mueve la ficha si hay hueco, arriba/abajo, ó izquierda/derecha

#No transformar el 0 a string
#validar fichas ingresadas

def llenadoManual(matriz):
    """
        Estandar de codificación:
            Nombre de Función: llenadoManual
            Descripción: Pide al usuario escribir 16 números entre 0 y 15 sin repetirse.
            Parámetros de entrada: matriz
            Parámetros de salida: matriz
        Autores: 
            Ricardo López
            Juan Jesús Ortiz
    """
    lista = []
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            num = int(input())
            
            while ((num > 15) or (num < 0)) or (num in lista):
                if (num > 15) or (num < 0):
                    print("ERROR: Valor fuera de rango")
                    num = int(input())          
                if num in lista:
                    print("ERROR: No se puede repetir los números")
                    num = int(input())

            lista.append(num)
            matriz[i][j] = num

    return matriz

def llenadoAutomatico(matriz):
    """
        Estandar de codificación:
            Nombre de Función: llenadoAutomatico
            Descripción: Llena la matriz con números aleatorios entre 0 y 15 sin repetirse.
            Parámetros de entrada: matriz
            Parámetros de salida: matriz
        Autores: 
            Ricardo López
            Juan Jesús Ortiz
    """
    from random import randint

    lista=[]
    for r in range(len(matriz)):
        for c in range(len(matriz[r])):
            numRand = randint(0, 15)
            
            while numRand in lista:
                numRand = randint(0, 15)
            
            lista.append(numRand)
            matriz[r][c] = numRand
    
    return matriz

def estadoGanador(matriz):
    """
        Estandar de codificación:
            Nombre de Función: estadoGanador
            Descripción: Revisa si la matriz esta en orden, y si lo está, felicita al usuario.
            Parámetros de entrada: matriz
            Parámetros de salida: ganador
        Autores: 
            Ricardo López
            Juan Jesús Ortiz
    """
    #¿La matriz ganadora donde tiene que tener al 0?
    matrizGanadora1 = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    matrizGanadora2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    ganador = False
    if matriz == matrizGanadora1 or matriz == matrizGanadora2:
        ganador = True

    return ganador

def desplegarTablero(matriz):
    """
        Estandar de codificación:
            Nombre de Función: desplegarTablero
            Descripción: Imprime el tablero en forma de tabla.
            Parámetros de entrada: matriz
            Parámetros de salida: matriz
        Autores: 
            Ricardo López
            Juan Jesús Ortiz
    """
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):    
            if matriz[i][j] == 0: 
                matriz[i][j] = str(matriz[i][j])
                matriz[i][j] = ''

            print(matriz[i][j], end="\t")

        print()
    
    return matriz

def indiceFicha(ficha, matriz):
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == ficha: 
                indiceRen = i
                indiceCol = j

    return indiceRen, indiceCol

def main(matriz, indiceRen, indiceCol):
    """
        Estandar de codificación:
            Nombre de Función: main
            Descripción: Se encarga de solicitar al usuario si es que quiere llenar su tablero el mismo, o que se haga automatico,
                         además se encarga de llamar a otras funciones según sea pertinente.
            Parámetros de entrada: matriz
            Parámetros de salida: -
        Autores: 
            Ricardo López
            Juan Jesús Ortiz
    """
    nombre = input("Ingresa tu nombre: ")
    decision = input("\n¿Desea llenar la tabla manualmente o que el programa lo haga automatico por usted? (m/a): ")
    if decision=='m':
        print("\nPara indicar el espacio vacio ingrese cero")
        matriz = llenadoManual(matriz)
    else:
        llenadoAutomatico(matriz)

    ganador = estadoGanador(matriz)

    desplegarTablero(matriz)
    
    while ganador!=True:
        ficha = int(input("¿Cuál ficha quiere mover?: "))
        while ficha<1 and ficha>15:
            print("Esa ficha es invalida")
            ficha = int(input("¿Cuál ficha quiere mover?: "))
        indiceRen, indiceCol = indiceFicha(ficha, matriz)
        print("{},{}".format(indiceRen, indiceCol))
        
    print("¡Felicidades {}, haz ganado!".format(nombre))

matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
indiceRen = 0
indiceCol = 0
main(matriz, indiceRen, indiceCol)