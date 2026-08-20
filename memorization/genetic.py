import random 
random.seed(1)

target = 'HELLO'
genes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pop_size = 20 

def create_chromosomes():
    return [random.choice(genes) for _ in range(len(target))]

def fitness(chromo):
    return sum( 1 for g ,t in zip(chromo , target) if g == t)

def selection(pop):
    return sorted(pop , key = fitness , reverse=True)[: pop_size // 2]

def crossover(p1 , p2 ):
    point = random.randint(1, len(target) - 1)
    return p1[:point] + p2[point :] , p2[:point] + p1[point :]

def mutate (chrosome , rate = 0.5):
    return [random.choice(genes) if random.random() < rate else g for g in chrosome]

population = [create_chromosomes() for _ in range(pop_size) ]
gen = 0 

while True: 
    population = sorted (population , key = fitness , reverse= True)
    best = selection(population)
    if fitness(best) == len(target) or gen > 500:
        break
    parents = selection(population)
    next_gen = parents.copy()
    