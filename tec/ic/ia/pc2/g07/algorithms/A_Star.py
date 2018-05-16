from tec.ic.ia.pc2.g07.algorithms.Algorithm import Algorithm
from queue import Queue
from random import choice
import itertools

"""
This class implements an A* algorithm to solve a path-finding problem.
"""


class A_Star(Algorithm):
    def __init__(self, board, vision, carrots):
        super().__init__(board)
        self.vision = vision
        self.carrots = carrots
        #A* Variables
        self.open = []
        self.f = []
        self.g = 0
        self.LastMovements = []
        self.MaxLastMovements = 5
        self.totalCost = 0

    # def calc_vision_field_slots(self):
    #     cont = 1
    #     odd = 3
    #     while(cont != self.vision):
    #         odd+=2
    #         cont+=1
    #     return odd*odd

    def search_start(self):
        for row in range(len(self.board)):
            if 'C' in self.board[row]:
                return [row, self.board[row].index('C')]
        print("\nThe file does not contain a rabbit.")
        exit(-1)

    def is_in_board(self, x, y):
        try:
            if x < 0 or y < 0:
                return False
            dummy = self.board[x][y]
            return True
        except:
            return False

    def search_neighbors(self, current_state):
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        succesors = []
        for neighbor in neighbors:
            x = current_state[0] + neighbor[0]
            y = current_state[1] + neighbor[1]
            if self.is_in_board(x, y):
                succesors.append([x, y])
        return succesors

    def get_lower(self):
        best = min(self.f)
        count = self.f.count(best)
        if count == 1:
            return best, self.open[self.f.index(best)]
        else:
            indixes = [i for i, x in enumerate(self.f) if x == best]
            return best, self.open[choice(indixes)]

    def put_Last_Movement(self, state):
        if len(self.LastMovements) == self.MaxLastMovements:
            self.LastMovements = self.LastMovements[1:]
        self.LastMovements.append(state)

    def pretty_print(self, last, current):
        movements_indexes = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        movements = ["LEFT", "RIGHT", "UP", "DOWN"]
        index = [current[0]-last[0], current[1]-last[1]]
        i = movements_indexes.index(index)
        movement = movements[i]

        step = "Step: %05d" % (self.g,)
        for direction_index in range(len(movements)):
            mov_index = movements_indexes[direction_index]
            index = [current[0]-mov_index[0], current[1]-mov_index[1]]
            cost = "Out of Borders"
            if index in self.open:
                cost = self.f[self.open.index(index)]
            step += " "+movements[direction_index]+": "+cost
        move = " Movement: "+movement
        print(step + move)

    def carrots_in_sight(self, current_state):
        posibilites = list(range(-self.vision, self.vision+1))
        vision_field_indexes = [[x, y] for x in posibilites for y in posibilites]
        vision_field_indexes.remove([0,0])
        carrots_coordinates = []
        for field in vision_field_indexes:
            x = current_state[0] + field[0]
            y = current_state[1] + field[1]
            if self.is_in_board(x,y) and self.board[x][y] == 'Z':
                carrots_coordinates.append([x,y])
        return carrots_coordinates

    def h_without_carrots(self):
        h = []
        for possible_state in self.open:
            #Last immediate direction
            if possible_state in self.LastMovements[-1:]:
                h.append(10)
            #Being there lately
            elif possible_state in self.LastMovements[:-1]:
                h.append(5)
            #Not being there
            else:
                h.append(1)
        return

    def h_with_carrots(self, carrots_coordinates):
        h = []
        for possible_state in self.open:
            nearest_carrot_distance = abs(possible_state[0]-carrots_coordinates[0][0]+ possible_state[1]-carrots_coordinates[0][1])
            for carrot in carrots_coordinates[1:]:
                distance = abs(possible_state[0]-carrot[0] + possible_state[1]-carrot[1])
                if distance < nearest_carrot_distance:
                    nearest_carrot_distance = distance
            h.append(nearest_carrot_distance)



    def calculate_f_score(self, current_state):
        g = [self.g for i in self.open]
        h = 0
        carrots_coordinates = self.carrots_in_sight(current_state)
        if carrots_coordinates == []:
            h = self.h_without_carrots()
        else:
            h = self.h_with_carrots(carrots_coordinates)

        self.f = [x + y for x, y in zip(g, h)]

    def execute(self):
        self.open.append(self.search_start())
        self.f.append(0)
        carrots_found = 0

        cost, current = self.get_lower()

        while len(self.open) != 0:
            if carrots_found == self.carrots:
                print("Step: "+self.g+ " FINAL ; Total Cost: "+ self.totalCost)
                break

            #Refresh neighbors
            self.open = self.search_neighbors(current)

            #f(state) = g(state) + h(state)
            self.calculate_f_score(current)

            #Stores last movement
            self.put_Last_Movement(current)
            last = current
            self.totalCost += cost

            #Move
            cost, current = self.get_lower()
            self.g += 1
            self.pretty_print(last, current)
            self.refresh_board(last, current)
            self.save_board()
