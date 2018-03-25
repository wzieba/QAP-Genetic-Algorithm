import time
from colorsys import hsv_to_rgb

import numpy as np
from matplotlib import cm

from data_loading import matrices_size, flow_matrix, distance_matrix
from src.crossover import perform_crossover
from src.drawer import CustomDrawer
from src.fitness_function import compute_fitness_scores_list
from src.generate_population import generate_random_population
from src.mutation import mutate_population
from src.selection import generate_new_population_using_roulette_selection
from src.tournament_selection import tournament_selection

population = generate_random_population(matrices_size, 1000)

drawer = CustomDrawer()

previous_max_chromosome = []


def get_color_for_value(value):
    max_distance = np.max(distance_matrix)
    percent_value = value / max_distance

    return rgb(0, max_distance, value)


def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value - minimum) / (maximum - minimum)
    b = int(max(0, 255 * (1 - ratio)))
    r = int(max(0, 255 * (ratio - 1)))
    g = 255 - b - r
    return g, r, b


for epoch in range(1000):

    fitness_scores = compute_fitness_scores_list(population)
    max_fitness = np.max(fitness_scores)
    max_chromosome = population[np.argmax(fitness_scores)]
    max_chromosome = list(map(lambda value: value + 1, max_chromosome))
    print("Epoch: \t\t\t\t{}\nMean fit.: \t\t\t{}\nMax score: \t\t\t{}\nMax chrom.: \t\t{}\n"
          .format(epoch, np.mean(fitness_scores), max_fitness, max_chromosome))

    selected_chromosomes = tournament_selection(population, fitness_scores)
    crossed_chromosomes = perform_crossover(selected_chromosomes)
    mutated_chromosomes = mutate_population(crossed_chromosomes)
    print('\n')

    if previous_max_chromosome != max_chromosome:
        drawer.draw_generation(max_chromosome, epoch, max_fitness)
        for x in range(matrices_size):
            for y in range(matrices_size):
                flow_value = flow_matrix[max_chromosome[x] - 1, max_chromosome[y] - 1]
                distance_value = distance_matrix[x, y]
                if flow_value != 0:
                    drawer.draw_line(x, y, pen_color=get_color_for_value(distance_value), pen_size=flow_value)

        drawer.screen.update()
        time.sleep(1)

    previous_max_chromosome = max_chromosome

    time.sleep(0.01)

    population = mutated_chromosomes

drawer.screen.mainloop()
