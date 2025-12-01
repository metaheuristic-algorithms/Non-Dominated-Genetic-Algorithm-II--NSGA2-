import numpy as np

class Individual:
    def __init__(self):
        self.position = None
        self.objectives = []
        self.constraints = []
        self.constraint_violation = 0.0
        self.rank = 0
        self.crowding_distance = 0.0
        self.domination_set = []
        self.dominated_count = 0
        