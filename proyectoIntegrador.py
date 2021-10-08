#proyecto integrador
#los numeros ingresados o generados tienen que ser del 1 al 15
#Para el espacio transformar el cero en string y después a '(espacio)' 
#buscar duplicados if x not in []

def llenadoManual(matriz):
    for i in range (4):
        matriz[i] = input().strip()
        matriz[i] = matriz[i].split(' ')
        for j in range(4):
            matriz[i][j] = int(matriz[i][j])
            while (matriz[i][j] > 16) or (matriz[i][j] < 0):
                print("Error. Valores fuera de rango")
                matriz[i] = input().strip()
                matriz[i] = matriz[i].split(' ')
                matriz[i][j] = int(matriz[i][j])

    #No la necesitamos
    """for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])"""
    
    if (len(matriz[0]) or len(matriz[1]) or len(matriz[0]) or len(matriz[1])) != 4:
        matriz = "ERROR: Solo se permiten 4 columnas"
        exit()

    """copias = [[],[],[],[]]
    for i in range(4):
        copias[i] = set(matriz[i])
    print("copias ",copias,"len",len(copias))"""
    
    """for x in matriz:
        for y in matriz[x]:
            if matriz.count(y)!=1:
                matriz="ERROR: Ingresó algún valor duplicado"""
    
    """if (len(matriz) != len(copias)):
        matriz = "ERROR: Ingreso algún valor duplicado"
        exit()"""

    return matriz

def llenadoAutomatico(matriz):
    from random import randint

    """for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numRand = randint(0,16)
            repetido = True    
            for x in range(len(matriz)):
                for y in range(len(matriz[x])):
                    if numRand != matriz[x][y]:
                        repetido=False"""
            
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numRand = randint(0,16)
            while (numRand not in lista) and (len(lista)<17):
                numRand = randint(0,16)
                lista.append(numRand)
                matriz[i][j] = numRand
    print(lista)
    return matriz

def desplegarTablero(matriz):
    print(matriz,"\n")
    
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()
    
    return matriz

def main(matriz):
    #preguntar el nombre
    decision = input("¿Desea llenar la tabla manualmente o que el programa lo haga automatico por usted? (m/a): ")
    if decision=='m':
        print("Ingrese las filas separadas por espacios")
        matriz = llenadoManual(matriz)
    else:
        llenadoAutomatico(matriz)

    print("El numero cero indica la casilla vacia")
    desplegarTablero(matriz)

#matriz = [[0]*4]*4 ¿Porque se repiten despues de llenarse?
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
main(matriz)