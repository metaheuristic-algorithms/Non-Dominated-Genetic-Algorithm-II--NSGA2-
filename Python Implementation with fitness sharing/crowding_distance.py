import numpy as np


def calculate_crowding_distance(population, fronts):
    """
    Calculate the crowding distance for individuals in each front.

    Args:
        population: list of Individual
        fronts: list of fronts (each a list of Individual)

    Returns:
        (population, fronts) with `crowding_distance` updated on individuals
    """

    # Reset distances
    for ind in population:
        ind.crowding_distance = 0.0

    for front in fronts:
        if len(front) == 0:
            continue

        n_obj = len(front[0].objectives)

        for m in range(n_obj):
            # Sort front based on objective m
            front.sort(key=lambda x: x.objectives[m])

            # Boundary points get infinite distance
            front[0].crowding_distance = float('inf')
            front[-1].crowding_distance = float('inf')

            # Objective range
            f_min = front[0].objectives[m]
            f_max = front[-1].objectives[m]

            if f_max == f_min:
                continue

            # Crowding distance for intermediate points
            for k in range(1, len(front) - 1):
                if front[k].crowding_distance != float('inf'):
                    dist = (front[k+1].objectives[m] - front[k-1].objectives[m]) / (f_max - f_min)
                    front[k].crowding_distance += dist

    return population, fronts