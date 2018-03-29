from unittest import TestCase

from src.mutation import BasicMutation

TEST_CHROMOSOME_TO_MUTATE = [1, 2, 3, 4]
TEST_POPULATION = [[1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 3, 2]]


class TestBasicMutation(TestCase):

    def setUp(self):
        super().setUp()
        self.basic_mutation = BasicMutation()

    def test_mutate_chromosome(self):
        self.assertEqual([1, 4, 3, 2], self.basic_mutation.mutate_chromosome(TEST_CHROMOSOME_TO_MUTATE, (1, 3)))

    def test_mutate_population(self):
        self.assertEqual(len(TEST_POPULATION), len(self.basic_mutation.mutate_population(TEST_POPULATION)))
