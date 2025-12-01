import numpy as np
import matplotlib.pyplot as plt
from individual import Individual
from get_problem_details import get_problem_details
from evaluate_objectives import evaluate_objectives
from non_dominated_sort import non_dominated_sort

# Import Hybrid Diversity Components
from crowding_distance import calculate_crowding_distance 
from fitness_share import calculate_fitness_sharing 
from tournament_selection import tournament_selection
from genetic_operators import genetic_operators

# ---------------- CONFIGURATION ----------------
# List of all problems to run
ALL_PROBLEMS = [
    'ZDT1', 'ZDT3', 'Kursawe', 'Fonseca', 
    'Schaffer1', 'Schaffer2', 'BinhKorn', 'ChankongHaimes'
]

N_POP = 50
MAX_IT = 100
PC = 0.9      # Crossover Prob
ETA_C = 15    # Crossover Distribution Index
ETA_M = 20    # Mutation Distribution Index

# ---------------- SINGLE-PROBLEM RUN SETUP ----------------

PROBLEM_NAME = ALL_PROBLEMS[6] # Select the problem to run

# --- START NEW FIGURE FOR THE PROBLEM ---
plt.figure(figsize=(7, 5)) 

print(f"\n--- Starting NSGA-II (Hybrid Diversity) for problem: {PROBLEM_NAME} ---")

# Get problem details
n_var, var_min, var_max = get_problem_details(PROBLEM_NAME)
PM = 1.0 / n_var

# Initialize Population
pop = []
for _ in range(N_POP):
    ind = Individual()
    ind.position = np.random.uniform(var_min, var_max)
    ind.objectives, ind.constraint_violation = evaluate_objectives(ind.position, PROBLEM_NAME)
    pop.append(ind)

# Initial Sort and Diversity Calculation (Calculate BOTH metrics)
pop, fronts = non_dominated_sort(pop)
pop, fronts = calculate_crowding_distance(pop, fronts)
pop = calculate_fitness_sharing(pop)

# ---------------- MAIN LOOP ----------------
for it in range(MAX_IT):
    
    # Create Offspring using the hybrid tournament selection
    offspring_pop = []
    while len(offspring_pop) < N_POP:
        p1 = tournament_selection(pop)
        p2 = tournament_selection(pop)
        
        c1_pos, c2_pos = genetic_operators(p1.position, p2.position, var_min, var_max, PC, ETA_C, PM, ETA_M)
        
        child1 = Individual()
        child1.position = c1_pos
        child1.objectives, child1.constraint_violation = evaluate_objectives(c1_pos, PROBLEM_NAME)
        offspring_pop.append(child1)
        
        if len(offspring_pop) < N_POP:
            child2 = Individual()
            child2.position = c2_pos
            child2.objectives, child2.constraint_violation = evaluate_objectives(c2_pos, PROBLEM_NAME)
            offspring_pop.append(child2)

    # Merge Populations
    combined_pop = pop + offspring_pop
    
    # Sort Combined Population
    combined_pop, fronts = non_dominated_sort(combined_pop)
    
    # Calculate BOTH metrics on the new population
    combined_pop, fronts = calculate_crowding_distance(combined_pop, fronts)
    combined_pop = calculate_fitness_sharing(combined_pop)
    
    # Survival Selection (Elitism)
    new_pop = []
    front_idx = 0
    
    while len(new_pop) < N_POP:
        front = fronts[front_idx]
        
        if len(new_pop) + len(front) <= N_POP:
            new_pop.extend(front)
        else:
            # --- HYBRID SURVIVAL SELECTION LOGIC for the boundary front ---
            
            # Check if this front is Rank 1 and it's the boundary front being trimmed
            if front_idx == 0: 
                # Use Crowding Distance (Higher CD is better for trimming the Pareto front)
                front.sort(key=lambda x: x.crowding_distance, reverse=True) 
            else:
                # Use Shared Fitness (Lower Niche Count is better for trimming deep fronts)
                front.sort(key=lambda x: x.shared_fitness, reverse=False) 

            needed = N_POP - len(new_pop)
            new_pop.extend(front[:needed])
            
        front_idx += 1
        
    pop = new_pop
    
    # Re-sort and recalculate for the next iteration
    pop, fronts = non_dominated_sort(pop)
    pop, fronts = calculate_crowding_distance(pop, fronts)
    pop = calculate_fitness_sharing(pop)

# ---------------- VISUALIZATION ----------------

pareto_front = [ind for ind in pop if ind.rank == 1]
f1_vals = [ind.objectives[0] for ind in pareto_front]
f2_vals = [ind.objectives[1] for ind in pareto_front]

# Plotting on the current figure context
plt.scatter(f1_vals, f2_vals, c='red', marker='o', s=10)
plt.title(f'Hybrid Front - {PROBLEM_NAME}', fontsize=12)
plt.xlabel(r'$f_1(\mathbf{x})$', fontsize=10)
plt.ylabel(r'$f_2(\mathbf{x})$', fontsize=10)
plt.grid(True, linestyle='--')

# Custom axes settings for ChankongHaimes
if PROBLEM_NAME == 'ChankongHaimes':
    plt.xlim(0, 250)
    plt.ylim(-250, 0)
    plt.xticks(np.arange(0, 251, 50))
    plt.yticks(np.arange(-250, 1, 50))

print(f"--- Optimization Finished for {PROBLEM_NAME} ---")

# --- SHOW THE RESULT ---
plt.tight_layout()
plt.show()