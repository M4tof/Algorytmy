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

def find_eulerian_cycle(adj_matrix):
    """
    Finds an Eulerian cycle in an adjacency matrix.

    Args:
        adj_matrix: A square matrix representing the adjacency matrix of a graph.

    Returns:
        A list of vertices representing the Eulerian cycle, or None if no cycle exists.
    """
    n = len(adj_matrix)

    # Check if the graph is connected
    if not is_connected(adj_matrix):
        return None

    # Create a copy of the adjacency matrix to track edges
    edge_matrix = [[adj_matrix[i][j] for j in range(n)] for i in range(n)]

    # Start with an arbitrary vertex
    cycle = [0]  # Initialize the Eulerian cycle with the first vertex

    while True:
        current_vertex = cycle[-1]

        # Check if there are any unused edges from the current vertex
        if sum(edge_matrix[current_vertex]) == 0:
            # Check if all edges have been used
            if all(sum(row) == 0 for row in edge_matrix):
                return cycle  # Return the Eulerian cycle

            return None  # No Eulerian cycle exists

        # Find the next unvisited neighbor of the current vertex
        for next_vertex in range(n):
            if edge_matrix[current_vertex][next_vertex] == 1:
                # Remove the edge from the matrix
                edge_matrix[current_vertex][next_vertex] = 0
                edge_matrix[next_vertex][current_vertex] = 0

                # Add the next vertex to the cycle
                cycle.append(next_vertex)
                break

    return None  # No Eulerian cycle exists


def is_connected(adj_matrix):
    """
    Checks if an adjacency matrix represents a connected graph.

    Args:
        adj_matrix: A square matrix representing the adjacency matrix of a graph.

    Returns:
        True if the graph is connected, False otherwise.
    """
    n = len(adj_matrix)
    visited = [False] * n

    # Perform depth-first search (DFS) starting from the first vertex
    dfs(adj_matrix, 0, visited)

    # Check if all vertices were visited
    return all(visited)


def dfs(adj_matrix, vertex, visited):
    """
    Performs depth-first search (DFS) on a graph represented by an adjacency matrix.

    Args:
        adj_matrix: A square matrix representing the adjacency matrix of a graph.
        vertex: The current vertex.
        visited: A list of boolean values indicating whether a vertex has been visited.

    Returns:
        None
    """
    visited[vertex] = True

    # Visit all neighbors of the current vertex
    for neighbor in range(len(adj_matrix)):
        if adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
            dfs(adj_matrix, neighbor, visited)




for i in range(1):
    
    if __name__ == "__main__":
        for n in range(1,2): #(1,16)
            Macierz1=[] 
            Macierz2=[[0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

            x = 100
            
            n=n*x
            
            g = 0.35

            GenerateGraph(Macierz1,n,g) #0.35 == 35%  !!!!!!!!!!!! 1 nie działa !!!!!!!!!!!!!!!!!!!!!!!
            EulerReady(Macierz1)

            #GenerateGraph(Macierz2,n,g) #0.35 == 35%  !!!!!!!!!!!! 1 nie działa !!!!!!!!!!!!!!!!!!!!!!!
            #EulerReady(Macierz2)

            print("Generation done", n//x)

            #PrintCykl(NewEulerMain(Macierz1))
            PrintCykl(find_eulerian_cycle(Macierz1))
           
            #a = CyklHamiltonaMain(Macierz2)
