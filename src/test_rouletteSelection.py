from unittest import TestCase

from src.selection import RouletteSelection

TEST_FITNESS_SCORES_LIST = [1, 2, 3]
TEST_CUMULATIVE_SUM = [1, 3, 6]
TEST_POPULATION = [["testA"], ["testB"], ["testC"]]


class TestRouletteSelection(TestCase):

    def setUp(self):
        super().setUp()
        self.roulette_selection_algorithm = RouletteSelection()

    def test_select_proper_value(self):
        self.assertEqual(["testC"], self.selected_chromosome(3.5))
        self.assertEqual(["testA"], self.selected_chromosome(0))
        self.assertEqual(["testC"], self.selected_chromosome(6))
        self.assertEqual(["testA"], self.selected_chromosome(0.99))

    def test_size_of_generated_population(self):
        new_population = self.roulette_selection_algorithm.selection(TEST_POPULATION, TEST_FITNESS_SCORES_LIST)
        self.assertEqual(len(TEST_POPULATION), len(new_population))

    def test_validate_members_of_generated_population(self):
        new_population = self.roulette_selection_algorithm.selection(TEST_POPULATION, TEST_FITNESS_SCORES_LIST)
        for chromosome in new_population:
            self.assertIn(chromosome, TEST_POPULATION)

    def selected_chromosome(self, randomly_generated_probability):
        return self.roulette_selection_algorithm.select_chromosome(TEST_POPULATION,
                                                                   TEST_CUMULATIVE_SUM,
                                                                   randomly_generated_probability)
