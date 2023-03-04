tab=[11,9,7,5,3,1,8,6,4,2,0]

def selectionSort(dane):
    n=len(dane)
    for j in range(0,n-1):
        minimum=j
        for i in range(j+1,n):
            if dane[i] < dane[minimum]:
                minimum = i
        dane[minimum],dane[j] = dane[j],dane[minimum]
    return dane

def insertSort(dane):
    n=len(dane)
    for j in range(1,n):
        key = dane[j]
        i=j-1
        while (i >= 0) and (dane[i] > key) :
            dane[i+1] = dane[i]
            i=i-1
        dane[i+1] = key
    return dane

