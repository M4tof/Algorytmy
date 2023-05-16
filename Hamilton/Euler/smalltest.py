import random
import math
import time
import sys
import random

sys.setrecursionlimit(2000000)

def generate_eulerian_graph(size, saturation):
    """
    Generates an adjacency matrix for a graph with an Eulerian cycle.

    Args:
        size: The size of the adjacency matrix (number of vertices).
        saturation: The saturation of the graph, represented as a decimal between 0 and 1.
                    A saturation of 1 corresponds to a complete graph, while 0 corresponds to no edges.

    Returns:
        The adjacency matrix representing the generated graph.
    """
    adjacency_matrix = [[0] * size for _ in range(size)]
    max_edges = size * (size - 1)  # Maximum number of edges in a directed graph

    num_edges = int(saturation * max_edges)
    edges_added = 0

    # Add edges to the graph until the desired number of edges is reached
    while edges_added < num_edges:
        src = random.randint(0, size - 1)
        dst = random.randint(0, size - 1)

        # Ensure the edge doesn't already exist and it's not a self-loop
        if adjacency_matrix[src][dst] == 0 and src != dst:
            adjacency_matrix[src][dst] = 1
            edges_added += 1

    return adjacency_matrix

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

def find_hamiltonian_cycle(adj_matrix):
    """
    Finds a Hamiltonian cycle in a graph represented by an adjacency matrix.

    Args:
        adj_matrix: The adjacency matrix of a graph.

    Returns:
        A list of vertices representing the Hamiltonian cycle, or an empty list if no cycle is found.
    """
    n = len(adj_matrix)
    visited = [False] * n
    path = []

    # Start from the first vertex
    path.append(0)
    visited[0] = True

    if find_hamiltonian_cycle_helper(adj_matrix, visited, path, 1):
        return path

    return []


def find_hamiltonian_cycle_helper(adj_matrix, visited, path, pos):
    """
    Helper function for finding a Hamiltonian cycle using backtracking.

    Args:
        adj_matrix: The adjacency matrix of a graph.
        visited: A list to track visited vertices.
        path: A list representing the current path.
        pos: The position in the path.

    Returns:
        True if a Hamiltonian cycle is found, False otherwise.
    """
    n = len(adj_matrix)

    # Base case: If all vertices are visited and the last vertex is connected to the first vertex
    if pos == n and adj_matrix[path[pos - 1]][path[0]] == 1:
        return True

    # Try different vertices as the next candidate in the path
    for v in range(1, n):
        if is_valid_next_vertex(v, adj_matrix, visited, path, pos):
            path[pos] = v
            visited[v] = True

            if find_hamiltonian_cycle_helper(adj_matrix, visited, path, pos + 1):
                return True

            # Backtrack if the current candidate does not lead to a Hamiltonian cycle
            path[pos] = -1
            visited[v] = False

    return False


def is_valid_next_vertex(v, adj_matrix, visited, path, pos):
    """
    Checks if a vertex v is a valid candidate for the next position in the Hamiltonian cycle.

    Args:
        v: The vertex to check.
        adj_matrix: The adjacency matrix of a graph.
        visited: A list to track visited vertices.
        path: A list representing the current path.
        pos: The current position in the path.

    Returns:
        True if the vertex is a valid candidate, False otherwise.
    """
    n = len(adj_matrix)

    # Check if the vertex is connected to the previous vertex in the path
    if adj_matrix[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been visited
    if visited[v]:
        return False

    return True

for i in range(1):
    matrix_size = 100
    saturation = 1

    adjacency_matrix = generate_eulerian_graph(matrix_size, saturation)
    adjacency_matrix2=adjacency_matrix.copy()

    eulerian_cycle = find_eulerian_cycle(adjacency_matrix)

    if eulerian_cycle is None:
        print("No Eulerian cycle exists.")
    else:
        print("Eulerian cycle:", eulerian_cycle)

    adjacency_matrix2=[[0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0]]
    hamiltonian_cycle = find_hamiltonian_cycle(adjacency_matrix2)

    if hamiltonian_cycle:
        print("Hamiltonian cycle found:", hamiltonian_cycle)
    else:
        print("No Hamiltonian cycle found.")
    