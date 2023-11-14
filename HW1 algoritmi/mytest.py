import random
import numpy as np
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

# mergesort implementato come visto a lezione
def mergesort_outofplace(A, end, begin = 0):
    if end > begin:

        # median è l'ultimo elemento del primo sub array
        median = (begin + end)//2

        # chiamo mergesort ricorsivamente per i due sub-array
        mergesort_outofplace(A, median, begin)
        mergesort_outofplace(A, end, median+1)

        merge_outofplace(A, begin, median, end)
        return A
        
def merge_outofplace(A, begin, median, end):

    # creo 2 sub-array d'appoggio
    # il primo sub-array: begin -> median
    # il secondo sub-array: median+1 -> end

    L = A[begin:median+1]
    R = A[median+1:end+1]

    # i scorre l'array L
    # j scorre l'array R

    i = 0
    j = 0

    # scorro tutto l'array A
    for k in range(begin, end+1):

        # c
        if i < len(L) and (j >= len(R) or L[i] <= R[j]):
            # se l'elemento in L < elemento in R, prendo L
            A[k] = L[i]
            i += 1
        else:
            # se l'elemento in R < elemento in L, prendo R
            A[k] = R[j]
            j += 1

# mergesort inplace con puntatori
def mergesort_inplace(A, end, begin = 0):
    if end > begin:

        # median è l'ultimo elemento del primo sub array
        median = (begin + end)//2

        # chiamo mergesort ricorsivamente per i due sub-array
        mergesort_inplace(A, median, begin)
        mergesort_inplace(A, end, median+1)

        merge_inplace(A, begin, median, end)
        return A
        
def merge_inplace(A, begin, median, end):

    # invece che creare due sub-array uso due puntatori a dei valori dell'array
    # il primo sub-array: begin -> median
    # il secondo sub-array: median+1 -> end

    # return quando l'array è ordinato
    if (A[median] <= A[median+1]):
        return

    while begin <=median and median+1 <= end:

        # confronto i primi elementi dei due sub array
        if A[begin] > A[median+1]:

            # se non sono ordinati
            # salvo  il valore più piccolo per metterlo all'inizio
            small = A[median+1]


            # scalo ogni elemento del primo array di 1 posto a destra


            for i in range(median+1, begin, -1):
                   A[i] = A[i-1]

            A[begin] = small

            # i puntatori al primo elemento vengono incrementati
            begin +=1
            median +=1



        else:
            # se invece il primo è nella posizione giusta passo al secondo
            begin += 1


"""

def esegui_outofplace():
    arr = []
    
    for i in range(1, 1001):

        A = []
        for j in range(0, i):
            A.append(random.randint(0, 10))

        
        dimensione = len(A)
        start_time = time.time()
        mergesort_outofplace(A, dimensione-1)
        arr.append([dimensione, time.time() - start_time])
        
        # eseguo con array sempre più lunghi
        #print("{}".format(A))
    return arr
    
def esegui_inplace():
    arr = []

    for i in range(1, 1001):

        A = []
        for j in range(0, i):
            A.append(random.randint(0, 10))


        dimensione = len(A)
        start_time = time.time()
        mergesort_inplace(A, dimensione-1)
        arr.append([dimensione, time.time() - start_time])

        # eseguo con array sempre più lunghi
        #print("{}".format(A))
    return arr

"""


def esegui(dim_input):
    A = []
    for i in range(0, dim_input):
        
        A.append(random.randint(0, 10))

    dimensione = len(A)
    mergesort_inplace(A, dimensione-1)
    return

    

dim_input = [10**i for i in range(0, 3)]
timing = []
ntrials = 100

for i in range(len(dim_input)):
    since = time.time()
    for j in range(ntrials):
        esegui(dim_input[i])
        print("done merge {}".format(dim_input[i]))
    elapsed = time.time() - since
    timing.append(elapsed/ntrials)

plt.plot(dim_input, timing)
# plot linear relationship between input size and time
plt.plot(dim_input, [(timing[-1]/dim_input[-1]) * dim_input[i]  for i in range(len(dim_input))], 'k--', alpha=0.5)
plt.xlabel('Input size')
plt.ylabel('Time elapsed')
plt.title('Time complexity')


plt.show()

print("done")



"""

oop_arr = esegui_outofplace()
ip_arr = esegui_inplace()

oop_arr = np.array(oop_arr)
ip_arr = np.array(ip_arr)

plt.plot(oop_arr[:,0], oop_arr[:,1], c="blue")
plt.plot(ip_arr[:,0], ip_arr[:,1], c="red")
#plt.plot(x, 2*np.log2(x), label="2 log2 m", color="black", linestyle="--", alpha=0.5)

#plt.plot(, c="red")

plt.xlim(0, 1)
plt.ylim(0, 3)
plt.xlabel("dimensione")
plt.ylabel("tempo")
plt.show()


"""