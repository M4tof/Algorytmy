import math
import time
import sys
import random

sys.setrecursionlimit(2000000)
MacierzSąsiedztwa=[]    
RowList=[]
ListaIncydencji=[]
SzareM=[]
CzarneM=[]
SzareL=[]
CzarneL=[]

def DAGen(N,G):
    global MacierzSąsiedztwa, RowList
    for y in range(N):
        MacierzSąsiedztwa.append([0]*N)
        
    for inte in range(1,N+1):
        RowList.append(inte)
        
    for Y in range(N):
        for X in range(Y+1,N):
            MacierzSąsiedztwa[Y][X]=1 #1 is conection from Row to Column
            MacierzSąsiedztwa[X][Y]=-1 #2 is conection from Column to Row

    Full = N*(N-1)/2
    ToDell = math.trunc(Full*G)

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

def Macierz2Lista():
    global MacierzSąsiedztwa
    for n in range(len(MacierzSąsiedztwa)):
        TempList=[n+1]
        for Xn in range(len(MacierzSąsiedztwa[0])):
            if MacierzSąsiedztwa[n][Xn]>0:
                TempList.append([Xn+1,MacierzSąsiedztwa[n][Xn]])
        ListaIncydencji.append(TempList)

def PrintListaIncydencji():
    global ListaIncydencji
    for i in range(len(ListaIncydencji)):
        print(ListaIncydencji[i])
    print("")

def PrintMacierzSąsiedztwa():
    global MacierzSąsiedztwa, RowList
    N = len(MacierzSąsiedztwa)
    print(" ",RowList)
    for i in range(N):
        print(i+1,MacierzSąsiedztwa[i])
    print("")

def ClearData():
    global MacierzSąsiedztwa, RowList, ListaIncydencji, CzarneM, SzareM,CzarneL,SzareL
    MacierzSąsiedztwa=[]
    ListaIncydencji=[]
    RowList=[]
    SzareM=[]
    CzarneM=[]
    SzareL=[]
    CzarneL=[]


def Wagi():
    global MacierzSąsiedztwa
    n=len(MacierzSąsiedztwa)
    for Y in range(n):
        for X in range(Y,n):
            if MacierzSąsiedztwa[Y][X]!=0:
                R=random.randint(1,1001)
                MacierzSąsiedztwa[Y][X]=R
                MacierzSąsiedztwa[X][Y]=R

def PrimaMacierz():
    global MacierzSąsiedztwa
    
    n = len(MacierzSąsiedztwa)
    Tv=[0]
    T=[]
    while len(T)< n-1:
        min_weight = 10000
        x=0
        y=0
        for u in range(n):
            if u in Tv:
                for v in range(n):
                    if (v not in Tv):
                        if (MacierzSąsiedztwa[u][v]>0) and (MacierzSąsiedztwa[u][v] < min_weight):
                            min_weight=MacierzSąsiedztwa[u][v]
                            min_edge=[u,v]
                            vp=v
            
        if min_edge != None:
            Tv.append(vp)
            T.append(min_edge)
    #print(T) #Print the MST


def PrimaLista():
    global ListaIncydencji

    n=len(ListaIncydencji)
    Tv=[0]
    T=[]
    while len(T)< n-1:
        min_weight = 10000
        min_edge = None
        x=0
        y=0
        for u in range(n):
            if u in Tv:
                for v in range(1,len(ListaIncydencji[u])):
                    if ListaIncydencji[u][v][0] -1 not in Tv:
                        if ListaIncydencji[u][v][1] < min_weight:
                            vp = (ListaIncydencji[u][v][0]) - 1
                            min_weight = ListaIncydencji[u][v][1]
                            min_edge = [u,vp]
        
        if min_edge != None:
            Tv.append(vp)
            T.append(min_edge)
    
    #print(T)
        

def main():
    global MacierzSąsiedztwa, RowList, ListaIncydencji,CzarneM,SzareM,CzarneL,SzareL
    
    
    for N in range(1,16):
        
        DAGen(N,0.7)
        Wagi()

        Macierz2Lista()
        
        PrimaMacierz()
        
        PrimaLista()

        ClearData()
    
    


#############DO #########################

main()