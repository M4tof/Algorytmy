import random

def RandGen(N,L,H):
    list=[]
    for i in range(N):
        list.append(random.randint(L,H))

    return(list)

#tab=RandGen(100,1,100)

#print(tab)