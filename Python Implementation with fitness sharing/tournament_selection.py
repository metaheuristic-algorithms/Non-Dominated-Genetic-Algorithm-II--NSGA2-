import random
from individual import Individual

def tournament_selection(population):
    """
    Binary Tournament Selection based on:
    1. Constrained Dominance Rank (always better).
    2. Hybrid Diversity Metric (if ranks are equal):
       - Rank 1: Crowding Distance (Higher is Better).
       - Rank > 1: Shared Fitness / Niche Count (Lower is Better).
    """
    n_pop = len(population)
    
    # Select 2 random individuals
    i = random.randint(0, n_pop - 1)
    j = random.randint(0, n_pop - 1)
    
    p1 = population[i]
    p2 = population[j]
    
    # 1. Compare Ranks (Lower is better)
    if p1.rank < p2.rank:
        return p1
    elif p2.rank < p1.rank:
        return p2
    else:
        # 2. Tie-Breaking: Use Hybrid Diversity Rule
        
        if p1.rank == 1:
            # Rank 1: Prioritize Crowding Distance (CD). Higher CD is better.
            if p1.crowding_distance > p2.crowding_distance:
                return p1
            else:
                return p2
        else:
            # Rank > 1: Prioritize Shared Fitness (FS). Lower Niche Count is better.
            if p1.shared_fitness < p2.shared_fitness:
                return p1
            else:
                return p2