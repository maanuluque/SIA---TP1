from SIA.TP2.Selection.selection import Selection
import random


class Universal(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)

    def select(self, population):
        # TODO: Change hardcoded K parameter
        #k = int(len(population) / 2)
        k = self.amount
        total_performance = 0
        # Just to get total performance
        # TODO: Can be added when population is created
        for character in population:
            total_performance += character.performance

        acumulated_performance = 0
        acc_performances = {} # Key: acc_performance (should be unique), Value --> Character
        for character in population:
            acumulated_performance += (character.performance / total_performance)
            character.acumulated_performance = acumulated_performance
            acc_performances[acumulated_performance] = character

        sorted_acc_performances = sorted(acc_performances.keys())
        random_numbers = {}
        for x in range(k):
            temporal_random_number = (random.randint(0,1) + x)/k
            random_numbers[x] = temporal_random_number

        selected_population = []
        for r_number in range(len(random_numbers)):
            for acc_performance in sorted_acc_performances:
                if r_number > acc_performance:
                    selected_population.append(acc_performances[acc_performance])
                    break

        return selected_population
