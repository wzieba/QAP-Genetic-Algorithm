from unittest import TestCase

from src.mutation import mutate_chromosome, mutate_population

TEST_CHROMOSOME_TO_MUTATE = [1, 2, 3, 4]
TEST_POPULATION = [[1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 3, 2]]


class TestMutateChromosome(TestCase):

    def test_mutate_chromosome(self):
        self.assertEqual([1, 4, 3, 2], mutate_chromosome(TEST_CHROMOSOME_TO_MUTATE, (1, 3)))

    def test_mutate_population(self):
        self.assertEqual(len(TEST_POPULATION), len(mutate_population(TEST_POPULATION)))
