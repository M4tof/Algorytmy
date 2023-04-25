import random
import math

N = 5

MacierzSąsiedztwa=[]
for y in range(N):
    MacierzSąsiedztwa.append([0]*N)
        
RowList=[]

for inte in range(1,N+1):
    RowList.append(inte)

def PrintMacierzSąsiedztwa():
    global MacierzSąsiedztwa, N, RowList
    print(" ",RowList)
    for i in range(N):
        print(i+1,MacierzSąsiedztwa[i])

PrintMacierzSąsiedztwa()
    
for Y in range(N):
    for X in range(Y+1,N):
        MacierzSąsiedztwa[Y][X]=1 #1 is conection from Row to Column
        MacierzSąsiedztwa[X][Y]=2 #2 is conection from Column to Row

print("")
PrintMacierzSąsiedztwa()

Full = N*(N-1)/2
ToDell = math.trunc(Full*0.4)

print("")
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


print("")
PrintMacierzSąsiedztwa()