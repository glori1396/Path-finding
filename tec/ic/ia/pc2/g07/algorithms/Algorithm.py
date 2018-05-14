from abc import ABC, abstractmethod

"""
This class implement an abstract class as a definition of an algorithm.
"""

class Algorithm(ABC):
    def __init__(self, board):
        self.board = board

    @abstractmethod
    def execute(self):
        pass
