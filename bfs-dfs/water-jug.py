from collections import deque

def bfs(cap1 , cap2 , goal ):
    start = (0,0)
    visited = {start}
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        x,y = path[-1]
        if x == goal or y == goal:
            return path
        d1 = min (x , cap2 - y) # jug 1 -> 2 
        d2 = min (y , cap1 - x) # jug 2 -> 1 
        next_states = [
            (cap1 , y),(x , cap2) , (0 , y) , (x , y),
            (x-d1 , y + d1 ) , (x+ d2 , y - d2)
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(path + [state])

    return None 


print(bfs (4,3,2))