# Luis Manuel Román García
# 000117077
#---------------------------------
# Librerías utilizadas
import numpy as np
#---------------------------------
# Método de intercambio
def inter_sort(array):
    # obtenemos longitud del arreglo
    N = array.size
    for i in range(1, N):  # range da la secuencia de números hasta uno menor a la cota superior
        aux = array[i]
        k = i - 1
        while (k >= 0) == True & (aux < array[k]) == True:
            array[k + 1] = array[k]
            k = k - 1
        array[k + 1] = aux
    return array

#---------------------------------
# Método directo
def direct_sort():
    return
