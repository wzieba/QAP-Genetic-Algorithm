from unittest import TestCase

from src.generate_population import generate_random_population

TEST_NUMBER_OF_RANDOM_CHROMOSOMES = 5
TEST_NUMBER_OF_OBJECTS = 10


class TestGenerateRandomPopulation(TestCase):
    list_of_random_chromosomes = []

    def setUp(self):
        self.list_of_random_chromosomes = generate_random_population(TEST_NUMBER_OF_OBJECTS,
                                                                     TEST_NUMBER_OF_RANDOM_CHROMOSOMES)

    def testGenerateRandomPopulationSize(self):
        self.assertTrue(self.list_of_random_chromosomes.__len__() == TEST_NUMBER_OF_RANDOM_CHROMOSOMES)

    def testGenerateRandomPopulationGensInRange(self):
        for chromosome in self.list_of_random_chromosomes:
            for gen in chromosome:
                self.assertTrue(gen in range(TEST_NUMBER_OF_OBJECTS))
