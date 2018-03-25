from unittest import TestCase

import numpy as np

from src.fitness_function import compute_fitness_scores_list, get_normalized_result_of_fitness_function_scores_list

TEST_POPULATION = [[1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 3, 2], [4, 1, 2, 3], [3, 4, 2, 1]]


class TestFitnessScore(TestCase):

    def test_fitness_scores_match(self):
        fitness_scores_list = compute_fitness_scores_list(population=TEST_POPULATION)
        self.assertEqual([454, 395, 495, 429, 417], fitness_scores_list)

    def test_normalized_fitness_scores(self):
        normalized_fitness_scores_list = get_normalized_result_of_fitness_function_scores_list(
            population=TEST_POPULATION)
        for normalized_fitness_score in normalized_fitness_scores_list:
            self.assertTrue(0 <= normalized_fitness_score <= 1)

    def test_invalid_parameters(self):
        with self.assertRaises(AssertionError):
            compute_fitness_scores_list(population=[[2, 1, 1, 1]])

    def test_normalized_fitness_score_values(self):
        scores_list = get_normalized_result_of_fitness_function_scores_list(population=TEST_POPULATION)
        print(scores_list)
        self.assertTrue(scores_list[2] < scores_list[0] < scores_list[3] < scores_list[1])

    def test_results_sum_to_one(self):
        normalized_fitness_scores_list = get_normalized_result_of_fitness_function_scores_list(
            population=TEST_POPULATION)
        self.assertTrue(abs(1.0 - sum(normalized_fitness_scores_list) <= 0.00002))

    def test_best_value_choose(self):
        normalized_fitness_scores_list = get_normalized_result_of_fitness_function_scores_list(
            population=TEST_POPULATION)
        max_chromosome = TEST_POPULATION[np.argmax(normalized_fitness_scores_list)]
        self.assertEqual([3, 4, 1, 2], max_chromosome)

    def test_mean_of_fitness_score(self):
        normalized_fitness_scores_list = get_normalized_result_of_fitness_function_scores_list(
            population=TEST_POPULATION)
        self.assertTrue(abs(0.2 - np.mean(normalized_fitness_scores_list) <= 0.00002))
