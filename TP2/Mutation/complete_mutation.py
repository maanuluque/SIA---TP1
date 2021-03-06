import random
from Mutation.mutation import Mutation


class CompleteMutation(Mutation):
    def __init__(self, children_size, probability, min_h, max_h, height_decimals, items_db):
        super().__init__(children_size, probability, min_h, max_h, height_decimals, items_db)

    def single_mutation(self, child):
        p = random.random()
        if p < self.probability:
            return child
        return self.mutate_gene(child, [*range(1, 7)])

