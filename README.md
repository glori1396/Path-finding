# Path Finding

**Description:** This repository contains the short-project #2 and #3 of Artificial Intelligence course from Instituto Tecnológico de Costa Rica, imparted by the professor Juan Manuel Esquivel. The project consists on implement search algorithms to solve labyrinth problems. Specifically, we will solve a problem where a board introduced as a file have a rabbit and carrots. The rabbit, then will have to find a specified amount of carrots.

The project will be divided into two parts, both contained in a console program that will execute with different modes using differentiated flags. The first will consist
in developing a heuristic used within [A*](#a) to generically go over the board in
look for carrots. The second will consist of developing a [Genetic Algorithm](#genetic-algorithm) that will optimize the placement of directional signals so that the rabbit travel over the board.

### Content:

* [Installation](#installation)
* [Usage](#usage)
* [Board Representation](#board-representation)
* [Algorithms' Report](#models-report)
* [Unit Testing](#unit-testing)

## Installation:

Before using the project, first you have to install all the project dependencies.

* Python 3.4 or greater.

Now that all dependencies are installed. You can install the project using:

```pip install -U tec.ic.ia.pc2.g07.main```

Or you can clone the repository by:

```git clone https://github.com/mamemo/Path-finding.git```

## Usage:

When you have the directory with the repository, you have to search the repository on a console and execute the instruction:

```python -m tec.ic.ia.pc2.g07.main -h```

This will display all the flags that you can work with:

```
  -h, --help            show this help message and exit
  --a-estrella          A* Algorithm.
  --vision VISION       Vision field range.
  --zanahorias ZANAHORIAS
                        Objective's amount to search.
  --movimientos-pasados MOVIMIENTOS_PASADOS
                        Number of past movements to store. (Default 5)
  --genetico            Genetic Algorithm.
  --derecha             All individual going to the right.
  --izquierda           All individual going to the left.
  --arriba              All individual going up.
  --abajo               All individual going down.
  --individuos INDIVIDUOS
                        Individual's amount.
  --generaciones GENERACIONES
                        Generation's amount.
  --politica-cruce {random,sons_of_sons}
                        Crossover algorithm.
  --cantidad-padres CANTIDAD_PADRES
                        Number of parents.
  --tasa-mutacion TASA_MUTACION
                        Mutation Rate Percent.
  --tablero-inicial TABLERO_INICIAL
                        Input file destination. File containing the scenario
                        to be resolved.
```
Each algorithm uses different flags, but they have one in common, you can see the description next to the flag:

```
  --tablero-inicial TABLERO_INICIAL
                      Input file destination. File containing the scenario
                      to be resolved.
```

To run A* you will need:

```
  --a-estrella          A* Algorithm.
  --vision VISION       Vision field range.
  --zanahorias ZANAHORIAS
                        Objective's amount to search.
  --movimientos-pasados MOVIMIENTOS_PASADOS
                        Number of past movements to store. (Default 5)
```

To run Genetic Algorithm you will need:

```
  --genetico            Genetic Algorithm.
  --derecha             All individual going to the right.
  --izquierda           All individual going to the left.
  --arriba              All individual going up.
  --abajo               All individual going down.
  --individuos INDIVIDUOS
                        Individual's amount.
  --generaciones GENERACIONES
                        Generation's amount.
  --politica-cruce {random,sons_of_sons}
                        Crossover algorithm.
  --cantidad-padres CANTIDAD_PADRES
                        Number of parents.
  --tasa-mutacion TASA_MUTACION
                        Mutation Rate Percent.
```



## Board Representation:

The board will be a text file of N lines and M columns and each character can be only:

* C: capitalized, identifies the position of the rabbit. There can only be one per board.
* Z: capitalized, identifies the position of a carrot. There may be multiple carrots per board.
* Blank space: The space character does not have any side effects but it does must be present to indicate a position on the board by which the rabbit can transit.
* <: symbol for smaller than, indicates a change of direction to the left.
* \>: symbol for greater than, indicates a change of direction to the right.
* A: letter A capitalized, indicates a change of direction upwards.
* V: letter V capitalized, indicates a change of direction downwards.
* Change of line: It has no interpretation in the program other than separating different rows.

For further experiments we will use the following board:

<div style="text-align:center"><img text="Board" src="images/board.PNG" width="500"></div>

## Algorithms' Report

This section contains the analysis of using each algorithm and how well it performs with different parameters. Every model is called from [main.py](../master/tec/ic/ia/pc2/g07/main.py) and the process is the following:
1. Waiting parameters.
2. Receiving parameters.
3. Creating the respectively algorithm.
3. Validate the flags.
4. Running the algorithm.
5. Generate output messages and files.

### A*

The main goal was to create a program that moves the rabbit through the board, a box at a time, using A\*. We had to design a cost function to guide the search A\* considering the accumulated cost and a heuristic to approximate the future cost. The accumulated cost up to a specific point in the execution of the algorithm will be simply the number of steps that the rabbit has given.

The future cost will be describe below, the elements that we had to consider was:
* The environment is not completely observable.
* The rabbit will have a range of vision. If the current state has the rabbit in the box (20,
18), for example, and the rabbit has a vision of two, may take into account the content of the boxes (18, 16) to the box (22, 20).
* The design of the heuristic should not include "memory" that makes the environment implicitly
observable. In particular, the algorithm should maintain the memory footprint equally for "big" and "little" search spaces.
* At the beginning of the program, it will be indicated how many carrots the rabbit should look for in total
to finish his work.

The function cost is defined as follows:

$$f(x) = \lambda e^{-\lambda x}$$

For logistic regression we had to compare how it performs with regularization L1 and L2. All the experiment combinations were ran 10 times and the value in the table is the mean. Also, all the experiments were ran with normalized samples covering the whole country, the samples were normalized and the labels were transformed to one hot encoding. The algorithm was implemented using Tensorflow and you can follow the process with specific commented functions at [Logistic_Regression.py](../master/tec/ic/ia/p1/models/Logistic_Regression.py). In these tests we used the next hyper-parameters to get the best results:
* Learning rate = 0.01
* Training epochs = 5000
* Batch size = 1000
* Regularization Coefficient = 0.01

The results were:
