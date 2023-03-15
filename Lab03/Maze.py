import pygad
import time
import numpy
import math
import matplotlib.pyplot as plt

safe_fields = [
    [1, 1], [1, 2], [1, 3], [1, 5], [1, 6], [1, 7], [1, 9], [1, 10],
    [2, 3], [2, 4], [2, 5], [2, 7], [2, 10],
    [3, 1], [3, 2], [3, 3], [3, 5], [3, 7], [3, 8], [3, 9], [3, 10],
    [4, 1], [4, 3], [4, 6], [4, 7], [4, 10],
    [5, 1], [5, 2], [5, 5], [5, 6], [5, 7], [5, 9], [5, 10],
    [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 7], [6, 8], [6, 9],
    [7, 1], [7, 3], [7, 4], [7, 7], [7, 9], [7, 10],
    [8, 1], [8, 5], [8, 6], [8, 7], [8, 10],
    [9, 1], [9, 3], [9, 6], [9, 8], [9, 10],
    [10, 1], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]
]

gene_space = [0, 1, 2, 3]

# Find the shortest path from start to end with max steps = 30
def fitness_func(solution, solution_idx):
    # Starting position
    position = [1, 1]
    # Remember explored positions
    explored_positions = []
    # Evaluate fitness of solution
    fitness = 0
    # Remember number of steps
    steps = 0
    
    
    for move in solution:
        steps += 1
        new_position = position.copy()
        
        # Decode move
        if move == 0:  # Up
            new_position[0] -= 1
        elif move == 1:  # Down
            new_position[0] += 1
        elif move == 2:  # Left
            new_position[1] -= 1
        elif move == 3:  # Right
            new_position[1] += 1
            
            
        if new_position in safe_fields:
            # Update position
            position = new_position
            # Update fitness
            fitness += new_position[0] * 2 + new_position[1] * 2
        else:
            fitness -= 5
        
        
        if new_position in explored_positions:
            fitness -= 20  # Penalize revisiting a position
        else:
            fitness += 10  # Reward exploring new positions
            
            
        if position == [10, 10]:
            fitness += 300  # Reward reaching the end
            break  # Reached the end
        # if steps == 30:
        #     break  # Maximum path length reached
        
        explored_positions.append(new_position)
        
        
    return fitness


fitness_function = fitness_func
sol_per_pop = 5000
num_parents_mating = 10
num_generations = 1000
keep_parents = 5
initial_population = numpy.random.randint(0, 4, (10, 30))
parent_selection_type = "tournament"
crossover_type = "two_points"
mutation_type = "scramble"
mutation_percent_genes = 4


ga_instance = pygad.GA(gene_space=gene_space,
                    num_generations=num_generations,
                    num_parents_mating=num_parents_mating,
                    fitness_func=fitness_function,
                    # sol_per_pop=sol_per_pop,
                    # num_genes=30,
                    parent_selection_type=parent_selection_type,
                    keep_parents=keep_parents,
                    crossover_type=crossover_type,
                    mutation_type=mutation_type,
                    mutation_percent_genes=mutation_percent_genes,
                    initial_population=initial_population)
ga_instance.run()


# Extract the best solution and its fitness value
best_solution = ga_instance.best_solution()[0]

best_fitness = ga_instance.best_solution()[1]


# Print the best solution and its fitness value
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)