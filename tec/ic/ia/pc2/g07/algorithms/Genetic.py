from tec.ic.ia.pc2.g07.algorithms.Algorithm import Algorithm
from tec.ic.ia.pc2.g07.algorithms.Genetic_Classes.Individual import Individual
from tec.ic.ia.pc2.g07.algorithms.Genetic_Classes.CrossOver import CrossOver
"""
This class implements a genetic algorithm to solve a path-finding problem.
"""


class Genetic(Algorithm):
    def __init__(self, board, direction, number_individuals, number_generations, crossover):
        super().__init__(board)
        self.rows_in_board = 0
        self.cols_in_board = 0
        self.direction = direction
        self.number_individuals = number_individuals
        self.number_generations = number_generations
        self.crossover = crossover

    # Function for establish a seed on random generator
    def set_random_seed(self, seed):
        random.seed(seed)

    def first_birth(self, template, amount):
        gene = []
        for row in template:
            gene += row

        # Population
        return [Individual(gene) for i in range(amount)]

    def calculate_fitness(self, population):
        pass

    def execute(self):
        # Variables to save files
        self.rows_in_board = len(self.board)
        self.cols_in_board = len(self.board[0])

        # Create original individuals
        population = self.first_birth(
            template=self.board, amount=self.number_individuals)

        # Reproduce for generations
        for generation in range(self.number_generations):
            old_population = population[:]
            for i in range(self.number_individuals):
                # Fathers Selection
                parents = self.crossover.select_parents(old_population)
                # Reproduction
                new_individual = self.crossover.cross(parents)
                # Integration to the society
                population.append(new_individual)

            # Mutation

            # Calculate population's fitness

            # Sort popoulation by fitness

            # Selection of Next Generation
