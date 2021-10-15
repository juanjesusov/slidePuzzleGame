"""
    Nombre del Programa: Proyecto integrador: Slide Puzzle
    Descripción: ddddddddddddd ?
    Fecha: 19/10/2021 ?

    Juan Jesús Ortiz A01639936
        - llenadoManual
        - llenadoAutomatico
        - EstadoGanador
        - desplegarTablero
        - indiceFicha
        - hueco
        - indiceHueco
        - mover
        - main

    Ricardo López A01284902
        - llenadoManual
        - llenadoAutomatico
        - EstadoGanador
        - desplegarTablero
        - indiceFicha
        - main
"""

def llenadoManual(matriz):
    """
        Estandar de codificación:
            Nombre de Función: llenadoManual
            Descripción: Pide al usuario escribir 16 números entre 0 y 15 sin repetirse.
            Parámetros de entrada: matriz
            Parámetros de salida: matriz
        Autores: 
            Ricardo López A01284902
            Juan Jesús Ortiz A01639936
    """
    lista = []
    valoresValidos = ['1', '2','3', '4','5','6','7','8','9','10','11','12','13','14','15','0']

    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            
            validado = False
            num = input()
            
            while validado==False:
                while num not in valoresValidos:
                    print('\033[31m'+"ERROR: Solo puede ingresar números"+'\033[39m')
                    num = input()              
                num = int(num)
                if (num > 15) or (num < 0):
                    print('\033[31m'+"ERROR: Valor fuera de rango"+'\033[39m')
                    num = int(input())
                elif num in lista:
                    print('\033[31m'+"ERROR: No se puede repetir los números"+'\033[39m')
                    num = int(input())
                else:
                    validado = True

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
            Ricardo López A01284902
            Juan Jesús Ortiz A01639936
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
            Descripción: Revisa si la matriz esta en orden, y si lo está, regresa una variable bandera para felicitar al usuario.
            Parámetros de entrada: matriz
            Parámetros de salida: ganador
        Autores: 
            Ricardo López A01284902
            Juan Jesús Ortiz A01639936
    """
    matrizGanadora = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'']]
    ganador = False
    if matriz == matrizGanadora:
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
            Ricardo López A01284902
            Juan Jesús Ortiz A01639936
    """
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):    
            if matriz[i][j] == 0: 
                matriz[i][j] = str(matriz[i][j])
                matriz[i][j] = ''

            print('\033[33m'+"{}".format(matriz[i][j]), end="\t")

        print('\033[39m')
    
    #return matriz

def indiceFicha(ficha, matriz):
    """
        Estandar de codificación:
            Nombre de Función: indiceFicha
            Descripción: Se encarga de localizar el indice en el que se encuentra la ficha que el usuario quiere mover.
            Parámetros de entrada: ficha, matriz
            Parámetros de salida: indiceRen, indiceCol
        Autores: 
            Ricardo López A01284902
            Juan Jesús Ortiz A01639936
    """
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == ficha: 
                indiceRen = i
                indiceCol = j

    return indiceRen, indiceCol

def hueco(matriz, indiceRen, indiceCol):
    """
        Estandar de codificación:
            Nombre de Función: hueco
            Descripción: Se encarga de identificar si es que la ficha seleccionada por el usuario tiene la casilla vacía adyacente
                         a ella, tanto en lo horizontal, como en lo vertical.
            Parámetros de entrada: matriz, indiceRen, indiceCol
            Parámetros de salida: huecoAdyacente
        Autores: 
            Juan Jesús Ortiz A01639936
    """
    huecoAdyacente = False
    
    if indiceRen==0 or indiceRen==1 or indiceRen==2:
        if matriz[indiceRen+1][indiceCol]=='':
            huecoAdyacente = True
    
    if indiceRen==1 or indiceRen==2 or indiceRen==3:
        if matriz[indiceRen-1][indiceCol]=='':
            huecoAdyacente = True

    if indiceCol==0 or indiceCol==1 or indiceCol==2:
        if matriz[indiceRen][indiceCol+1]=='':
            huecoAdyacente = True
    
    if indiceCol==1 or indiceCol==2 or indiceCol==3:
        if matriz[indiceRen][indiceCol-1]=='':
            huecoAdyacente = True

    """
        if indiceRen==0:
            #Revisar abajo
            if matriz[indiceRen+1][indiceCol]=='':
                huecoAdyacente = True
        
        if indiceRen==1 or indiceRen==2:
            #Revisar arriba y abajo
            if matriz[indiceRen+1][indiceCol]=='' or matriz[indiceRen-1][indiceCol]=='':
                huecoAdyacente = True

        if indiceRen==3:
            #Revisar arriba
            if matriz[indiceRen-1][indiceCol]=='':
                huecoAdyacente = True

        if indiceCol==0:
            #Revisar derecha
            if matriz[indiceRen][indiceCol+1]=='':
                huecoAdyacente = True
        
        if indiceCol==1 or indiceCol==2:
            #Revisar derecha y izquierda
            if matriz[indiceRen][indiceCol+1]=='' or matriz[indiceRen][indiceCol-1]=='':
                huecoAdyacente = True

        if indiceCol==3:
            #Revisar izquierda    
            if matriz[indiceRen][indiceCol-1]=='':
                huecoAdyacente = True
    """

    return huecoAdyacente

