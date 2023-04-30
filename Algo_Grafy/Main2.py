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

def TarjanaMacierz(Row,N): #TarjanaMacierz(1,1)
    global MacierzSąsiedztwa,SzareM,CzarneM
    SzareM.append(Row+1)
    for i in range(N):
        if MacierzSąsiedztwa[Row][i]==1 and (i+1 not in SzareM) and (i+1 not in CzarneM):
            TarjanaMacierz(i,N)
    CzarneM.append(Row+1)

def TarjanaLista(Row):
    global ListaIncydencji,SzareL,CzarneL
    SzareL.append(ListaIncydencji[Row][0])
    for i in range(1,len(ListaIncydencji[Row])):
        if (ListaIncydencji[Row][i] not in SzareL) and (ListaIncydencji[Row][i] not in CzarneL):
            Poz = ListaIncydencji[Row][i] -1
            TarjanaLista(Poz)
    CzarneL.append(ListaIncydencji[Row][0])



def main():
    global MacierzSąsiedztwa, RowList, ListaIncydencji,CzarneM,SzareM,CzarneL,SzareL
    
    
    for N in range(1,16):
        
        print("DAG done "+str(N))
        N=N*200
        
        DAGen(N)
        
        #PrintMacierzSąsiedztwa() #1 from R to C , 2 from C to R
    
        Macierz2Lista()
        
        #PrintListaIncydencji()

        File.write(str(N)+"M,")
        print("Time start")
        startTime = time.time()
        
        k=0
        while len(CzarneM)!=len(RowList):
            TarjanaMacierz(k,N)
            k+=1
        CzarneM=CzarneM[::-1]
        
        #print(CzarneM)
        
        endTime= time.time()    #time at end #NANO MACHINES SON !
        totalTime= endTime - startTime  #run time

        File.write(str(totalTime)+"\n")
        
        print("Time end")

        print("Time 2 start")
        File.write(str(N)+"L,")
        startTime = time.time()
        
        k=0
        while len(CzarneL)!=len(RowList):
            TarjanaLista(k)
            k+=1
        CzarneL=CzarneL[::-1]
        
        #print(CzarneL)
        
        endTime= time.time()    #time at end #NANO MACHINES SON !
        totalTime= endTime - startTime  #run time

        File.write(str(totalTime)+"\n")
        
        print("Time 2 end")


        ClearData()
    
    


#############DO #########################
File = open("./wyniki2.txt","a")
main()
File.close()