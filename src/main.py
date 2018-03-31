import sys
import os.path

import time

import numpy as np

from src.plot_drawer import PlotDrawer

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.config import POPULATION_SIZE, NUMBER_OF_GENERATIONS, DRAW_VISUALIZATION, INPUT_FILE, DRAW_CHART
from src.crossover import BasicCrossover, Crossover
from src.data_loading import matrices_size, flow_matrix, distance_matrix
from src.visualization_drawer import CustomDrawer
from src.fitness_function import get_normalized_result_of_fitness_function_scores_list, compute_fitness_scores_list
from src.generate_population import generate_random_population
from src.mutation import Mutation, BasicMutation
from src.selection import Selection, TournamentSelection, RouletteSelection

selection_strategy = Selection(selection_algorithm=TournamentSelection())
mutation_strategy = Mutation(mutation_algorithm=BasicMutation())
crossover_strategy = Crossover(crossover_algorithm=BasicCrossover())


def main():
    population = generate_random_population(matrices_size, POPULATION_SIZE)

    visualization_drawer = CustomDrawer()
    plot_drawer = PlotDrawer()

    generation_indicies = []
    average_results = []
    min_results = []
    max_results = []
    previous_max_chromosome = []

    def draw_visual_frame():
        visualization_drawer.draw_generation_frame(max_chromosome, epoch, max_fitness, max_chromosome, flow_matrix,
                                                   distance_matrix)
        time.sleep(1)
        return

    def print_console_output():
        print("Epoch: \t\t\t\t{}\nMean fit.: \t\t\t{}\nMax score: \t\t\t{}\nMax chrom.: \t\t{}\n\n"
              .format(epoch, average_fitness, max_fitness, max_chromosome))

    for epoch in range(NUMBER_OF_GENERATIONS):

        fitness_scores = compute_fitness_scores_list(population, distance_matrix, flow_matrix)
        fitness_scores_normalized = get_normalized_result_of_fitness_function_scores_list(fitness_scores)

        # While it's not normalized yet, max means "the worst", therefor "min" for us.
        max_fitness = np.min(fitness_scores)
        min_fitness = np.max(fitness_scores)
        average_fitness = np.mean(fitness_scores)

        max_results.append(max_fitness)
        min_results.append(min_fitness)
        average_results.append(average_fitness)
        generation_indicies.append(epoch)

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

    if DRAW_CHART:
        plot_drawer.drawPlot(INPUT_FILE, generation_indicies, average_results, max_results, min_results)

    visualization_drawer.screen.mainloop()


if __name__ == "__main__":
    main()
