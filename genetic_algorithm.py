import random
import numpy as np
import matplotlib.pyplot as plt

# Parameters
population_size = 100
gene_length = 10
mutation_rate = 0.01
generations = 100

# Fitness Function (example)
def fitness(individual):
    return sum(individual)  # Simple fitness function: sum of gene values

# Initial population
def generate_individual():
    return [random.randint(0, 1) for _ in range(gene_length)]

def generate_population():
    return [generate_individual() for _ in range(population_size)]

# Selection - Tournament Selection
def tournament_selection(population):
    tournament_size = 5
    selected = random.sample(population, tournament_size)
    selected.sort(key=lambda x: fitness(x), reverse=True)
    return selected[0]

# Crossover - One-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, gene_length - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation - Flip bit with a probability
def mutate(individual):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]

# Genetic Algorithm
def genetic_algorithm():
    population = generate_population()
    avg_values, min_values, max_values = [], [], []
    
    for generation in range(generations):
        # Selection
        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])

        population = new_population

        # Collect stats for plotting
        fitness_values = [fitness(ind) for ind in population]
        avg_values.append(np.mean(fitness_values))
        min_values.append(np.min(fitness_values))
        max_values.append(np.max(fitness_values))

        # Print stats (optional)
        print(f"Generation {generation + 1}:")
        print(f"  Average Fitness: {avg_values[-1]}")
        print(f"  Minimum Fitness: {min_values[-1]}")
        print(f"  Maximum Fitness: {max_values[-1]}")
    
    return avg_values, min_values, max_values

# Run Genetic Algorithm and get fitness metrics
avg_values, min_values, max_values = genetic_algorithm()

# Plotting the results
plt.figure(figsize=(10, 6))

# Plot for average, minimum, and maximum values
plt.plot(avg_values, label='Average Fitness', color='blue', linestyle='-', marker='o')
plt.plot(min_values, label='Minimum Fitness', color='red', linestyle='--', marker='x')
plt.plot(max_values, label='Maximum Fitness', color='green', linestyle='-.', marker='^')

# Add labels and title
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Genetic Algorithm Fitness Over Generations')

# Add a legend
plt.legend()

# Show the plot
plt.show()
