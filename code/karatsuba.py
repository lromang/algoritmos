######################################################################################
## Split the numbers in two (precise)
## Luis Manuel Roman Garcia 000117077
## Maria Fernanda Mora Alba 000103596
import numpy as np
from decimal import *
import time
######################################################################################
## Obtener largo numeros
def int_length_p(integer):
  integer  = Decimal(integer).log10()//1
  return integer + 1

## Dividir numeros en dos
def split_num_p(integer, cut):
  ## Vector de resultados
  result     = [0,0,0]
  ## Convertir numeros a clases Decimal.
  integer    = Decimal(integer)
  divider    = 10
  ## Obtener punto de corte
  int_size   = cut//2
  divider    = 10**int_size
  ## Obtener mitades
  first_hal  = int(integer/divider)
  second_hal = integer - Decimal(first_hal*divider)
  ## Almacenar resultados
  result[2]  = divider
  result[0]  = first_hal
  result[1]  = second_hal
  return result

## Multiplicar numeros
def karatsuba(int1, int2):
  ## Obtener largo de numeros.
  length1 = int_length_p(int1)
  length2 = int_length_p(int2)
  ## Verificar condicion caso base.
  if length1 <= 2 or length2 <= 2:
    return int1 * int2
  else:
    ## Dividir los arreglos en dos sub partes
    cut = np.min([length1, length2])
    int1_split = split_num_p(int1, cut)
    int2_split = split_num_p(int2, cut)
    ## Obtener el largo del menor
    power = int1_split[2]
    ## llevar a cabo la multiplicacion
    ac = karatsuba(int1_split[0], int2_split[0])
    bd = karatsuba(int1_split[1], int2_split[1])
    ab = np.sum(int1_split[0:2])
    cd = np.sum(int2_split[0:2])
    apb_dpc = karatsuba(ab, cd) - ac -bd
    return np.power(power, 2)*ac + power*apb_dpc + bd

###Ejemplos
karatsuba(1234,5678)
karatsuba(12341234,234)
######################################################################################
## Pruebas de estress
######################################################################################
## Facil
time_start   = time.clock()
karatsuba(1234,5678)
time_elapsed = (time.clock() - time_start)

time_start   = time.clock()
1234*5678
time_elapsed = (time.clock() - time_start)


## medio
time_start   = time.clock()
karatsuba(12341234123412341234,1241241234123412341234)
time_elapsed = (time.clock() - time_start)

time_start   = time.clock()
12341234123412341234*1241241234123412341234
time_elapsed = (time.clock() - time_start)

## difícil
LARGE = 17**987273 ## 1.2 million digitos
time_start_d   = time.clock()
EXTRA_LARGE    = karatsuba(LARGE, LARGE)
time_elapsed_d = (time.clock() - time_start)

#####
##test
####
## Obtener largo numeros
def int_length_p(integer):
  integer  = Decimal(integer).log10()//1
  return integer + 1

## Dividir numeros en dos
def split_num_p(integer, cut):
  ## Vector de resultados
  result     = [0,0,0]
  ## Convertir numeros a clases Decimal.
  integer    = str(integer)
  ## Obtener punto de corte
  half       = int(cut/2)
  ## Obtener mitades
  first_hal   = integer[0:half]
  second_hal  = integer[half:int(cut)]
  ## Almacenar resultados
  result[0]  = Decimal(first_hal)
  result[1]  = Decimal(second_hal)
  ##---------------------------
  ## Obtener posicion decimal
  divider    = 10
  ## Obtener punto de corte
  divider    = 10**half
  ##---------------------------
  result[2]  = divider
  return result

## Multiplicar numeros
def karatsuba(int1, int2):
  ## Obtener largo de numeros.
  length1 = int_length_p(int1)
  length2 = int_length_p(int2)
  ## Verificar condicion caso base.
  if length1 <= 2 or length2 <= 2:
    return int1 * int2
  else:
    ## Dividir los arreglos en dos sub partes
    cut = np.min([length1, length2])
    int1_split = split_num_p(int1, cut)
    int2_split = split_num_p(int2, cut)
    ## Obtener el largo del menor
    power = int1_split[2]
    ## llevar a cabo la multiplicacion
    ac = karatsuba(int1_split[0], int2_split[0])
    bd = karatsuba(int1_split[1], int2_split[1])
    ab = np.sum(int1_split[0:2])
    cd = np.sum(int2_split[0:2])
    apb_dpc = karatsuba(ab, cd) - ac -bd
    return np.power(power, 2)*ac + power*apb_dpc + bd
