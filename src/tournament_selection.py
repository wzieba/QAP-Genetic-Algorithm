import random


def tournament_selection(population_list, fitness_scores_list, elitism=False):  # Create new population
    new_species = []
    population_size = len(fitness_scores_list)
    population_size = population_size - 1 if elitism else population_size
    for _ in range(0, population_size):
        # Take best
        of_parent_idx = random.randint(0, len(fitness_scores_list) - 1)
        tf_parent_idx = random.randint(0, len(fitness_scores_list) - 1)
        if fitness_scores_list[of_parent_idx] > fitness_scores_list[tf_parent_idx]:
            ch_winner = population_list[of_parent_idx]
        else:
            ch_winner = population_list[tf_parent_idx]
        new_species.append(ch_winner)
    return new_species
