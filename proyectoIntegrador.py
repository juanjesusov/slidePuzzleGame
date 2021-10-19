# INSTRUCCIONES PREVIAS A LA EJECUCIÓN DEL PROGRAMA:
    # Es necesario instalar la librería "tabulate".
    # Para esto se tendrá que que abrir el cmd desde el buscador de su sistema y escribir "pip install tabulate".

    # SI NO TIENE LOS PREREQUISITOS INSTALADOS PARA QUE ESTO FUNCIONE REVISE LO SIGUIENTE:
        # Tiene que abrir el cmd y asegurarse de que el instalador "pip" de python este descargado.
        # En caso de no ser así, asegurarse de tener instalado "python" en su sistema.
        # Si la variable "pip" sigue sin funcionar en el cmd una vez que se haya reiniciado, haga lo siguiente:
        # Escriba "variable" desde el buscador de su sistema y haga click en "Editar las variables de entorno del sistema".
        # Despues haga click en "Variables de entorno..." y luego seleccione "Path" en la sección de "Variables del sistema" y haga click a "Editar..."
        # Aquí es donde se van a colocar las librerías que ocupamos para que este procedimiento funcione.
        # Ahora abra la ubicacion del archivo de la opción que incluya "IDLE" cuando escriba "python" en el buscador de su sistema.
        # Una vez abierto, de click derecho y haga click en "Propiedades" y después en "Abrir ubicación".
        # Haga click en la parte superior donde indica la ubicación del archivo y cópielo y péguelo en la seccíon de "Variables del entorno" despues de dar click a "Nuevo", y luego "Aceptar".
        # Ahora se debe de repetir la anterior acción pero con la ubicación del archivo "Scripts" que se encuentra en la misma carpeta de antes.
        # Haga click en "Aceptar" en todas las pestañas que queden restantes y, hecho esto, puede cerrar todo lo que tenga abierto.
        # Habra el cmd de nuevo e intente de nuevo instalar la librería escribiendo "pip install tabulate".
        # Con esto, el proceso de la instalación de los prerequisitos se habrá finalizado.

"""
    Nombre del Programa: Proyecto integrador: Slide Puzzle
    Descripción:    Es un programa que simula ser un juego en el que hay un tablero de 4x4 con números de 1 al 15
                    y con un espacio vacío para que las piezas se puedan cambiar de lugar según lo desee el jugador. El 
                    jugador al empezar el juego se le pregunta si desea que los números sean acomodados de manera
                    automática y aleatoria o manualmente por el mismo jugador. El programa está preparado para
                    cualquier caso o situación que pueda suceder por los ingresos de datos del jugador, lo que hace que el juego
                    pueda continuar fluidamente después de que se le advierte al jugador si es que ha cometido algún
                    error. El juego termina, felicitando al jugador, cuando se logra acomodar los números por orden de 
                    mayor a menor y con el espacio vacío al final en la esquina inferior a la derecha o incluso, una vez comenzado 
                    el juego y se le pida al jugador mover las fichas, el jugador tendrá la libertad de terminar el juego a pesar de que 
                    no se haya ordenado completamente el tablero en cualquier momento que desee, solo tiene que escribir 'no' y el juego se finalizará.
    Fecha: 19/10/2021 

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

# Estos son los modificadores del color para el texto impreso en el programa:
"""
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m
"""

"""
    Estándar de codificación:
        Nombre de Función: llenadoManual
        Descripción: Pide al usuario escribir 16 números entre 0 y 15 sin repetirse.
        Parámetros de entrada: matriz, valoresValidos
        Parámetros de salida: matriz
    Autores: 
        Ricardo López A01284902
        Juan Jesús Ortiz A01639936
"""
def llenadoManual(matriz, valoresValidos):
    lista = []

    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            num = input()
            
            while True: #Este ciclo siempre será ejecutado hasta que la entrada sea válida
                while (num not in valoresValidos) or (int(num) in lista):
                    if num not in valoresValidos:
                        print('\033[31m'+"ERROR: Solo puede ingresar números enteros entre el 0 y 15"+'\033[39m')
                        num = input()
                        continue #El continue sirve para que apesar de que se valide la primer condición cuando vuelva a leer un nuevo valor pase por las dos condiciones

                    if int(num) in lista:
                        print('\033[31m'+"ERROR: No se puede repetir los números"+'\033[39m')
                        num = input()
                
                lista.append(int(num))
                break
            
            num = int(num)
            matriz[i][j] = num
            
    return matriz

"""
    Estándar de codificación:
        Nombre de Función: llenadoAutomatico
        Descripción: Llena la matriz con números aleatorios entre 0 y 15 sin repetirse.
        Parámetros de entrada: matriz
        Parámetros de salida: matriz
    Autores: 
        Ricardo López A01284902
        Juan Jesús Ortiz A01639936
