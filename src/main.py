import numpy as np

from data_loading import matrices_size
from src.crossover import perform_crossover
from src.fitness_function import compute_fitness_scores_list
from src.generate_population import generate_random_population
from src.mutation import mutate_population
from src.selection import generate_new_population_using_roulette_selection

population = generate_random_population(matrices_size, 100)
for epoch in range(100):
    fitness_scores = compute_fitness_scores_list(population)
    max_fitness = np.max(fitness_scores)
    max_chromosome = population[np.argmax(fitness_scores)]
    max_chromosome = list(map(lambda value: value + 1, max_chromosome))
    print("Epoch: \t\t\t\t{}\nMean fit.: \t\t\t{}\nMax score: \t\t\t{}\nMax chrom.: \t\t{}\n"
          .format(epoch, np.mean(fitness_scores), max_fitness, max_chromosome))

    selected_chromosomes = generate_new_population_using_roulette_selection(population, fitness_scores)
    crossed_chromosomes = perform_crossover(selected_chromosomes)
    mutated_chromosomes = mutate_population(crossed_chromosomes)
    print('\n')

    population = mutated_chromosomes
