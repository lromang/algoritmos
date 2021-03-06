# Fernanda Mora Alba
# 000103596
# Luis Manuel Román García
# 000117077
#---------------------------------
# Librerías utilizadas
import numpy as np
import timeit
#---------------------------------
# Método de insercion directa
def inser_sort(array):
    N = array.size
    for i in range(1, N):  
        aux = array[i]
        k = i - 1
        while (k >= 0) == True & (aux < array[k]) == True:
            array[k + 1] = array[k]
            k = k - 1
        array[k + 1] = aux
    return array

#---------------------------------
# Método mezcla
# ordenamiento
def sort(L,R):
    NL = L.size
    NR = R.size
    answer = np.empty(0)
    i = 0
    j = 0
    k = 0
    while (i < NL) == True & (j < NR) == True:
        if L[i] <= R[j]:
            answer = np.hstack([answer, L[i]])
            k = k + 1
            i = i + 1
        else:
            answer = np.hstack([answer, R[j]])
            k = k + 1
            j = j + 1
    if i < NL:
        answer = np.hstack([answer, L[i::]])
    elif j < NR:
        answer = np.hstack([answer, R[j::]])
    return answer
# mezcla
def mix(array):
    N = array.size
    if N == 1:
        return array
    elif N == 2:
        if array[0] >= array[1]:
            return array[1::-1]
    return sort(mix(array[0:N/2]), mix(array[N/2:N]))
#---------------------------------
trials = np.hstack([np.array(range(10,100,10)),np.array(range(100,5000,100))])
k = trials.size
elapsed_mix = np.empty(k)
elapsed_ins = np.empty(k)
j = 1
for i in trials:
    a = np.floor(np.random.rand(i) * 100)
    start_time = timeit.default_timer()
    mix(a)
    elapsed_mix[j] = timeit.default_timer() - start_time
    start_time = timeit.default_timer()
    inser_sort(a)
    elapsed_ins[j] = timeit.default_timer() - start_time
    j = j +1
# Guardamos resultados
np.save("/home/luis/Documents/oto2015/algoritmos/code/mix.txt",elapsed_mix)
np.save("/home/luis/Documents/oto2015/algoritmos/code/ins.txt",elapsed_ins)
