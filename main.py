
import copy
from tkinter import *
from tkinter.ttk import *
import time
tablero = [[-1,-1,-1,-1, 3,-1,-1,-1, 8],
           [-1, 6, 8, 2,-1, 9,-1, 4,-1],
           [ 2,-1,-1, 4, 7, 8,-1,-1, 6],
           [-1,-1, 4, 3, 8, 6,-1,-1,-1],
           [ 8,-1, 9,-1,-1,-1, 3, 6,-1],
           [-1,-1,-1,-1,-1,-1, 4,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [ 9, 5,-1,-1,-1, 2, 6,-1, 4],
           [-1, 8, 7,-1, 6,-1, 2,-1, 5]]

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
                return False

    return True

def comprobar_solucion(fila,columna):

    global tablero_solucion
    global matrix_label
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
        #+1 es por que el stop es excluyente
        for numero in range(1,9+1,1):

            #Relizo las comprobación de que sea una solucion correcta
            if comprobar_vecinos(tablero_solucion,fila,columna,numero):
                if comprobar_fila(tablero_solucion,fila,numero):
                    if comprobar_columna(tablero_solucion,columna,numero):
                        matrix_label[fila][columna][0].itemconfig(matrix_label[fila][columna][1], text=numero)
                        matrix_label[fila][columna][0].itemconfig(matrix_label[fila][columna][1], fill="green")

                        tablero_solucion[fila][columna] = numero
                        if columna+1 > 8:
                            solucion = comprobar_solucion(fila+1,0)
                        else:
                            solucion = comprobar_solucion(fila,columna+1)

            #Si no hubiera una solución correcta en este nodo de exploración lo elimino
            #Si la solución fuera true es que ha llegado al final y por lo tanto no tengo 
            # que seguir buscando            
            if not solucion:
                tablero_solucion[fila][columna] = -1
            else:
                break
    return solucion

matrix_label = []

"""

window = Tk()

window.title("Sudoku-Solver")
lbl = Label(window, text="Hello")
for x,fila in enumerate(tablero):
    fila_label = []
    for y,columna in enumerate(fila):
        lbl = Label(window,text=str(columna))
        lbl.grid(row=x,column=y,sticky=W,pady=2)
        fila_label.append(lbl)
"""


root = Tk()

box_frame = Frame(root)
box_frame.pack()

for x,fila in enumerate(tablero):
    prep_list = []
    for y,columna in enumerate(fila):
        prep_list.append([Canvas(box_frame, width=50, height=50), ''])
        prep_list[y][0].create_line(50, 50, 0, 50)
        prep_list[y][0].create_line(50, 50, 50, 0)
        text_id = prep_list[y][0].create_text(25,25,fill="red",font="Times 20 italic bold",
                        text=columna)
        prep_list[y][1] = text_id
        prep_list[y][0].grid(row=x, column=y)
    matrix_label.append(prep_list)

solucion = False
root.after(1000, comprobar_solucion,0,0)

root.mainloop()

print("--------------------Sodoku entrada----------------------")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in tablero]))
print("--------------------Sodoku solucion---------------------")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in tablero_solucion]))
print("--------------------------------------------------------")
