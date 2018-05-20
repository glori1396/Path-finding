
"""
This class implements a genetic algorithm individual.
"""


class Individual():
    def __init__(self, gene):
        self.gene = gene
        self.fitness = 0

    def get_part(self, part_number, number_of_breaks):
        average = len(self.gene) / float(number_of_breaks)
        result = []
        last = 0.0

        while last < len(self.gene):
            result.append(self.gene[int(last):int(last + average)])
            last += average
        return result[part_number]

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __repr__(self):
        return str([self.gene, self.fitness])

    def __str__(self):
        return str([self.gene, self.fitness])
