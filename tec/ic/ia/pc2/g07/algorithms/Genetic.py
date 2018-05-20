from tec.ic.ia.pc2.g07.algorithms.Algorithm import Algorithm

"""
This class implements a genetic algorithm to solve a path-finding problem.
"""

class Genetic(Algorithm):
    def __init__(self, board, direction, number_individuals, number_generations):
        super().__init__(board)
        self.rows_in_board = 0
        self.cols_in_board = 0
        self.direction = direction
        self.number_individuals = number_individuals
        self.number_generations = number_generations

    def first_birth(self):
        for row in self.board:
            pass
        print(self.board)

    def calculate_fitness(self, population):
        pass

    def execute(self):
        #Variables to save files
        self.rows_in_board = len(self.board)
        self.cols_in_board = len(self.board[0])

        # Create original individuals
        population = self.first_birth()
        print(population)

        # Reproduce for generations
        #for generation in range(self.number_generations):

            #Fathers Selection

            #Reproduction

            #Mutation

            #Calculate population's fitness

            #Sort popoulation by fitness

            #Selection of Next Generation
