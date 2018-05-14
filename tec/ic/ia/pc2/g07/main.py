import argparse

from tec.ic.ia.pc2.g07.algorithms.A_Star import A_Star
from tec.ic.ia.pc2.g07.algorithms.Genetic import Genetic

parser = argparse.ArgumentParser(
    description='This program allows to execute a path-finding algortihm. It can be A* or a genetic algorithm for scenario changes.')

# A*
parser.add_argument("--a-estrella",
                    action="store_true", help="A* Algorithm.")
parser.add_argument("--vision", type=int, help="Vision field range.")
parser.add_argument("--zanahorias", type=int, help="Objective's amount to search.")

# Genetic Algorithm
parser.add_argument("--genetico",
                    action="store_true", help="Genetic Algorithm.")
parser.add_argument("--derecha", action="store_true", help="All individual going to the right.")
parser.add_argument("--izquierda", action="store_true", help="All individual going to the left.")
parser.add_argument("--arriba", action="store_true", help="All individual going up.")
parser.add_argument("--abajo", action="store_true", help="All individual going down.")
parser.add_argument("--individuos", type=int, help="Individual's amount.")
parser.add_argument("--generaciones", type=int, help="Generation's amount.")

# Main Program
parser.add_argument("--tablero-inicial", required=True,
                    help="Input file destination. File containing the scenario to be resolved.")

args = parser.parse_args()

# Checks if just one algorithm is selected
cont_unique_flag = 0
unique_flags = ["a_estrella", "genetico"]
for flag in unique_flags:
    if args.__dict__[flag]:
        cont_unique_flag += 1

if cont_unique_flag != 1:
    parser.error("The application needs ONE algorithm per execution.")
    exit(-1)

algorithm = None
#Checks algorithm selected parameters
if args.a_estrella:
    if args.vision is None or args.zanahorias is None:
        parser.error(
            "The A* algorithm needs to know the vision fiel range and carrot's amount.")
        exit(-1)
    elif args.vision < 1 or args.zanahorias < 1:
        parser.error(
            "The A* algorithm needs to know the vision fiel range and carrot's amount. (>=1)")
        exit(-1)

    algorithm = A_Star(board = None, vision = args.vision, carrots = args.zanahorias)

elif args.genetico:
    # Checks if just one direction is selected
    cont_unique_flag = 0
    direction = ""
    unique_flags = ["derecha", "izquierda", "arriba", "abajo"]
    for flag in unique_flags:
        if args.__dict__[flag]:
            cont_unique_flag += 1
            direction = flag

    if cont_unique_flag != 1:
        parser.error("The genetic algorithm need just one direction.")
        exit(-1)
    if args.individuos is None or args.generaciones is None:
        parser.error(
            "The genetic algorithm needs to know the individual's and generation's amount.")
        exit(-1)
    elif args.individuos < 1 or args.generaciones < 1:
        parser.error(
            "The genetic algorithm needs to know the individual's and generation's amount. (>=1)")
        exit(-1)
    algorithm = Genetic(board = None, direction = direction, individuals = args.individuos, generations = args.generaciones)

#Read the board
board = []
with open(args.tablero_inicial) as file:
    for rows in file.readlines():
        row = []
        for col in rows[:-1]:
            row.append(col)
        board.append(row)

#Execute the algorithm
algorithm.board = board
algorithm.execute()
