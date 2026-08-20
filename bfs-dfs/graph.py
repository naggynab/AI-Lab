from collections import deque

graph = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'],
    'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E'],
}

def bfs(graph, start, goal):
    visited = {start}
    queue = deque([[start]])          # each item = a full path so far
    while queue:
        path = queue.popleft()        # FIFO: take from the FRONT
        node = path[-1]
        if node == goal:
            return path
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(path + [nbr])
    return None

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited, path = set(), [start]
    visited.add(start)
    if start == goal:
        return path
    for nbr in graph[start]:
        if nbr not in visited:
            result = dfs(graph, nbr, goal, visited, path + [nbr])
            if result:
                return result
    return None

print("BFS A->F:", bfs(graph, 'A', 'F'))   # ['A', 'C', 'F']
print("DFS A->F:", dfs(graph, 'A', 'F'))   # ['A', 'B', 'E', 'F']