import random


def generate_random_population(number_of_objects, number_of_random_chromosomes):
    population_list = []
    for _ in range(number_of_random_chromosomes):
        rand_chromosome = list(range(number_of_objects))
        random.shuffle(rand_chromosome)
        population_list.append(rand_chromosome)
    return population_list
