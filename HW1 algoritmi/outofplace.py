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


# Function to generate a random array of size n
def generate_random_array(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Measure the time complexity of a sorting function for different input sizes
def measure_time_complexity(sort_func, sizes):
    time_complexity = []

    for size in sizes:
        A = generate_random_array(size)
        start_time = time.time()
        sort_func(A, len(A) - 1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_complexity.append(elapsed_time)

    return time_complexity

# Sizes of input arrays (e.g., 100, 200, 300, ..., 1000)
input_sizes = list(range(100, 1100, 100))

# Measure time complexity for both merge sort functions
outofplace_complexity = measure_time_complexity(mergesort_outofplace, input_sizes)
inplace_complexity = measure_time_complexity(mergesort_inplace, input_sizes)

# Plot the time complexity graphs
plt.plot(input_sizes, outofplace_complexity, label='Out-of-Place Merge Sort')
plt.plot(input_sizes, inplace_complexity, label='In-Place Merge Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Merge Sort Time Complexity')
plt.show()