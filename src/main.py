import time
from colorsys import hsv_to_rgb

import numpy as np
from matplotlib import cm

from data_loading import matrices_size, flow_matrix, distance_matrix
from src.config import INITIAL_POPULATION_SIZE, NUMBER_OF_GENERATIONS
from src.crossover import perform_crossover
from src.drawer import CustomDrawer
from src.fitness_function import compute_fitness_scores_list, get_normalized_result_of_fitness_function_scores_list
from src.generate_population import generate_random_population
from src.mutation import mutate_population
from src.selection import generate_new_population_using_roulette_selection
from src.tournament_selection import tournament_selection


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
        fitness_scores = get_normalized_result_of_fitness_function_scores_list(population)
        max_fitness = np.max(fitness_scores)
        max_chromosome = population[np.argmax(fitness_scores)]
        max_chromosome = list(map(lambda value: value + 1, max_chromosome))

        selected_chromosomes = tournament_selection(population, fitness_scores)
        crossed_chromosomes = perform_crossover(selected_chromosomes)
        mutated_chromosomes = mutate_population(crossed_chromosomes)

        print_console_output()
        if previous_max_chromosome != max_chromosome:
            draw_visual_frame()

        previous_max_chromosome = max_chromosome

        population = mutated_chromosomes

    drawer.screen.mainloop()


if __name__ == "__main__":
    main()
