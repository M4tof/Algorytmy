tab=[21,37,2,1,3,7,0]

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


heapSort(tab)

print(tab)