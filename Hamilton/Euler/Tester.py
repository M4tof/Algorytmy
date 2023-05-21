import random
import math
import time
import sys
import random

sys.setrecursionlimit(9999999)




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
    
def euler(v, adj_matrix, euler_cycle):
    for w in range(len(adj_matrix)):
        if adj_matrix[v][w] == 1:
            adj_matrix[v][w] = 0  # Mark the edge as visited
            euler(w, adj_matrix, euler_cycle)

    euler_cycle.append(v)

def find_euler_cycle(adj_matrix):
    num_vertices = len(adj_matrix)
    euler_cycle = []
    euler(0, adj_matrix, euler_cycle)

    euler_cycle.reverse()  # Reverse to get the correct order

    return euler_cycle

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

def HamiltonReady(MacierzSąsiedztwa):
    n=len(MacierzSąsiedztwa)
    Kolej=list(range(n))
    random.shuffle(Kolej)
    
    while len(Kolej)>1:
        if MacierzSąsiedztwa[Kolej[0]][Kolej[1]]==0:
            MacierzSąsiedztwa[Kolej[0]][Kolej[1]]=1
            MacierzSąsiedztwa[Kolej[1]][Kolej[0]]=1
        Kolej.remove(Kolej[0])

def isSafe(v, graph, path, pos):
   
    # If the vertex is adjacent to
    # the vertex of the previously
    # added vertex
    if graph[path[pos - 1]][v] == 0:
        return False
 
    # If the vertex has already
    # been included in the path
    for i in range(pos):
        if path[i] == v:
            return False
 
    # Both the above conditions are
    # not true, return true
    return True
 
# To check if there exists
# at least 1 hamiltonian cycle
hasCycle = False
 
# Function to find all possible
# hamiltonian cycles
def hamCycle(graph):
    global hasCycle
     
    # Initially value of boolean
    # flag is false
    hasCycle = False
 
    # Store the resultant path
    path = []
    path.append(0)
 
    # Keeps the track of the
    # visited vertices
    visited = [False]*(len(graph))
 
    for i in range(len(visited)):
        visited[i] = False
 
    visited[0] = True
 
    # Function call to find all
    # hamiltonian cycles
    FindHamCycle(graph, 1, path, visited)
 
    if hasCycle:
        # If no Hamiltonian Cycle
        # is possible for the
        # given graph
        print("No Hamiltonian Cycle" + "possible ")
        return
 
# Recursive function to find all
# hamiltonian cycles
def FindHamCycle(graph, pos, path, visited):
   
    # If all vertices are included
    # in Hamiltonian Cycle
    if pos == len(graph):
       
        # If there is an edge
        # from the last vertex to
        # the source vertex
        if graph[path[-1]][path[0]] != 0:
           
            # Include source vertex
            # into the path and
            # print the path
            path.append(0)
            for i in range(len(path)):
                print(path[i], end = " ")
            print()
 
            # Remove the source
            # vertex added
            path.pop()
 
            # Update the hasCycle
            # as true
            hasCycle = True
        return
 
    # Try different vertices
    # as the next vertex
    for v in range(len(graph)):
       
        # Check if this vertex can
        # be added to Cycle
        if isSafe(v, graph, path, pos) and not visited[v]:
            path.append(v)
            visited[v] = True
 
            # Recur to construct
            # rest of the path
            FindHamCycle(graph, pos + 1, path, visited)
 
            # Remove current vertex
            # from path and process
            # other vertices
            visited[v] = False
            path.pop()
################################################################################################



file=open("wyniki.txt", "a")
for n in range(1,16):
    Macierz=[]
    
    n=n*1

    GenerateGraph(Macierz,n,0.3) #0.35 == 35%  !!!!!!!!!!!! 1 nie działa !!!!!!!!!!!!!!!!!!!!!!!
    #PrintMacierzSąsiedztwa(Macierz)
    print("H")
    HamiltonReady(Macierz)
    print("H2")

    startTime = time.time_ns()        
            
    #hamCycle(Macierz)
    CyklHamiltonaMain(Macierz)


    endTime= time.time_ns()    #time at end #NANO MACHINES SON !
    totalTime= endTime - startTime  #run time

    print(n,",",totalTime)  
    file.write((str(n)+","+str(totalTime)+"\n"))
    time.sleep(5)

file.close()