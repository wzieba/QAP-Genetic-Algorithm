from unittest import TestCase

from crossover import crossover_chromosomes, perform_crossover

TEST_POPULATION = [[6, 5, 4, 4, 5, 6], [1, 2, 3, 3, 2, 1]]


class TestCrossoverChromosomes(TestCase):

    def test_crossover_chromosomes(self):
        self.assertEqual(([6, 5, 4, 4, 5, 6], [1, 2, 3, 3, 2, 1]),
                         crossover_chromosomes(([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]), 3))

    def test_size_of_crossovered_population(self):
        self.assertGreaterEqual(len(perform_crossover(TEST_POPULATION)), len(TEST_POPULATION))
