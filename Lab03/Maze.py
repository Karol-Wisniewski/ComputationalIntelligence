import pygad
import time
import numpy
import math
import matplotlib.pyplot as plt

maze = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0], 
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0], 
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0], 
        [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0], 
        [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0], 
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], 
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0], 
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0], 
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0], 
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# 0 - down, 1 - up, 2 - left, 3 - right
gene_space = [0, 1, 2, 3]

start_position = (1, 1)
end_position = (10, 10)

position = [0, 0]

def check_colission(x, y):
    if x > 11 or y > 11 or x < 0 or y < 0:
        return True
    if maze[x][y] == 0:
       return True
    return False

# Find the shortest path from start to end with max steps = 30
def fitness_func(solution, solution_idx):
    end_row, end_col = end_position
    row, column = start_position
    steps = 0
    
    for move in solution:
        if row == end_row and column == end_col:
            position[0] = row
            position[1] = column
            return steps * -1
        if move == 0:
            if not check_colission(row + 1, column):
                row += 1
        if move == 1:
            if not check_colission(row - 1, column):
                row -= 1
        if move == 2:
            if not check_colission(row, column - 1):
                column -= 1
        if move == 3:
            if not check_colission(row, column + 1):
                column += 1
        steps += 1

    #Distance from end position - 1 (to avoid multiplying steps by 0) * steps (to penalize longer paths)
    return (((abs(end_col - column) + abs(end_row - row)) * -1) - 1) * steps 


fitness_function = fitness_func
sol_per_pop = 200
num_genes = 30
num_parents_mating = 70
num_generations = 500
keep_parents = 50
parent_selection_type = "tournament"
crossover_type = "two_points"
mutation_type = "scramble"
mutation_percent_genes = 6


ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)
ga_instance.run()


# Extract the best solution and its fitness value
best_solution = ga_instance.best_solution()[0]

best_fitness = ga_instance.best_solution()[1]


# Print the best solution and its fitness value
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
print("Steps taken:", -best_fitness)
print("Final position: ",  position)
# ga_instance.plot_fitness()