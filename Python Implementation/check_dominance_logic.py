def check_dominance(p, q):
    """
    Checks if Individual p dominates Individual q
    Logic: Constrained Dominance
    """
    
    # Case 1: Both are feasible
    if p.constraint_violation == 0 and q.constraint_violation == 0:
        # Standard Pareto Dominance
        # p dominates q if p is better or equal in all objectives 
        # AND strictly better in at least one
        p_obj = p.objectives
        q_obj = q.objectives
        
        better_or_equal = all(pv <= qv for pv, qv in zip(p_obj, q_obj))
        strictly_better = any(pv < qv for pv, qv in zip(p_obj, q_obj))
        
        return better_or_equal and strictly_better

    # Case 2: p is feasible, q is infeasible
    elif p.constraint_violation == 0 and q.constraint_violation > 0:
        return True

    # Case 3: p is infeasible, q is feasible
    elif p.constraint_violation > 0 and q.constraint_violation == 0:
        return False

    # Case 4: Both are infeasible
    else:
        # The one with less violation dominates
        return p.constraint_violation < q.constraint_violation