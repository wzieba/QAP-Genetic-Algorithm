from unittest import TestCase

from selection import select_chromosome_using_roulette_method, generate_new_population_using_roulette_selection

TEST_FITNESS_SCORES_LIST = [1, 2, 3]
TEST_CUMULATIVE_SUM = [1, 3, 6]
TEST_POPULATION = [["testA"], ["testB"], ["testC"]]


def selected_chromosome(randomly_generated_probability):
    return select_chromosome_using_roulette_method(TEST_POPULATION, TEST_CUMULATIVE_SUM,
                                                   randomly_generated_probability)


class TestSelectMemberUsingRouletteMethod(TestCase):

    def test_select_member_using_roulette_method(self):
        self.assertEqual(["testC"], selected_chromosome(3.5))
        self.assertEqual(["testA"], selected_chromosome(0))
        self.assertEqual(["testC"], selected_chromosome(6))
        self.assertEqual(["testA"], selected_chromosome(0.99))

    def test_size_of_generated_population(self):
        new_population = generate_new_population_using_roulette_selection(TEST_POPULATION, TEST_FITNESS_SCORES_LIST)
        self.assertEqual(len(TEST_POPULATION), len(new_population))

    def test_validate_members_of_generated_population(self):
        new_population = generate_new_population_using_roulette_selection(TEST_POPULATION, TEST_FITNESS_SCORES_LIST)
        for chromosome in new_population:
            self.assertIn(chromosome, TEST_POPULATION)
