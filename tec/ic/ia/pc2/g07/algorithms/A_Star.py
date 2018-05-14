from tec.ic.ia.pc2.g07.algorithms.Algorithm import Algorithm

"""
This class implements an A* algorithm to solve a path-finding problem.
"""

class A_Star(Algorithm):
    def __init__(self, board, vision, carrots):
        super().__init__(board)
        self.vision = vision
        self.carrots = carrots

    def execute(self):
        pass
