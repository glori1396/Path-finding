from tec.ic.ia.pc2.g07.algorithms.Algorithm import Algorithm

"""
This class implements a genetic algorithm to solve a path-finding problem.
"""

class Genetic(Algorithm):
    def __init__(self, board, direction, individuals, generations):
        super().__init__(board)
        self.direction = direction
        self.individuals = individuals
        self.generations = generations

    def execute(self):
        pass
