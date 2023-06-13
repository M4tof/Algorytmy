Macierz=[]

file=open("dane.txt")
File=file.readlines()
file.close()
for i in File:
    i=list(map(int,i.strip().split()))
    Macierz.append(i)

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

def isSafe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False
    for i in range(pos):
        if path[i] == v:
            return False
    return True

hasCycle = False

def MultiCyklHamiltona(graph):
    global hasCycle
    hasCycle = False
    path = []
    path.append(0)
    visited = [False] * len(graph)
    for i in range(len(visited)):
        visited[i] = False
    visited[0] = True
    FindHamCycle(graph, 1, path, visited)
    if hasCycle:
        print("No Hamiltonian Cycle possible")
        return

def FindHamCycle(graph, pos, path, visited):
    if pos == len(graph):
        if graph[path[-1]][path[0]] != 0:
            path.append(0)
            #for i in range(len(path)):
            #    print(path[i], end=" ")
            
            PrintCykl(path)
            #print()
            
            path.pop()
            hasCycle = True
        return
    for v in range(len(graph)):
        if isSafe(v, graph, path, pos) and not visited[v]:
            path.append(v)
            visited[v] = True
            FindHamCycle(graph, pos + 1, path, visited)
            visited[v] = False
            path.pop()

def NewEulerMain(Macierz):
    M=([0,1,2,3,1,4,3,5,4,2,0])

    return(M)

def CyklHamiltonaMain(Macierz):
    V = []
    n = len(Macierz)

    def NewHamiltonianSub(v):
        V.append(v)
        if len(V) == n:
            if Macierz[v][I] == 1:
                V.append(I)
                return V  # Return the Hamiltonian cycle path
        for w in range(n):
            if w not in V and Macierz[w][v] == 1:
                result = NewHamiltonianSub(w)
                if result is not None:
                    return result
        V.remove(v)
        return None  # Return None if no Hamiltonian cycle is found

    I = 0
    return NewHamiltonianSub(I)

#################################################
# print("Maciorka: ")
# PrintMacierzSąsiedztwa(Macierz)
# print()

# print("Pierwszy Cykl Hamiltona: ")
# PrintCykl(CyklHamiltonaMain(Macierz))
# print()

print("Wszystkie Cykle Hamiltona: ")
MultiCyklHamiltona(Macierz)
print()

print("Cykl Eulera: ")
PrintCykl(NewEulerMain(Macierz))