import random
import math

MacierzSąsiedztwa=[]    
RowList=[]
ListaIncydencji=[]

def DAGen(N):
    global MacierzSąsiedztwa, RowList
    for y in range(N):
        MacierzSąsiedztwa.append([0]*N)
        
    for inte in range(1,N+1):
        RowList.append(inte)
        
    for Y in range(N):
        for X in range(Y+1,N):
            MacierzSąsiedztwa[Y][X]=1 #1 is conection from Row to Column
            MacierzSąsiedztwa[X][Y]=2 #2 is conection from Column to Row

    Full = N*(N-1)/2
    ToDell = math.trunc(Full*0.4)

    while ToDell > 0:
        Y = random.randint(0,N-1)
        if (MacierzSąsiedztwa[Y].count(1) > 1):
            
            test=0
            while(test==0):
                IntToDel=random.randint(Y+1,N-1)
                if(MacierzSąsiedztwa[Y][IntToDel]==1):
                    test=1
            
            MacierzSąsiedztwa[Y][IntToDel]=0
            MacierzSąsiedztwa[IntToDel][Y]=0
            ToDell-=1

def PrintMacierzSąsiedztwa():
    global MacierzSąsiedztwa, RowList
    N = len(MacierzSąsiedztwa)
    print(" ",RowList)
    for i in range(N):
        print(i+1,MacierzSąsiedztwa[i])

DAGen(3)
PrintMacierzSąsiedztwa()

def Macierz2Lista(Macierz):
    for n in range(len(Macierz)):
        TempList=[n+1]
        for Xn in range(len(Macierz[0])):
            if Macierz[n][Xn]==1:
                TempList.append(Xn+1)
        ListaIncydencji.append(TempList)

Macierz2Lista(MacierzSąsiedztwa)
