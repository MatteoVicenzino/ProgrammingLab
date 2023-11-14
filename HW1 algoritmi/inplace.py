import random
import time
import matplotlib.pyplot as plt


def mergesort_outofplace(A, end, begin = 0):
    if end > begin:

        # median è l'ultimo elemento del primo sub array
        median = (begin + end)//2

        # chiamo mergesort ricorsivamente per i due sub-array
        mergesort_outofplace(A, median, begin)
        mergesort_outofplace(A, end, median+1)

        merge_outofplace(A, begin, median, end)

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

def mergesort_inplace(A, end, begin = 0):
    if end > begin:

        # median è l'ultimo elemento del primo sub array
        median = (begin + end)//2

        # chiamo mergesort ricorsivamente per i due sub-array
        mergesort_inplace(A, median, begin)
        mergesort_inplace(A, end, median+1)

        merge_inplace(A, begin, median, end)

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


def genera_casuale():
    return random.randint(0, 100)



def faiin():
    A = [68, 90, 10, 41, 42, 45, 17, 68, 63, 95]
    dimensione = len(A)
    mergesort_inplace(A, dimensione-1)

    
def faiout():
    A = [1, 2, 4, 6, 2, 7, 4, 0, 55, 6, 3, 2, 7]
    dimensione = len(A)
    mergesort_outofplace(A, dimensione-1)


    
A = faiin()
print("{}".format(A))
B = faiout()
print("{}".format(B))