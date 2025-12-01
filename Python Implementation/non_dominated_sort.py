from check_dominance_logic import check_dominance

def non_dominated_sort(population):
    """
    Performs Fast Non-Dominated Sorting.
    Returns:
        population: Updated with Rank and Domination stats
        fronts: List of lists, where fronts[0] is the first front (Rank 1)
    """
    
    fronts = [[]]
    
    for p in population:
        p.domination_set = []
        p.dominated_count = 0
        
        for q in population:
            if p == q:
                continue
            
            if check_dominance(p, q):
                p.domination_set.append(q)
            elif check_dominance(q, p):
                p.dominated_count += 1
        
        if p.dominated_count == 0:
            p.rank = 1
            fronts[0].append(p)
            
    i = 0
    while len(fronts[i]) > 0:
        next_front = []
        for p in fronts[i]:
            for q in p.domination_set:
                q.dominated_count -= 1
                if q.dominated_count == 0:
                    q.rank = i + 2 # Ranks are 1-based
                    next_front.append(q)
        i += 1
        if len(next_front) > 0:
            fronts.append(next_front)
        else:
            break
            
    return population, fronts