import random
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

def find_euler_cycle(adj_matrix):
    # Initialize variables
    num_vertices = len(adj_matrix)
    euler_cycle = []
    stack = [0]  # Start from vertex 0
    current_vertex = 0

    while stack:
        if any(adj_matrix[current_vertex]):
            # Find an unvisited neighbor of the current vertex
            for neighbor in range(num_vertices):
                if adj_matrix[current_vertex][neighbor] == 1:
                    # Add the current vertex to the stack
                    stack.append(current_vertex)
                    # Remove the edge between current vertex and neighbor
                    adj_matrix[current_vertex][neighbor] = 0
                    adj_matrix[neighbor][current_vertex] = 0
                    # Move to the neighbor
                    current_vertex = neighbor
                    break
        else:
            # Backtrack to the previous vertex
            euler_cycle.append(current_vertex)
            current_vertex = stack.pop()

    # Add the last vertex to complete the cycle
    euler_cycle.append(current_vertex)
    euler_cycle.reverse()  # Reverse to get the correct order

    return euler_cycle


Macierz=[]

GenerateGraph(Macierz,200,0.3) #0.35 == 35%  !!!!!!!!!!!! 1 nie działa !!!!!!!!!!!!!!!!!!!!!!!
#PrintMacierzSąsiedztwa(Macierz)
print("H")

EulerReady(Macierz)
print("H2")

PrintCykl(find_euler_cycle(Macierz))

print("H3")