"""
def llenadoAutomatico(matriz):
    from random import randint

    lista=[]
    for r in range(len(matriz)):
        for c in range(len(matriz[r])):
            numRand = randint(0, 15) 
            
            while numRand in lista: #Hace que no se puedan repetir valores aleatorios dentro de la lista de valores
                numRand = randint(0, 15)
            
            lista.append(numRand)
            matriz[r][c] = numRand
    
    return matriz

"""
    Estándar de codificación:
        Nombre de Función: estadoGanador
        Descripción: Revisa si la matriz está en orden, y si lo está, regresa una variable bandera para felicitar al usuario.
        Parámetros de entrada: matriz
        Parámetros de salida: ganador
    Autores: 
        Ricardo López A01284902
        Juan Jesús Ortiz A01639936
"""
def estadoGanador(matriz):
    matrizGanadora = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'']]
    ganador = False
    
    if matriz == matrizGanadora: #Se compara la matriz actual de la partida con la versión correcta/ganadora de ella
        ganador = True

    return ganador

"""
    Estándar de codificación:
        Nombre de Función: desplegarTablero
        Descripción: Imprime el tablero en forma de tabla.
        Parámetros de entrada: matriz
        Parámetros de salida: -
    Autores: 
        Ricardo López A01284902
        Juan Jesús Ortiz A01639936
"""
def desplegarTablero(matriz):
    from tabulate import tabulate

    for i in range (len(matriz)):
        for j in range(len(matriz[i])):    
            if matriz[i][j] == 0: #Este condicional se encarga de cambiar el numero cero de la matriz, por un espacio vacio para que sea leída con mayor intuitividad
                matriz[i][j] = str(matriz[i][j])
                matriz[i][j] = ''

    print('\033[33m'+ tabulate(matriz,tablefmt='fancy_grid') +'\033[39m') #La función tabulate se encarga de imprimir las lineas separadoras del tablero, el primer parámetro es la matriz del tablero y el segundo el tipo de lineas que imprimirá

"""
    Estándar de codificación:
        Nombre de Función: indiceFicha
        Descripción: Se encarga de localizar el índice en el que se encuentra la ficha que el usuario quiere mover.
        Parámetros de entrada: ficha, matriz
        Parámetros de salida: indiceRen, indiceCol
    Autores: 
        Ricardo López A01284902
        Juan Jesús Ortiz A01639936
"""
def indiceFicha(ficha, matriz):
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == ficha: #Nos da los indices de la ficha que seleccionó el usuario
                indiceRen = i
                indiceCol = j

    return indiceRen, indiceCol

"""
    Estándar de codificación:
        Nombre de Función: hueco
        Descripción: Se encarga de identificar si es que la ficha seleccionada por el usuario tiene la casilla vacía adyacente
                        a ella, tanto en lo horizontal, como en lo vertical.
        Parámetros de entrada: matriz, indiceRen, indiceCol
        Parámetros de salida: huecoAdyacente
    Autores: 
        Juan Jesús Ortiz A01639936
"""
def hueco(matriz, indiceRen, indiceCol):
    huecoAdyacente = False
    
    if indiceRen==0 or indiceRen==1 or indiceRen==2: #Se encarga de identificar si es que el hueco del tablero se ubica a la derecha de la ficha ingresda
        if matriz[indiceRen+1][indiceCol]=='':
            huecoAdyacente = True
    
    if indiceRen==1 or indiceRen==2 or indiceRen==3: #Se encarga de identificar si es que el hueco del tablero se ubica a la izquierda de la ficha ingresda
        if matriz[indiceRen-1][indiceCol]=='':
            huecoAdyacente = True

    if indiceCol==0 or indiceCol==1 or indiceCol==2: #Se encarga de identificar si es que el hueco del tablero se ubica arriba de la ficha ingresda
        if matriz[indiceRen][indiceCol+1]=='':
            huecoAdyacente = True
    
    if indiceCol==1 or indiceCol==2 or indiceCol==3: #Se encarga de identificar si es que el hueco del tablero se ubica abajo de la ficha ingresda
        if matriz[indiceRen][indiceCol-1]=='':
            huecoAdyacente = True

    return huecoAdyacente

"""
    Estándar de codificación:
        Nombre de Función: indiceHueco
        Descripción: Se encarga de regresar el renglón y la columna en donde se encuentra el hueco.
        Parámetros de entrada: matriz
        Parámetros de salida: indiceHuecoRen, indiceHuecoCol
    Autores: 
        Juan Jesús Ortiz A01639936
