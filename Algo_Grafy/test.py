import math

MacierzSąsiedztwa=[[0,1,2,0,2],[2,0,2,1,1],[1,1,0,2,0],[0,2,1,0,2],[1,2,0,1,0]]    
RowList=[1,2,3,4,5]
ListaIncydencji=[]

def Macierz2Lista(Macierz):
    for n in range(len(Macierz)):
        TempList=[n+1]
        for Xn in range(len(Macierz[0])):
            if Macierz[n][Xn]==1:
                TempList.append(Xn+1)
        ListaIncydencji.append(TempList)



Macierz2Lista(MacierzSąsiedztwa)
for i in range(len(ListaIncydencji)):
    print(ListaIncydencji[i])