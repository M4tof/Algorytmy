def selectionSort(dane):
    n=len(dane)
    for j in range(0,n-1):
        minimum=j
        for i in range(j+1,n):
            if dane[i] < dane[minimum]:
                minimum = i
        dane[minimum],dane[j] = dane[j],dane[minimum]
    return dane