"""
def indiceHueco(matriz):
    for i in range (len(matriz)):
        for j in range(len(matriz[i])): 
            if matriz[i][j] == '': #Nos regresa el índice donde el hueco se encuentra
                indiceHuecoRen = i
                indiceHuecoCol = j

    return indiceHuecoRen, indiceHuecoCol

"""
    Estándar de codificación:
        Nombre de Función: hueco
        Descripción: Sustituye los valores del hueco y de la ficha seleccionada para simular el hecho de que se movieron las fichas.
        Parámetros de entrada: matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol
        Parámetros de salida: matriz
    Autores: 
        Juan Jesús Ortiz A01639936
""" 
def mover(matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol):   
    matriz[indiceHuecoRen][indiceHuecoCol] = matriz[indiceRen][indiceCol] #Asigna la ficha seleccionada a el hueco adyacente
    matriz[indiceRen][indiceCol] = 0 #Asigna el hueco al lugar donde se encontraba la ficha seleccionada
                
    return matriz

"""
    Estándar de codificación:
        Nombre de Función: main
        Descripción: Se encarga de solicitar al usuario si es que quiere llenar su tablero el mismo, o que se haga automático,
                        además se encarga de llamar a otras funciones según sea pertinente.
        Parámetros de entrada: matriz
        Parámetros de salida: -
    Autores: 
        Ricardo López A01284902
        Juan Jesús Ortiz A01639936
"""
def main(matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol):
    movimientos = 0
    valoresValidos = ['1', '2','3', '4','5','6','7','8','9','10','11','12','13','14','15','0']
    nombre = input("\nIngresa tu nombre: ")
    decision = input("\n¿Desea llenar la tabla manualmente o que el programa lo haga automático por usted? (m/a): ").lower()
    
    while decision!='m' and decision!='a': #Valida que la opción elegida sea correcta
        print('\033[31m'+"\nERROR: El valor que acaba de ingresar no es válido"+'\033[39m')
        decision = input("\n¿Desea llenar la tabla manualmente o que el programa lo haga automático por usted? (m/a): ").lower()

    if decision=='m':
        print('\033[36m'+"\nIngrese los valores con los que desea llenar el tablero (Un valor por entrada).\nPara indicar el espacio vacío ingrese cero."+'\033[39m')
        matriz = llenadoManual(matriz, valoresValidos)
        print("")
    else:
        llenadoAutomatico(matriz)

    desplegarTablero(matriz) #Imprime el tablero generado automatica o manualmente
    
    ganador = estadoGanador(matriz) #Se revisa si el orden de la matriz es correcto
    
    if ganador==False: #Imprime las instrucciones si la matriz sigue sin estar ordenada
        print('\033[36m'+"\nLe recordamos que en cualquier momento del juego puede decidir terminar la partida escribiendo \"no\" en la consola."+'\033[39m')

    while ganador!=True: #Pide al usuaria que seleccione que ficha mover hasta que se logre acomodar la matriz correctamente, a menos que se ingrese un 'no', lo que lo acabaría
        ficha = input("\n¿Cuál ficha quiere mover?: ")
        while ficha not in valoresValidos[0:15]: #Valida que la entrada sea un valor valido (número) o que sea 'no'
            if ficha=='no' or ficha=='NO' or ficha=='No' or ficha=='nO':
                print('\033[34m'+"\nTerminando partida...\n"+'\033[39m')
                exit()
            else:
                print('\033[31m'+"\nSolo puede ingresar valores entre el 1 y 15."+'\033[39m')
                ficha = input("\n¿Cuál ficha quiere mover?: ")
        
        ficha = int(ficha) #Convierte el valor de la entrada a un entero

        movimientos+=1 #Cuenta cada vez que se mueve una ficha
        indiceRen, indiceCol = indiceFicha(ficha, matriz)
        huecoAdyacente = hueco(matriz, indiceRen, indiceCol)
        indiceHuecoRen, indiceHuecoCol = indiceHueco(matriz)
        
        if huecoAdyacente == True: #Evalúa si la ficha seleccionada tenga el hueco adyacente; de ser así mueve la ficha en el tablero y lo despliega ya actualizado
            matriz = mover(matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol)
            desplegarTablero(matriz)
        else: #En caso de que la ficha no sea adyacente al hueco se imprimirá el tablero y marcará el error
            desplegarTablero(matriz)
            print('\033[31m'+"\nERROR: La ficha que ha seleccionado no puede moverse. El tablero no ha registrado cambios"+'\033[39m')
        
        ganador = estadoGanador(matriz) #Evalúa si el tablero el esta ordenado correctamente; de ser así sale del ciclo en el que se pide datos
        
    print('\033[32m'+"\n¡Felicidades {}, has ganado!\nHas utilizado {} movimientos.".format(nombre, movimientos))
    print('\033[39m')

#Se asignan valores iniciales de algunas variables.
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
indiceHuecoRen = 0
indiceHuecoCol = 0
indiceRen = 0
indiceCol = 0

main(matriz, indiceRen, indiceCol, indiceHuecoRen, indiceHuecoCol)