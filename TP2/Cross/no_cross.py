from Cross.crossover import Crossover


class NoCross(Crossover):
    def __init__(self, parent_size, genome_size, item_keys):
        super().__init__(parent_size, genome_size, item_keys)

    def crossover(self, parent1, parent2):
        pass

    def cross(self, parents):
        return parents
