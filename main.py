
tablero = [[-1,-1,-1,-1, 3,-1,-1,-1, 8],
           [-1, 6, 8, 2,-1, 9,-1, 4,-1],
           [ 2,-1,-1, 4, 7, 8,-1,-1, 6],
           [-1,-1, 4, 3, 8, 6,-1,-1,-1],
           [ 8,-1, 9,-1,-1,-1, 3, 6,-1],
           [-1,-1,-1,-1,-1,-1, 4,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [ 9, 5,-1,-1,-1, 2, 6,-1, 4],
           [-1, 8, 7,-1, 6,-1, 2,-1, 5]
          ]



def comprobar_fila(tablero,fila,numero):

    for x in tablero[fila]:
        if x == numero:
            y = x
            #return False
        
    return True

def comprobar_columna(tablero,columna,numero):

    for x in range(0,9,1):
        if tablero[x][columna] == numero:
            return False

        return True

def comprobar_vecinos(tablero,fila,columna,numero):

    fila_grande = fila//3
    columna_grande = columna//3

    for x in range(fila_grande*3,fila_grande*3+3):
        for y in range(columna_grande*3,columna_grande*3+3):
            
            if fila == x and columna == y:
                continue

            if tablero[fila][columna] == numero:

                return False
    return True

comprobar_vecinos(tablero,2,5,7)