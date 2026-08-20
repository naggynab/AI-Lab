import heapq

graph = {
    'Arad': {'Sibiu': 140},
    'Sibiu': {'Arad': 140,  'Fagaras': 99, 'RimnicuVilcea': 80},
    'RimnicuVilcea': {'Sibiu': 80, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'RimnicuVilcea': 97, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101},
}
heuristic = {'Arad': 366, 'Sibiu': 253, 'RimnicuVilcea': 193,
             'Fagaras': 176, 'Pitesti': 100, 'Bucharest': 0}

def a_star(graph , start , goal , h):
    pq = [(h[start] , 0 , start , [start])]
    visited = set()

    while pq:
        f,g,node, path = heapq.heappop(pq)
        if node in visited: continue
        visited.add(node)
        if node == goal:
            return path , g
        for nbr , cost in graph.get(node , {}).items():
            if nbr not in visited:
                new_g = g + cost
                heapq.heappush(pq , (new_g + h[nbr] , new_g , nbr , path + [nbr]) )

    return None , float('inf')

print(a_star(graph, 'Arad', 'Bucharest', heuristic))

def greedy(graph , start , goal , h):
    pq = [(h[start] , start , [start])]
    visited = set ()

    while pq:
        hval , node , path = heapq.heappop(pq)
        if node in visited: continue
        if node == goal:
            return path 
        for nbr , cost in graph.get(node , {}).items():
            if nbr not in visited:
                heapq.heappush(pq , (h[nbr] , nbr , path + [nbr]))

    return None

print(greedy(graph, 'Arad', 'Bucharest', heuristic))
