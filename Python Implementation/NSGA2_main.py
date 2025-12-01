import numpy as np
import matplotlib.pyplot as plt
from individual import Individual
from get_problem_details import get_problem_details
from evaluate_objectives import evaluate_objectives
from non_dominated_sort import non_dominated_sort
from crowding_distance import calculate_crowding_distance
from tournament_selection import tournament_selection
from genetic_operators import genetic_operators


# ---------------- CONFIGURATION ----------------
# Choose problem: 'ZDT1','ZDT3','Kursawe','Fonseca','Schaffer1','Schaffer2','BinhKorn','ChankongHaimes'
PROBLEM_NAME = 'ZDT1'

N_POP = 50
MAX_IT = 50
PC = 0.9      # Crossover Prob
ETA_C = 15    # Crossover Distribution Index
ETA_M = 20    # Mutation Distribution Index

# ---------------- INITIALIZATION ----------------
print(f"Starting NSGA-II for problem: {PROBLEM_NAME}")

# Get problem details
n_var, var_min, var_max = get_problem_details(PROBLEM_NAME)
PM = 1.0 / n_var  # Mutation Prob

# Initialize Population
pop = []
for _ in range(N_POP):
    ind = Individual()
    # Random position within bounds
    ind.position = np.random.uniform(var_min, var_max)
    # Evaluate
    ind.objectives, ind.constraint_violation = evaluate_objectives(ind.position, PROBLEM_NAME)
    pop.append(ind)

# Initial Sort
pop, fronts = non_dominated_sort(pop)
pop, fronts = calculate_crowding_distance(pop, fronts)

# ---------------- MAIN LOOP ----------------
for it in range(MAX_IT):
    print(f"Iteration {it + 1}/{MAX_IT}")
    
    # Create Offspring
    offspring_pop = []
    while len(offspring_pop) < N_POP:
        p1 = tournament_selection(pop)
        p2 = tournament_selection(pop)
        
        c1_pos, c2_pos = genetic_operators(p1.position, p2.position, var_min, var_max, PC, ETA_C, PM, ETA_M)
        
        # Create Child 1
        child1 = Individual()
        child1.position = c1_pos
        child1.objectives, child1.constraint_violation = evaluate_objectives(c1_pos, PROBLEM_NAME)
        offspring_pop.append(child1)
        
        # Create Child 2 (if space permits)
        if len(offspring_pop) < N_POP:
            child2 = Individual()
            child2.position = c2_pos
            child2.objectives, child2.constraint_violation = evaluate_objectives(c2_pos, PROBLEM_NAME)
            offspring_pop.append(child2)

    # Merge Populations
    combined_pop = pop + offspring_pop
    
    # Sort Combined Population
    combined_pop, fronts = non_dominated_sort(combined_pop)
    combined_pop, fronts = calculate_crowding_distance(combined_pop, fronts)
    
    # Survival Selection (Elitism)
    new_pop = []
    front_idx = 0
    
    while len(new_pop) < N_POP:
        front = fronts[front_idx]
        
        if len(new_pop) + len(front) <= N_POP:
            # If whole front fits, take it
            new_pop.extend(front)
        else:
            # If front doesn't fit, sort by Crowding Distance and take top
            # Sort descending (higher CD is better)
            front.sort(key=lambda x: x.crowding_distance, reverse=True)
            
            needed = N_POP - len(new_pop)
            new_pop.extend(front[:needed])
            
        front_idx += 1
        
    pop = new_pop
    
    # Re-sort for clean Rank/CD for next iteration (optional but good practice)
    pop, fronts = non_dominated_sort(pop)
    pop, fronts = calculate_crowding_distance(pop, fronts)

# ---------------- VISUALIZATION ----------------
print("Optimization Finished.")

# Extract F1 and F2 for plotting
pareto_front = [ind for ind in pop if ind.rank == 1]
f1_vals = [ind.objectives[0] for ind in pareto_front]
f2_vals = [ind.objectives[1] for ind in pareto_front]

plt.figure(figsize=(6, 4))
plt.scatter(f1_vals, f2_vals, c='blue', marker='*', label='Pareto Front')
plt.title(f'Pareto Front - {PROBLEM_NAME}')
plt.xlabel('Objective 1',fontsize=12)
plt.ylabel('Objective 2',fontsize=12)
plt.grid(True, linestyle='--')
plt.legend()
plt.show()