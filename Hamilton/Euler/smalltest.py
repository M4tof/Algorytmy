import random
import math
import time
import sys
import random
sys.setrecursionlimit(2000000)


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
    

    PrintMacierzSąsiedztwa(MacierzSąsiedztwa)
    while len(Nieparzyste)>0:
        print(Nieparzyste)
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
                    if Y!=X and MacierzSąsiedztwa[Y][X]==1:
                        x=X
                        y=Y
                        control=1
            
            if control==0:
                MacierzSąsiedztwa[x][y]==1
                MacierzSąsiedztwa[y][x]==1
                Nieparzyste.remove(x)
                Nieparzyste.remove(y)
            else:
                MacierzSąsiedztwa[x][y]==0
                MacierzSąsiedztwa[y][x]==0
                Nieparzyste.remove(x)
                Nieparzyste.remove(y)

        elif len(Nieparzyste)==1:
            for Yy in range(n):
                MacierzSąsiedztwa[Yy][Nieparzyste[0]]==0
                MacierzSąsiedztwa[Nieparzyste[0]][Yy]==0
    

Macierz=[]

GenerateGraph(Macierz,10,0.3) #0.35 == 35%  !!!!!!!!!!!! 1 nie działa !!!!!!!!!!!!!!!!!!!!!!!
PrintMacierzSąsiedztwa(Macierz)
print("H")

EulerReady(Macierz)
PrintMacierzSąsiedztwa(Macierz)
print("H2")

print(find_eulerian_cycle(Macierz))
print("H3")

