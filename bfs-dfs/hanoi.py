def tower_hanoi(n , source , aux , target , moves):
    if n == 1:
        moves.append(f" Move disk 1 from {source} to {target}")
        return
    tower_hanoi(n-1 , source , target , aux , moves)
    moves.append(f" Move disk {n} from {source} to {target}")
    tower_hanoi(n-1 , aux , source , target , moves )


moves = []
tower_hanoi(3 , 'A' , 'B' , 'C' , moves)
for m in moves:
    print(m)
print(len(moves))

def hanoi(n, source, aux, target, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, target, aux, moves)   # step 1: move N-1 out of the way
    moves.append(f"Move disk {n} from {source} to {target}")  # step 2: move the big one
    hanoi(n-1, aux, source, target, moves)   # step 3: move N-1 onto target

moves = []
hanoi(3, 'A', 'B', 'C', moves)
for m in moves:
    print(m)
print(f"Total moves: {len(moves)}")