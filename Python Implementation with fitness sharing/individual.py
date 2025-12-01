import numpy as np

class Individual:
    """
    Represents an individual solution in the population.
    Includes fields for decision variables, objectives, constraints, 
    non-dominated sorting rank, and both diversity metrics.
    """
    def __init__(self):
        self.position = None              # Decision variables (numpy array)
        self.objectives = []              # Objective values (list/numpy array)
        self.constraints = []             # Constraint values (list)
        self.constraint_violation = 0.0   # Total sum of positive constraint violations
        self.rank = 0                     # Non-dominated Rank (1 is best)
        
        # NSGA-II Diversity Metric
        self.crowding_distance = 0.0      # Crowding Distance (Higher is better)
        
        # Fitness Sharing Diversity Metric (Niche Count)
        self.shared_fitness = 0.0         # Niche Count (Lower is better)
        
        self.domination_set = []          # Indices of individuals this one dominates
        self.dominated_count = 0          # Number of individuals that dominate this one