from time import sleep
from threading import Timer

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

#quick, 2 parts
def Partiton(dane,p,r):
    x = dane[r]
    i=p-1
    for j in range(p,r):
        if dane[j] <= x:
            i+=1
            dane[i],dane[j]=dane[j],dane[i]
    dane[i+1],dane[r] = dane[r],dane[i+1]
    return i+1

def quickSort(dane,p,r):
    if p < r:
        q = Partiton(dane,p,r)
        quickSort(dane,p,q-1)
        quickSort(dane,q+1,r)

def sleepSort(dane):
    sleepSort.result = []
    def add1(x):
        sleepSort.result.append(x)
    mx = dane[0]
    for v in dane:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleepSort.result

def heapLite(dane,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if (l < n) and (dane[i] < dane[l]):
        largest = l
    
    if (r < n) and (dane[largest] < dane[r]):
        largest = r

    if largest != i:
        dane[i], dane[largest] = dane[largest], dane[i]
        heapLite(dane,n,largest)

def heapSort(dane):
    n = len(dane)
    for i in range(n//2,-1,-1):
        heapLite(dane,n,i)
    for i in range(n-1,0,-1):
        dane[i],dane[0]=dane[0],dane[i]
        heapLite(dane,i,0)