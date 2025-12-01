import numpy as np
import math

def evaluate_objectives(x, problem_name):
    """
    Evaluates objectives and constraints.
    Returns: objectives (list/array), cv (float - sum of constraint violations)
    """
    name = problem_name.lower()
    objectives = []
    cv = 0.0
    
    if name == 'zdt1':
        f1 = x[0]
        g = 1 + 9 * np.sum(x[1:]) / (len(x) - 1)
        h = 1 - np.sqrt(f1 / g)
        f2 = g * h
        objectives = [f1, f2]
        cv = 0.0

    elif name == 'zdt3':
        f1 = x[0]
        g = 1 + 9 * np.sum(x[1:]) / (len(x) - 1)
        h = 1 - np.sqrt(f1 / g) - (f1 / g) * np.sin(10 * np.pi * f1)
        f2 = g * h
        objectives = [f1, f2]
        cv = 0.0

    elif name == 'kursawe':
        f1 = 0.0
        f2 = 0.0
        # f1 calculation
        for i in range(len(x) - 1):
            f1 -= 10 * np.exp(-0.2 * np.sqrt(x[i]**2 + x[i+1]**2))
        # f2 calculation
        for i in range(len(x)):
            f2 += abs(x[i])**0.8 + 5 * np.sin(x[i]**3)
        objectives = [f1, f2]
        cv = 0.0

    elif name == 'fonseca':
        n = len(x)
        s1 = np.sum((x - 1/np.sqrt(n))**2)
        s2 = np.sum((x + 1/np.sqrt(n))**2)
        f1 = 1 - np.exp(-s1)
        f2 = 1 - np.exp(-s2)
        objectives = [f1, f2]
        cv = 0.0

    elif name == 'schaffer1':
        f1 = x[0]**2
        f2 = (x[0] - 2)**2
        objectives = [f1, f2]
        cv = 0.0

    elif name == 'schaffer2':
        x1 = x[0]
        if x1 <= 1:
            f1 = -x1
        elif 1 < x1 <= 3:
            f1 = x1 - 2
        elif 3 < x1 <= 4:
            f1 = 4 - x1
        else:
            f1 = x1 - 4
        f2 = (x1 - 5)**2
        objectives = [f1, f2]
        cv = 0.0

    elif name == 'binhkorn':
        f1 = 4*x[0]**2 + 4*x[1]**2
        f2 = (x[0] - 5)**2 + (x[1] - 5)**2
        
        g1 = (x[0] - 5)**2 + x[1]**2 - 25
        g2 = 7.7 - ((x[0] - 8)**2 + (x[1] + 3)**2)
        
        # Calculate Constraint Violation
        cv = max(0, g1) + max(0, g2)
        objectives = [f1, f2]

    elif name == 'chankonghaimes':
        f1 = 2 + (x[0] - 2)**2 + (x[1] - 1)**2
        f2 = 9*x[0] - (x[1] - 1)**2
        
        g1 = x[0]**2 + x[1]**2 - 225
        g2 = x[0] - 3*x[1] + 10
        
        cv = max(0, g1) + max(0, g2)
        objectives = [f1, f2]
        
    else:
        raise ValueError("Unknown problem")

    return objectives, cv