def indiceHueco(matriz):
    """
        Estandar de codificación:
            Nombre de Función: indiceHueco
            Descripción: Se encarga de regresar el renglon y la columna en donde se encuentra el hueco.
            Parámetros de entrada: matriz
            Parámetros de salida: indiceHuecoRen, indiceHuecoCol
        Autores: 
            Juan Jesús Ortiz A01639936
    """
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == '': 
                indiceHuecoRen = i
                indiceHuecoCol = j

    return indiceHuecoRen, indiceHuecoCol

def mover(matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol):
    """
        Estandar de codificación:
            Nombre de Función: hueco
            Descripción: Sutituye los valores del hueco y de la ficha seleccionada para simular el hecho de que se movieron las fichas.
            Parámetros de entrada: matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol
            Parámetros de salida: matriz
        Autores: 
            Juan Jesús Ortiz A01639936
    """    
    matriz[indiceHuecoRen][indiceHuecoCol] = matriz[indiceRen][indiceCol]
    matriz[indiceRen][indiceCol] = 0
                
    return matriz

def main(matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol):
    """
        Estandar de codificación:
            Nombre de Función: main
            Descripción: Se encarga de solicitar al usuario si es que quiere llenar su tablero el mismo, o que se haga automatico,
                         además se encarga de llamar a otras funciones según sea pertinente.
            Parámetros de entrada: matriz
            Parámetros de salida: -
        Autores: 
            Ricardo López A01284902
            Juan Jesús Ortiz A01639936
    """

    movimientos = 0
    nombre = input("\nIngresa tu nombre: ")
    decision = input("\n¿Desea llenar la tabla manualmente o que el programa lo haga automatico por usted? (m/a): ").lower()
    
    while decision!='m' and decision!='a':
        print('\033[31m'+"\nERROR: El valor que acaba de ingresar no es valido"+'\033[39m')
        decision = input("\n¿Desea llenar la tabla manualmente o que el programa lo haga automatico por usted? (m/a): ").lower()

    if decision=='m':
        print('\033[36m'+"\nPara indicar el espacio vacio ingrese cero"+'\033[39m')
        matriz = llenadoManual(matriz)
        print("")
    else:
        llenadoAutomatico(matriz)

    desplegarTablero(matriz)
    
    ganador = estadoGanador(matriz)
    
    if ganador==False:
        print('\033[36m'+"\nLe recordamos que en cualquier momento del juego puede decidir terminar la partida escribiendo \"no\" en la consola."+'\033[39m')

    while ganador!=True:
        ficha = input("\n¿Cuál ficha quiere mover?: ")
        if ficha=='no':
            print('\033[34m'+"\nPartida terminada.\n"+'\033[39m')
            exit()
        else:
            ficha = int(ficha)
        
        while ficha<1 or ficha>15:
            print('\033[31m'+"ERROR: Ficha invalida"+'\033[39m')
            ficha = input("\n¿Cuál ficha quiere mover?: ")
            if ficha=='no':
                print('\033[34m'+"\nPartida terminada.\n"+'\033[39m')
                exit()
            else:
                ficha = int(ficha)

        movimientos+=1
        indiceRen, indiceCol = indiceFicha(ficha, matriz)
        huecoAdyacente = hueco(matriz, indiceRen, indiceCol)
        indiceHuecoRen, indiceHuecoCol = indiceHueco(matriz)
        
        if huecoAdyacente == True:
            matriz = mover(matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol)
            desplegarTablero(matriz)
        else:
            desplegarTablero(matriz)
            print('\033[31m'+"\nERROR: La ficha que ha seleccionado no puede moverse. El tablero no ha registrado cambios"+'\033[39m')
        
        ganador = estadoGanador(matriz)
        
    print('\033[32m'+"\n¡Felicidades {}, haz ganado!\nHas utilizado {} movimientos.".format(nombre, movimientos))
    print('\033[39m')

matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
indiceHuecoRen = 0
indiceHuecoCol = 0
indiceRen = 0
indiceCol = 0
main(matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol)