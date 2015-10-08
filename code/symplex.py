
# Luis Manuel Roman Garcia
# Maria Fernanda Mora Alba
import numpy as np
import numpy.matlib
# Problema de prueba,
# A es la matriz de restricciones, 
# z es la funcion objetivo
# b es el vector de restricciones
A = np.array([[4,1,1],[2,3,1],[1,2,3]])
z = np.array([3,2,1])
b = np.array([[30],[60],[40]])
# Testing     
size_A  = A.shape
slack   = np.matlib.identity(size_A[0])
shadow  = np.hstack([-z, np.zeros(size_A[0] + 1)])
tableau = np.hstack([A, slack,b])
tableau = np.vstack([tableau, shadow])
# Funciones
def pivot(tableau):
    # z debe contener ya los precios sombra de las
    # variables de holgura.
    tab_size = tableau.shape
    z        = tableau[-1, :]
    # Elegimos el elemento que esta en el indice uno pues z es
    # una matriz horizontal.
    enter_index = np.where(z[0] == np.min(z[0]))[1].item(0)
    coef        = np.divide(tableau[:-1,-1], tableau[:-1, enter_index])
    # Elegimos el elemento que esta en el indice cero pues
    # coef es una matriz vertical
    positive_coef = coef[np.where(coef >= 0)[0]]
    min_pos_coef  = positive_coef[0][np.where(positive_coef[0] == np.min(positive_coef))[0].item(0)][0].item(0)
    leave_index   = np.where(coef == min_pos_coef)[0].item(0)
    pivot         = np.divide(tableau[leave_index, :], tableau[leave_index, enter_index])
    for i in range(tab_size[0]):
        tableau[i, :] = tableau[i, :] - tableau[i, enter_index]*pivot
    tableau[leave_index, :] = pivot
    return tableau

def simplex(A,b,z):
    if np.sum(-z < 0) ==  0:
        print("La solucion es:")
    else:
        size_A = A.shape
        slack   = np.matlib.identity(size_A[0])
        shadow = np.hstack([-z, np.zeros(size_A[0] + 1)])
        tableau = np.hstack([A, slack,b])
        tableau = np.vstack([tableau, shadow])
        while np.sum(shadow < 0) != 0:
            tableau = pivot(tableau)
            shadow  = tableau[-1, :]
    return [tableau,tableau[-1,-1]]
#---------------------------------------------------------------
#---------------------------------------------------------------
# Problemas de prueba
#---------------------------------------------------------------
# A es la matriz de restricciones, 
# z es la funcion objetivo
# b es el vector de restricciones
# simplex regresa el tabloide final. Ahi se puede verificar 
# el valor de las variables, los precios sombra, y el valor
# maximo de la funcion
#---------------------------------------------------------------
# Problema de prueba 1 (clase)
A = np.array([[2,3],[4,1],[2,9]])
z = np.array([21,31])
b = np.array([[25],[32],[54]])
simplex(A, b, z);
# Problema de prueba 2
A = np.array([[-1,1],[1,1],[2,5]])
z = np.array([4,6])
b = np.array([[11],[27],[90]])
simplex(A, b, z);
# Problema de prueba 3
A = np.array([[4,1,1],[2,3,1],[1,2,3]])
z = np.array([3,2,1])
b = np.array([[30],[60],[40]])
simplex(A, b, z);
