import time

import numpy as np

from src.config import INITIAL_POPULATION_SIZE, NUMBER_OF_GENERATIONS, DRAW_VISUALIZATION
from src.crossover import BasicCrossover, Crossover
from src.data_loading import matrices_size, flow_matrix, distance_matrix
from src.drawer import CustomDrawer
from src.fitness_function import get_normalized_result_of_fitness_function_scores_list, compute_fitness_scores_list
from src.generate_population import generate_random_population
from src.mutation import Mutation, BasicMutation
from src.selection import Selection, TournamentSelection

selection_strategy = Selection(selection_algorithm=TournamentSelection())
mutation_strategy = Mutation(mutation_algorithm=BasicMutation())
crossover_strategy = Crossover(crossover_algorithm=BasicCrossover())


def main():
    population = generate_random_population(matrices_size, INITIAL_POPULATION_SIZE)

    drawer = CustomDrawer()

    previous_max_chromosome = []

    def draw_visual_frame():
        drawer.draw_generation_frame(max_chromosome, epoch, max_fitness, max_chromosome, flow_matrix, distance_matrix)
        time.sleep(1)
        return

    def print_console_output():
        print("Epoch: \t\t\t\t{}\nMean fit.: \t\t\t{}\nMax score: \t\t\t{}\nMax chrom.: \t\t{}\n\n"
              .format(epoch, np.mean(fitness_scores), max_fitness, max_chromosome))

    for epoch in range(NUMBER_OF_GENERATIONS):

        fitness_scores = compute_fitness_scores_list(population, distance_matrix, flow_matrix)
        fitness_scores_normalized = get_normalized_result_of_fitness_function_scores_list(fitness_scores)

        max_fitness = np.min(fitness_scores)
        max_chromosome = population[np.argmin(fitness_scores)]
        max_chromosome = list(map(lambda value: value + 1, max_chromosome))

        selected_chromosomes = selection_strategy.select(population, fitness_scores_normalized)
        crossed_chromosomes = crossover_strategy.crossover(selected_chromosomes)
        mutated_chromosomes = mutation_strategy.mutate(crossed_chromosomes)

        print_console_output()
        if DRAW_VISUALIZATION and previous_max_chromosome != max_chromosome:
            draw_visual_frame()

        previous_max_chromosome = max_chromosome

        population = mutated_chromosomes

    drawer.screen.mainloop()


if __name__ == "__main__":
    main()
