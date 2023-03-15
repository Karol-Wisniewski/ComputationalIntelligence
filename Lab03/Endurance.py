import pygad
import time
import numpy
import math
import matplotlib.pyplot as plt

#gene space is a number between 0 and 1
gene_space = numpy.arange(0, 1, 0.001)

def endurance(x, y, z, u, v, w):
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)

def fitness_func(solution, solution_idx):
    x = solution[0]
    y = solution[1]
    z = solution[2]
    u = solution[3]
    v = solution[4]
    w = solution[5]
    
    return endurance(x, y, z, u, v, w)

fitness_function = fitness_func
sol_per_pop = 50
num_genes = 6
num_parents_mating = 3
num_generations = 50
keep_parents = 1

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 17

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

best_fitness_values = []
generations = []

for generation in range(num_generations):
    generations.append(generation)
    best_fitness = ga_instance.best_solutions_fitness[generation]
    best_fitness_values.append(best_fitness)

# Create a line plot of the best fitness values vs. generations
plt.plot(generations, best_fitness_values)
plt.title("Best Fitness Value vs. Generation")
plt.xlabel("Generation")
plt.ylabel("Best Fitness Value")
plt.show()

