import random

def tournament_selection(population):
    """
    Binary Tournament Selection based on Rank and Crowding Distance.
    """
    n_pop = len(population)
    
    # Select 2 random indices
    i = random.randint(0, n_pop - 1)
    j = random.randint(0, n_pop - 1)
    
    p1 = population[i]
    p2 = population[j]
    
    # Compare Ranks (Lower is better)
    if p1.rank < p2.rank:
        return p1
    elif p2.rank < p1.rank:
        return p2
    else:
        # If Ranks are equal, compare Crowding Distance (Higher is better)
        if p1.crowding_distance > p2.crowding_distance:
            return p1
        else:
            return p2