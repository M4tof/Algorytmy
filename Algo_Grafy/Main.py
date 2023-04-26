import math
import random

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

def Macierz2Lista():
    global MacierzSąsiedztwa
    for n in range(len(MacierzSąsiedztwa)):
        TempList=[n+1]
        for Xn in range(len(MacierzSąsiedztwa[0])):
            if MacierzSąsiedztwa[n][Xn]==1:
                TempList.append(Xn+1)
        ListaIncydencji.append(TempList)

def PrintListaIncydencji():
    global ListaIncydencji
    for i in range(len(ListaIncydencji)):
        print(ListaIncydencji[i])

def PrintMacierzSąsiedztwa():
    global MacierzSąsiedztwa, RowList
    N = len(MacierzSąsiedztwa)
    print(" ",RowList)
    for i in range(N):
        print(i+1,MacierzSąsiedztwa[i])

def ClearData():
    global MacierzSąsiedztwa, RowList, ListaIncydencji
    MacierzSąsiedztwa=[]
    ListaIncydencji=[]
    RowList=[]

def main():
    global MacierzSąsiedztwa, RowList, ListaIncydencji
    for N in range(3,6):
        DAGen(N)
        PrintMacierzSąsiedztwa() #1 from R to C , 2 from C to R
    
        Macierz2Lista()
        print("")
        PrintListaIncydencji()

        ClearData()
        print("")




main()