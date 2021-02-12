
import copy
tablero = [[-1,-1,-1,-1, 3,-1,-1,-1, 8],
           [-1, 6, 8, 2,-1, 9,-1, 4,-1],
           [ 2,-1,-1, 4, 7, 8,-1,-1, 6],
           [-1,-1, 4, 3, 8, 6,-1,-1,-1],
           [ 8,-1, 9,-1,-1,-1, 3, 6,-1],
           [-1,-1,-1,-1,-1,-1, 4,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [ 9, 5,-1,-1,-1, 2, 6,-1, 4],
           [-1, 8, 7,-1, 6,-1, 2,-1, 5]]
tablero = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
tablero_solucion=copy.deepcopy(tablero)

def comprobar_fila(_tablero,fila,numero):
    for x in _tablero[fila]:
        if x == numero:
            return False
    return True

def comprobar_columna(_tablero,columna,numero):

    for x in range(0,9,1):
        if _tablero[x][columna] == numero:
            return False
    return True

def comprobar_vecinos(_tablero,fila,columna,numero):

    fila_grande = fila//3
    columna_grande = columna//3

    for x in range(fila_grande*3,fila_grande*3+3):
        for y in range(columna_grande*3,columna_grande*3+3):
            
            if fila == x and columna == y:
                continue

            if _tablero[x][y] == numero:
                #print("comprobar: "+str(numero))
                return False

    return True





def comprobar_solucion(fila,columna):

    global tablero_solucion
    if fila > 8:
        return True

    #Recorremos las filas y columnas que nos quedan por comprobar
    solucion = False
    
    #Si es una posicion pre-fijada, pasamos a la siguiente
    if tablero[fila][columna] != -1:
        if columna+1 > 8:
            solucion = comprobar_solucion(fila+1,0)
        else:
            solucion = comprobar_solucion(fila,columna+1)
    #Si es un numero a buscar, lo buscamos
    else:
        for numero in range(1,9+1,1):

            
            if comprobar_vecinos(tablero_solucion,fila,columna,numero):
                if comprobar_fila(tablero_solucion,fila,numero):
                    if comprobar_columna(tablero_solucion,columna,numero):
                        tablero_solucion[fila][columna] = numero
                        if columna+1 > 8:
                            solucion = comprobar_solucion(fila+1,0)
                        else:
                            solucion = comprobar_solucion(fila,columna+1)
                        
            if not solucion:
                tablero_solucion[fila][columna] = -1
            else:
                break

    return solucion



comprobar_solucion(0,0)
print("--------------------Sodoku entrada----------------------")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in tablero]))
print("--------------------Sodoku solucion---------------------")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in tablero_solucion]))
print("--------------------------------------------------------")
