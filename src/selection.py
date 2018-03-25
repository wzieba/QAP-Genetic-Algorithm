import numpy as np
import random


# Chromosomes with bigger fitness will be selected more times
def generate_new_population_using_roulette_selection(population, fitness_scores_list):
    new_population = []

    # Remove maximum value from every element so roullete selection will rely on bigger difference
    worst_result = np.min(fitness_scores_list)
    fitness_scores_list = list(map(lambda value: value - worst_result, fitness_scores_list))

    cumulative_sum = np.cumsum(fitness_scores_list)

    for _ in range(len(population)):
        probability_of_choose = random.uniform(0, 1) * sum(fitness_scores_list)
        randomly_selected_member = select_chromosome_using_roulette_method(population, cumulative_sum,
                                                                           probability_of_choose)
        new_population.append(randomly_selected_member)

    return new_population


def select_chromosome_using_roulette_method(population, cumulative_sum, randomly_generated_probability):
    for index, _ in enumerate(cumulative_sum):
        if randomly_generated_probability <= cumulative_sum[index]:
            return population[index]
