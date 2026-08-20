from collections import deque

graph = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'],
    'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E'],
}

def bfs(graph , start , goal):
    visited = {start}
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(path + [nbr])
    return None

print(bfs(graph, "A" , "F"))




def dfs (graph , start , goal , visited = None , path = None):
    if visited is None:
        visited = set()
        path = [start]
    visited.add(start)

    if start == goal :
        return path
    for nbr in graph[start]:
        if nbr not in visited:
            result = dfs (graph , nbr , goal , visited , path + [nbr])
            if result :
                return result
    return None

print(dfs(graph, "A" , "F"))