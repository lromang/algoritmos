##################################################
## Rutinas para resolver el problema de la mochila
## utilizando programación dinámica.
##################################################
## Librerías utilizadas
import numpy as np

###################################################
#################### Top Down #####################
## Regresa el valor optimo que puede ser alcanzado
## introduciendo objetos de tamaño w_i y utilidad
## v_i dentro de una mochila de capacidad W
## utilizando el paradigma recursivo top-down.
###################################################


def knapsack_td(i, W):
  ##############################
  # i: ínidce de interés.
  # W: capacidad de la mochila.
  ##############################
  # Si la mochila no tiene capacidad o
  # si no hay objetos regresamos 0
  if W == 0 or i == -1:
    return 0
  # Si hay un único objeto lo regresamos
  if v.size == 1:
    return v[i]
  else:
    # Si el peso del objeto es menor que la
    # capacidad de la mochila vemos si nos
    # conviene meterlo o no.
    if W - w[i] >= 0:
      return max(knapsack_td(i - 1, W), v[i] + knapsack_td(i - 1, W - w[i]))
    else:
      # Si no cabe el objeto no lo metemos.
      return knapsack_td(i - 1, W)

###################################################
################### Bottom Up #####################
## Regresa el valor optimo que puede ser alcanzado
## introduciendo objetos de tamaño w_i y utilidad
## v_i dentro de una mochila de capacidad W
## utilizando el paradigma recursivo bottom-up.
###################################################
def knapsack_bu(n, W):
  ##############################
  # i: ínidce de interés.
  # W: capacidad de la mochila.
  ##############################
  V = np.zeros(W)
y  for j in range(W)[1:]:
    for i in range(n):
      if w[i] <= j and (v[i] + V[j - w[i]]) > V[j]:
        V[j] = v[i] + V[j - w[i]]
  return V



##################################################
## Pruebas
##################################################
W = 20
w = np.array([11, 7, 5, 4, 3, 3, 3, 2, 2, 2, 2 ,1])
v = np.array([20, 10, 11, 5, 25, 50, 15, 12, 6, 4, 5, 30])
i = w.size - 1
n = i + 1
## Top Down
sol_td = knapsack_td(i, W)
## Bottom Up
sol_bu = knapsack_bu(n, W)
##################################################
