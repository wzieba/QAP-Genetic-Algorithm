import random

from config import mutation_probability


# In TSP and QAP problem mutation will have slightly different form. We will choose two genes and swap them.

def mutate_population(population):
    chromosomes_with_mutated = []

    for chromosome in population:
        if 0 <= random.uniform(0, 1) <= mutation_probability:
            mutated_chromosome = mutate_chromosome(chromosome, generate_random_gen_indexes(chromosome))
            chromosomes_with_mutated.append(mutated_chromosome)
        else:
            chromosomes_with_mutated.append(chromosome)

    return chromosomes_with_mutated


def mutate_chromosome(chromosome, random_indexes):
    gen_a_index, gen_b_index = random_indexes
    chromosome[gen_a_index], chromosome[gen_b_index] = chromosome[gen_b_index], chromosome[gen_a_index]
    return chromosome


def generate_random_gen_indexes(chromosome):
    return random.randint(0, len(chromosome) - 1), random.randint(0, len(chromosome) - 1)
