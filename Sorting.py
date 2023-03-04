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
