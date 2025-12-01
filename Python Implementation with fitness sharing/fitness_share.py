import numpy as np

# Sensitivity parameters for the sharing function
SIGMA_SHARE = 0.5  # Niche radius (tunable)
ALPHA = 2.0        # Shape factor


def calculate_fitness_sharing(population):
    """
    Applies fitness sharing to population and stores a `shared_fitness` attribute
    on each individual (1 / (1 + niche_count)). Returns the population.
    """
    n = len(population)
    if n == 0:
        return population

    # Extract objective matrix
    objectives = np.array([ind.objectives for ind in population])

    # Normalize objectives
    f_min = objectives.min(axis=0)
    f_max = objectives.max(axis=0)
    ranges = f_max - f_min
    ranges[ranges == 0] = 1.0
    norm_obj = (objectives - f_min) / ranges

    for i in range(n):
        share_sum = 0.0
        for j in range(n):
            if i == j:
                continue
            d = np.linalg.norm(norm_obj[i] - norm_obj[j])
            if d < SIGMA_SHARE:
                share_sum += 1 - (d / SIGMA_SHARE) ** ALPHA
        population[i].shared_fitness = 1.0 / (1.0 + share_sum)

    return population