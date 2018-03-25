import numpy as np
from data_loading import matrices_size, flow_matrix, distance_matrix


# Summary: The objective of the Quadratic Assignment Problem (QAP) is to assign n facilities to n locations in such a
#  way as to minimize the assignment cost.
#
# The assignment cost is the sum, over all pairs, of the flow between a pair
#  of facilities multiplied by the distance between their assigned locations.


def compute_fitness_scores_list(population):
    fitness_scores_list = []
    for chromosome in population:
        assert len(chromosome) == len(set(chromosome))
        chromosome_fitness_sum = 0
        for x in range(matrices_size):
            for y in range(matrices_size):
                chromosome_fitness_sum += distance_matrix[x, y] * flow_matrix[chromosome[x] - 1, chromosome[y] - 1]
        fitness_scores_list.append(chromosome_fitness_sum / 2)

    return fitness_scores_list


def get_normalized_result_of_fitness_function_scores_list(population):
    fitness_scores_list = compute_fitness_scores_list(population)
    map_to_minimization_problem = list(map(lambda value: 1. / value, fitness_scores_list))
    normalized_results = np.array(map_to_minimization_problem) / np.sum(map_to_minimization_problem)
    return normalized_results
