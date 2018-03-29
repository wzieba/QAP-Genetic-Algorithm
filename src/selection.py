import numpy as np
import random


class Selection(object):
    def __init__(self, selection_algorithm):
        self.selection_algorithm = selection_algorithm

    def select(self, population, fitness_scores):
        return self.selection_algorithm(population, fitness_scores)


class RouletteSelection(object):

    def __init__(self):
        pass

    def __call__(self, population, fitness_score_list):
        return self.selection(population, fitness_score_list)

    # Chromosomes with bigger fitness will be selected more times
    @staticmethod
    def selection(population, fitness_scores_list):
        new_population = []

        # Remove maximum value from every element so roulette selection will rely on bigger difference
        worst_result = np.min(fitness_scores_list)
        fitness_scores_list = list(map(lambda value: value - worst_result, fitness_scores_list))

        cumulative_sum = np.cumsum(fitness_scores_list)

        for _ in range(len(population)):
            probability_of_choose = random.uniform(0, 1) * sum(fitness_scores_list)
            randomly_selected_member = RouletteSelection.select_chromosome(population,
                                                                           cumulative_sum,
                                                                           probability_of_choose)
            new_population.append(randomly_selected_member)

        return new_population

    @staticmethod
    def select_chromosome(population, cumulative_sum, randomly_generated_probability):
        for index, _ in enumerate(cumulative_sum):
            if randomly_generated_probability <= cumulative_sum[index]:
                return population[index]


class TournamentSelection(object):

    def __init__(self):
        pass

    def __call__(self, population, fitness_score_list):
        return self.tournament_selection(population, fitness_score_list)

    @staticmethod
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
