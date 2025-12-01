NSGA-II Implementation

Introduction

This repository contains an educational and runnable implementation of the NSGA-II (Non-dominated Sorting Genetic Algorithm II), one of the most popular evolutionary algorithms for solving Multi-Objective Optimization Problems (MOOP).

The implementation supports the Constrained Dominance principle to handle constrained MOOPs and utilizes Fast Non-dominated Sort and Crowding Distance mechanisms to maintain a diverse set of solutions on the Pareto Front.

Features

NSGA-II Core: Complete and modular implementation of the main NSGA-II flowchart.

Constrained Dominance: Capability to solve multi-objective optimization problems with constraints (such as Binh-Korn and Chan-Kong-Haimes).

Standard Test Functions: Includes well-known test functions in multi-objective optimization, such as:

ZDT1, ZDT3

Kursawe, Fonseca

Schaffer1, Schaffer2

BinhKorn, Chan-Kong-Haimes

Genetic Operators: Uses SBX Crossover and Polynomial Mutation for offspring generation.

Visualization: Generates a plot of the final Pareto Front using Matplotlib (in the Python version).

File Structure

The project is designed to be modular for clarity and maintainability.

File

Description

Language

NSGA2_main.py / NSGA2_main.m

Main file and entry point for executing the algorithm.

Python / MATLAB

individual.py

Defines the class/struct to hold individual data (position, objectives, rank, crowding distance, and constraint violation).

Python

evaluate_objectives.py / evaluate_objectives.m

Defines objective functions and constraints for various test problems.

Python / MATLAB

get_problem_details.py / get_problem_details.m

Defines the number of variables and the upper/lower bounds for each problem.

Python / MATLAB

check_dominance_logic.py / check_dominance_logic.m

The core function for comparing two individuals based on the constrained dominance rule.

Python / MATLAB

non_dominated_sort.py / non_dominated_sort.m

Implements the fast non-dominated sorting mechanism to determine the Rank of individuals.

Python / MATLAB

crowding_distance.py / crowding_distance.m

Calculates the crowding distance for individuals within each Pareto Front.

Python / MATLAB

tournament_selection.py / tournament_selection.m

Selects individuals for reproduction using tournament selection based on rank and crowding distance.

Python / MATLAB

genetic_operators.py / genetic_operators.m

Implements the SBX Crossover and Polynomial Mutation operators.

Python / MATLAB

Prerequisites

For Python Implementation

Python: Version 3.7 or higher

NumPy: For array operations

Matplotlib: For plotting results (Pareto Front)

To install the required packages, run the following command:

pip install numpy matplotlib


For MATLAB Implementation

MATLAB: Any recent version that supports scripts and functions.

Getting Started

1. Python Implementation

Download or clone the Python files.

Execute the main file:

python NSGA2_main.py


Change the Problem: To solve a different problem (e.g., BinhKorn), edit the PROBLEM_NAME variable at the top of the NSGA2_main.py file:

# NSGA2_main.py
PROBLEM_NAME = 'BinhKorn' # Changed from 'ZDT1'


2. MATLAB Implementation

Place all .m files in a single directory (folder).

Execute the main script in the MATLAB environment:

NSGA2_main


Change the Problem: Modify the problem_name variable at the top of the NSGA2_main.m file:

% NSGA2_main.m
problem_name = 'Kursawe'; % Changed from 'ZDT3'


Results

Upon completion of the algorithm (in the Python version), a plot containing the non-dominated Pareto Front (Front 1) in the Objective Space is displayed. This chart shows the distribution of final solutions and the quality of convergence.

Contribution

We welcome contributions to improve this code! If you find a bug or have a suggestion, please open an Issue or submit a Pull Request.

