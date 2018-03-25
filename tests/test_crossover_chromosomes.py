from unittest import TestCase

from src.crossover import crossover_chromosomes, perform_crossover

TEST_POPULATION = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]


class TestCrossoverChromosomes(TestCase):

    def test_crossover_chromosomes(self):
        chromosome_a, chromosome_b = crossover_chromosomes(
            TEST_POPULATION[0],
            TEST_POPULATION[1],
            point_of_crossover=2
        )
        self.assertEqual([6, 5, 3, 4, 2, 1], chromosome_a)
        self.assertEqual([1, 2, 4, 3, 5, 6], chromosome_b)


def test_size_of_crossovered_population(self):
    self.assertGreaterEqual(len(perform_crossover(TEST_POPULATION)), len(TEST_POPULATION))
