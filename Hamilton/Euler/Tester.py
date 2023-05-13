import math
import time
import sys
import random

sys.setrecursionlimit(2000000)
Macierz1=[] 
Macierz2=[[0,1,1],[1,0,1],[1,1,0]]

def PrintMacierzSąsiedztwa(MacierzSąsiedztwa):
    RowList=list(range(1,len(MacierzSąsiedztwa)+1))
    N = len(MacierzSąsiedztwa)
    print(" ",RowList)
    for i in range(N):
        print(i+1,MacierzSąsiedztwa[i])
    print("")

def ClearData():
    global Macierz1, Macierz2
    Macierz1=[]
    Macierz2=[]

def GenerateGraph(MacierzSąsiedztwa,N,G): #który obiekt, po ile wierzchołków, gęstość
    for y in range(N):
        MacierzSąsiedztwa.append([0]*N)

    ToDell = math.trunc(N*(N-1)/2*G)
    
    for Y in range(n):
        for X in range(Y+1,n):
            MacierzSąsiedztwa[Y][X]=1 #1 is conection from Row to Column
            MacierzSąsiedztwa[X][Y]=1 
    
    while ToDell > 0:
        Y = random.randint(0,N-1)
        if (MacierzSąsiedztwa[Y].count(1) > 1):
            while True:
                IntToDel=random.randint(0,N-1)
                if(MacierzSąsiedztwa[Y][IntToDel]==1):
                    break
            
            MacierzSąsiedztwa[Y][IntToDel]=0
            MacierzSąsiedztwa[IntToDel][Y]=0
            ToDell-=1   
    
    Nieparzyste=[]
    for y in range(n):
        if (MacierzSąsiedztwa[y].count(1))%2 == 1:
            Nieparzyste.append(y)

    while len(Nieparzyste)>2:
        Y=Nieparzyste[(random.randint(0,len(Nieparzyste)-1))]
        X=Nieparzyste[(random.randint(0,len(Nieparzyste)-1))]
        if X!=Y and MacierzSąsiedztwa[X][Y]==0:
            MacierzSąsiedztwa[X][Y]=1
            MacierzSąsiedztwa[Y][X]=1
            Nieparzyste.remove(Y)
            Nieparzyste.remove(X)

def CyklHamiltonaMain(MacierzSąsiedztwa):
    V=[]
    def CyklHamiltonaSub(MacierzSąsiedztwa,v):
        V.append(v)










for i in range(1): #powtarzanie dla średnich
    if __name__ == "__main__":
        
        for n in range(6,7):

            GenerateGraph(Macierz1,n,0.3) #0.3 == 30% 
            PrintMacierzSąsiedztwa(Macierz1)

##########TODO##########################
##Cykl Hamiltona Checker i zatynm do generatora 
##Cykl Eulera Checker 
##Main Macierz1 = 30% Macierz2 =70%
##Hamilton z powtarzaniem dla Macierzy1 = 50% ale to drugim pliku IMO
##Pomiary w środe rano może bo czasu w huj

            ClearData()