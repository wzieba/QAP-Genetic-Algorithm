from unittest import TestCase

from fitness_function import compute_fitness_scores_list, get_normalized_result_of_fitness_function_scores_list

TEST_POPULATION = [[1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 3, 2]]
TEST_FITNESS_SCORES = [454, 395, 495]


class TestFitnessScore(TestCase):

    def test_fitness_scores_match(self):
        fitness_scores_list = compute_fitness_scores_list(population=TEST_POPULATION)
        self.assertEqual(fitness_scores_list, TEST_FITNESS_SCORES)

    def test_normalized_fitness_scores(self):
        normalized_fitness_scores_list = get_normalized_result_of_fitness_function_scores_list(
            population=TEST_POPULATION)
        for normalized_fitness_score in normalized_fitness_scores_list:
            self.assertTrue(0 <= normalized_fitness_score <= 1)

    def test_invalid_parameters(self):
        with self.assertRaises(AssertionError):
            compute_fitness_scores_list(population=[[2, 1, 1, 1]])
