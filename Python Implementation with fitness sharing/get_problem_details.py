import numpy as np

def get_problem_details(problem_name):
    """
    Returns n_var, var_min, var_max based on the problem name.
    """
    name = problem_name.lower()
    
    if name == 'zdt1':
        n_var = 30
        var_min = np.zeros(n_var)
        var_max = np.ones(n_var)
        
    elif name == 'zdt3':
        n_var = 30
        var_min = np.zeros(n_var)
        var_max = np.ones(n_var)
        
    elif name == 'kursawe':
        n_var = 3
        var_min = -5 * np.ones(n_var)
        var_max = 5 * np.ones(n_var)
        
    elif name == 'fonseca':
        n_var = 3
        var_min = -4 * np.ones(n_var)
        var_max = 4 * np.ones(n_var)
        
    elif name == 'schaffer1':
        n_var = 1
        var_min = np.array([-100.0])
        var_max = np.array([100.0])
        
    elif name == 'schaffer2':
        n_var = 1
        var_min = np.array([-5.0])
        var_max = np.array([10.0])
        
    elif name == 'binhkorn':
        n_var = 2
        var_min = np.array([0.0, 0.0])
        var_max = np.array([5.0, 3.0])
        
    elif name == 'chankonghaimes':
        n_var = 2
        var_min = np.array([-20.0, -20.0])
        var_max = np.array([20.0, 20.0])
        
    else:
        raise ValueError(f"Unknown problem: {problem_name}")
        
    return n_var, var_min, var_max