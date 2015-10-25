## Luis Manuel Roman Garcia
## 000117077

##################################################
## Rutinas para resolver el problema de la mochila
## y secuencias de numeros de catalan
## utilizando programación dinámica.
##################################################


##################################################
## Librerías utilizadas
##################################################
import numpy as np
import math

##############################################################################
##############################################################################
################################### TOP DOWN #################################
##############################################################################
##############################################################################

###################################################
######### Top Down knapsack (recursivo) ###########
###################################################
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
  if i == -1:
    return 0
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
######## Top Down knapsack (memoizacion) ##########
###################################################
## Regresa el valor optimo que puede ser alcanzado
## introduciendo objetos de tamaño w_i y utilidad
## v_i dentro de una mochila de capacidad W
## utilizando el paradigma recursivo top-down, con
## memoizacion.
###################################################
def knapsack_td_m(i, W):
  ##############################
  # i: ínidce de interés.
  # W: capacidad de la mochila.
  ##############################
  # Si la mochila no tiene capacidad o
  # si no hay objetos regresamos 0
  if i == -1:
    return 0
  else:
    # Si el peso del objeto es menor que la
    # capacidad de la mochila vemos si nos
    # conviene meterlo o no.
    if knapsack[i, W] < 0:
      # Verificamos si ya contabamos con el
      # valor que se desea calcular.
      if W - w[i] >= 0:
        knapsack[i, W] = max(knapsack_td_m(i - 1, W),
                             v[i] + knapsack_td_m(i - 1, W - w[i]))
      else:
        # Si no cabe el objeto no lo metemos.
        knapsack[i, W] = knapsack_td_m(i - 1, W)
    return knapsack[i, W]

###################################################
########## Top Down Catalan (recursivo) ###########
###################################################
## Regresa el numero de catalan correspondiente
## al valor N usando recursion.
###################################################
def catalan_td(N):
  ##############################
  # N es el indice del numero de
  # catalan.
  ##############################
  if N == 1 or N == 0:
    return 1
  else:
    catalan = 0
    for i in range(N + 1)[1:]:
      catalan = catalan + catalan_td(i - 1) * catalan_td(N - i)
    return catalan

###################################################
######### Top Down Catalan (memoizacion) ##########
###################################################
## Regresa el numero de catalan correspondiente
## al valor N usando recursion y el metodo de
## memoizacion.
###################################################
def catalan_td_m(N):
  ##############################
  # N es el indice del numero de
  # catalan.
  ##############################
  if N == 1 or N == 0:
    return 1
  else:
    if catalan_calc[N] < 0:
      catalan = 0
      for i in range(N + 1)[1:]:
        catalan = catalan + catalan_td(i - 1) * catalan_td(N - i)
      catalan_calc[N] = catalan
    return catalan_calc[N]

##############################################################################
##############################################################################
################################## BOTTOM UP #################################
##############################################################################
##############################################################################

###################################################
############### Bottom Up Knapsack ################
###################################################
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
  V = np.zeros([n, W])
  for i in range(n):
    for j in range(W):
      if w[i] <= j :
        V[i, j] = max(V[i - 1, j], v[i] + V[i - 1, j - w[i]])
      else:
        V[i, j] = V[i - 1, j]
  return V[i, j]

###################################################
############### Bottom Up Catalan  ################
###################################################
def catalan_bu(N):
  # Si N = 0 o N = 1 regreso 1.
  if N == 0 or N == 1:
    return 1
  else:
    sol     = np.zeros(N + 1)
    sol[0]  = 1
    cat_sum = 0
    for j in range(N + 1)[1:]:
      # En este for se almacenan los
      # valores de cat_sum en sol.
      cat_sum = 0
      for i in range(j + 1):
        # En este for se calcula
        # la suma acumulada de
        # los valores anteriores.
        cat_sum  = cat_sum + sol[i]*sol[j- i - 1]
      sol[j]     = cat_sum
  return sol[N]


##############################################################################
##############################################################################
################################### PRUEBAS ##################################
##############################################################################

##############################################################################
## TOP DOWN
##############################################################################

##############################################################################
## Knapsack
W = 20
w = np.array([11, 7, 5, 4, 3, 3, 3, 2, 2, 2, 2 ,1])
v = np.array([20, 10, 11, 5, 25, 50, 15, 12, 6, 4, 5, 30])
i = w.size - 1
n = i + 1
## Matriz para memoizacion
knapsack = -1*np.ones([n + 1, W + 1])
## Top Down
sol_td   = knapsack_td(i, W)
sol_td_m = knapsack_td_m(i, W)
##############################################################################
## Catalan
N = 5
catalan_calc  = -1*np.ones(N + 1)
sol_catalan   = catalan_td(N)
sol_catalan_m = catalan_td_m(N)

##############################################################################
## BOTTOM UP
##############################################################################
## Knapsack
sol_bu = knapsack_bu(n,W)
## Catalan
N = 20
sol_catalan_bu = catalan_bu(N)
