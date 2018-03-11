import copy
import random
import numpy as np

from config import crossover_probability


def perform_crossover(population):
    chromosomes_to_crossover = []
    crossovered_chromosomes = []

    for chromosome in population:
        if 0 <= random.uniform(0, 1) <= crossover_probability:
            chromosomes_to_crossover.append(chromosome)

    for parents in pairwise(chromosomes_to_crossover):
        point_of_crossover = random.randint(0, len(parents[0]))
        result_of_crossovering = crossover_chromosomes(parents, point_of_crossover)
        crossovered_chromosomes += list(result_of_crossovering)

    # Removes invalid chromosomes
    crossovered_chromosomes = list(filter(lambda val: len(val) == len(set(val)), crossovered_chromosomes))

    return np.asarray(population + crossovered_chromosomes)


def crossover_chromosomes(parents, point_of_crossover):
    father, mother = parents
    child_a, child_b = copy.copy(father), copy.copy(mother)

    for change_index in range(point_of_crossover):
        child_a[change_index], child_b[change_index] = child_b[change_index], child_a[change_index]

    return child_a, child_b


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)
