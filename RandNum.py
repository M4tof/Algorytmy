import random

def RandGen():
    N=int(input("Length of random number list: "))
    L=int(input("Min value: "))
    H=int(input("Max value: "))

    list=[]
    for i in range(N):
        list.append(random.randint(L,H))

    return(list)

#tab=RandGen()

#print(tab)