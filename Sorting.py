import sys
sys.setrecursionlimit(200000000)

def selectionSort(dane):
    n=len(dane)
    for j in range(0,n-1):
        minimum=j
        for i in range(j+1,n):
            if dane[i] < dane[minimum]:
                minimum = i
        dane[minimum],dane[j] = dane[j],dane[minimum]

def insertSort(dane):
    n=len(dane)
    for j in range(1,n):
        key = dane[j]
        i=j-1
        while (i >= 0) and (dane[i] > key) :
            dane[i+1] = dane[i]
            i=i-1
        dane[i+1] = key

def mergeSort(dane):
    n=len(dane)
    if n > 1:
        mid=n//2
        left=dane[:mid]
        right=dane[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                dane[k] = left[i]
                i+=1
            else:
                dane[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            dane[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            dane[k] = right[j]
            j+=1
            k+=1

def heapify(dane,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if (l < n) and (dane[i] < dane[l]):
        largest = l
    
    if (r < n) and (dane[largest] < dane[r]):
        largest = r

    if largest != i:
        dane[i], dane[largest] = dane[largest], dane[i]
        heapify(dane,n,largest)

def heapSort(dane):
    n = len(dane)
    for i in range(n//2,-1,-1):
        heapify(dane,n,i)
    for i in range(n-1,0,-1):
        dane[i],dane[0]=dane[0],dane[i]
        heapify(dane,i,0)


def quickSort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)
    else:
        return array
