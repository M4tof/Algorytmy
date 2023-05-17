import math
import time
import sys
import random
import multiprocessing

sys.setrecursionlimit(2000000000)

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
        
    while len(Nieparzyste)>0:
        
        #PrintMacierzSąsiedztwa(MacierzSąsiedztwa)
        #print(Nieparzyste)
        
        if len(Nieparzyste)>1:
            x='a'
            y='a'
            control=0
            for Y in Nieparzyste:
                for X in Nieparzyste:
                    if Y!=X and MacierzSąsiedztwa[Y][X]==0:
                        x=X
                        y=Y
                        control=0
                    elif Y!=X and MacierzSąsiedztwa[Y][X]==1:
                        x=X
                        y=Y
                        control=1
            
           # print(x,y,control)
            
            if control==0:
                MacierzSąsiedztwa[x][y]=1
                MacierzSąsiedztwa[y][x]=1
                Nieparzyste.remove(x)
                Nieparzyste.remove(y)
            else:
                MacierzSąsiedztwa[x][y]=0
                MacierzSąsiedztwa[y][x]=0
                Nieparzyste.remove(x)                           #1 2 3 4 6 9
                Nieparzyste.remove(y)

        elif len(Nieparzyste)==1:
            for Yy in range(n):
                MacierzSąsiedztwa[Yy][Nieparzyste[0]]=0
                MacierzSąsiedztwa[Nieparzyste[0]][Yy]=0


def HamiltonReady(MacierzSąsziedztwa):
    n= len(MacierzSąsziedztwa)
    for Y in range(n-1):
        if MacierzSąsziedztwa[Y][Y+1]==0:
            MacierzSąsziedztwa[Y][Y+1]=1
            MacierzSąsziedztwa[Y+1][Y]=1


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

def NewEulerMain(Macierz):
    M=Macierz.copy()
    C=[]
    n=len(Macierz)

    def NewEuler(v):
        for u in range(n):
            if M[u][v]==1:
                M[u][v]=0
                M[v][u]=0
                NewEuler(u)
        C.append(v)
    
    NewEuler(0)
    return C


def HamiltonReady(MacierzSąsiedztwa):
    n=len(MacierzSąsiedztwa)
    Kolej=list(range(n))
    random.shuffle(Kolej)
    
    while len(Kolej)>1:
        if MacierzSąsiedztwa[Kolej[0]][Kolej[1]]==0:
            MacierzSąsiedztwa[Kolej[0]][Kolej[1]]=1
            MacierzSąsiedztwa[Kolej[1]][Kolej[0]]=1
            Kolej.remove(Kolej[0])
    
    if len(Kolej)==1:






def run():
    g = 0.35
    Macierz1=[]

    x = 200
    n=x

    GenerateGraph(Macierz1,n,g) #0.35 == 35%  !!!!!!!!!!!! 1 nie działa !!!!!!!!!!!!!!!!!!!!!!!
    EulerReady(Macierz1)
    #HamiltonReady(Macierz1)

    print("Generation done", n//x)

    print(CyklHamiltonaMain(Macierz1))

    for i in range(len(Macierz1)):
        file.write(str(Macierz1[i])+"\n")
    

file=open("graf.txt", "w")

        

if __name__ == "__main__":
    for j in range(100):
        r = multiprocessing.Process(target=run)
        r.start()
        time.sleep((60))
        print("Times up")
        r.terminate()