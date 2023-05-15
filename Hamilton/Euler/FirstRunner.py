import math
import time
import sys
import random

sys.setrecursionlimit(2000000)

def PrintMacierzSąsiedztwa(MacierzSąsiedztwa):
    RowList=list(range(1,len(MacierzSąsiedztwa)+1))
    N = len(MacierzSąsiedztwa)
    print(" ",RowList)
    for i in range(N):
        print(i+1,MacierzSąsiedztwa[i])
    print("")

def PrintCykl(Cykl):
    a=Cykl.copy()
    for i in range (len(Cykl)):
        a[i]=a[i]+1
    print(a)

def GenerateGraph(MacierzSąsiedztwa,N,G): #który obiekt, po ile wierzchołków, gęstość
    for y in range(N):
        MacierzSąsiedztwa.append([0]*N)
    
    for Y in range(N):
        for X in range(Y+1,N):
            MacierzSąsiedztwa[Y][X]=1 #1 is conection from Row to Column
            MacierzSąsiedztwa[X][Y]=-1
    
    ToDell = N*(N-1)/2
    ToDell = math.trunc(ToDell*(1-G))

    while ToDell > 0:
        Y = random.randint(0,N-1)
        if (MacierzSąsiedztwa[Y].count(1) > 1):
            
            while True:
                IntToDel=random.randint(Y+1,N-1)
                if(MacierzSąsiedztwa[Y][IntToDel]==1):
                    break

            MacierzSąsiedztwa[Y][IntToDel]=0
            MacierzSąsiedztwa[IntToDel][Y]=0
            ToDell-=1    

def EulerReady(MacierzSąsiedztwa):
    Nieparzyste=[]
    n=len(MacierzSąsiedztwa)
    for y in range(n):
        for x in range(n):
            if MacierzSąsiedztwa[y][x]==-1:
                MacierzSąsiedztwa[y][x]=1
    
    for y in range(n):
        if (MacierzSąsiedztwa[y].count(1))%2 == 1:
            Nieparzyste.append(y)
    
    while len(Nieparzyste)>2:
        Y=Nieparzyste[0]
        for X in Nieparzyste:
            if X!=Y and MacierzSąsiedztwa[X][Y]==0:
                MacierzSąsiedztwa[X][Y]=1
                MacierzSąsiedztwa[Y][X]=1
                Nieparzyste.remove(Nieparzyste[0])
                Nieparzyste.remove(X)
    


def CyklHamiltonaMain(Macierz):
    V=[]
    n=len(Macierz)

    def NewHamiltionianSub(v):
        V.append(v)
        for w in range(0,n):
            if (w not in V) and (Macierz[w][v]==1):
                NewHamiltionianSub(w)
        if (len(V)==(n)):
            if(Macierz[v][I]==1):
                return True
        else:
            V.remove(v)
    
    I=0
    NewHamiltionianSub(I)

    V.append(I)
    return V

def CyklEuleraMain(MacierzSąsiedztwa,v):
    Cykl=[]
    Zwiedzone=[]

    def CyklEuleraSub(MacierzSąsiedztwa,v):
        for w in range(len(MacierzSąsiedztwa)):
            if ([v,w] not in Zwiedzone) and ([w,v] not in Zwiedzone) and (MacierzSąsiedztwa[v][w]==1):
                Zwiedzone.append([v,w])
                
                CyklEuleraSub(MacierzSąsiedztwa,w)
        Cykl.append(v)

    CyklEuleraSub(MacierzSąsiedztwa,v)
    
    return(Cykl)

def NewEulerMain(Macierz):
    C=[]
    n=len(Macierz)

    def NewEuler(v):
        for u in range(n):
            if Macierz[u][v]==1:
                Macierz[u][v]=0
                Macierz[v][u]=0
                NewEuler(u)
        C.append(v)
    
    NewEuler(0)
    return C



for i in range(1):
    
    if __name__ == "__main__":
        for n in range(1,2): #(1,16)
            Macierz1=[] 
            Macierz2=[]

            n=n*50
            
            g = 0.7
            GenerateGraph(Macierz1,n,g) #0.35 == 35%  !!!!!!!!!!!! 1 nie działa !!!!!!!!!!!!!!!!!!!!!!!
            EulerReady(Macierz1)

            GenerateGraph(Macierz2,n,g)
            EulerReady(Macierz2)
            
            #PrintMacierzSąsiedztwa(Macierz3)
            
            PrintCykl(NewEulerMain(Macierz1))
            PrintCykl(CyklHamiltonaMain(Macierz2))