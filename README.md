# Path Finding

**Description:** This repository contains the short-project #2 and #3 of Artificial Intelligence course from Instituto Tecnológico of Costa Rica, imparted by the professor Juan Manuel Esquivel. The project consists on implementing search algorithms to solve labyrinth problems. Specifically, we will solve a problem where a board introduced as a file have a rabbit and carrots. The rabbit, then will have to find a specified amount of carrots.

The project will be divided into two parts, both contained in a console program that will execute with different modes using differentiated flags. The first will consist
in developing a heuristic used within [A*](#a) to generically go over the board looking for carrots. The second will consist of developing a [Genetic Algorithm](#genetic-algorithm) that will optimize the placement of directional signals so that the rabbit travel over the board.

### Content:

* [Installation](#installation)
* [Usage](#usage)
* [Board Representation](#board-representation)
* [Algorithms' Report](#algorithms-report)
* [Unit Testing](#unit-testing)

## Installation:

Before using the project, first you have to install all the project dependencies.

* Python 3.4 or greater.

Now that all dependencies are installed. You can install the project using:

```pip install -U tec.ic.ia.pc2.g07.main```

Or you can clone the repository by:

```git clone https://github.com/mamemo/Path-finding.git```

## Usage:

When you have the directory with the repository, you have to search that repository on a console and execute the instruction:

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
Each algorithm uses differentiated flags, but they have one in common, you can see the description next to the flag:

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

Examples of boards will be presented at the analysis of the algorithms.

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

<div style="text-align:center"><img text="Board" src="images/cost_function.png" width="200"></div>

we defined g(x) as:

<div style="text-align:center"><img src="images/cost_g.png" width="200"></div>

where x stands for the number of steps taken.

Then we have the heuristic h(x) defined as:
<div style="text-align:center"><img src="images/cost_h.png" width="300"></div>

We defined h_without_carrots(x) as the function of heuristic without considering the carrots in sight:

<div style="text-align:center"><img src="images/cost_h_without_carrots.png" width="400"></div>

where x is the possible state to move. Then the function considering the carrots is defined as the heuristic h_with_carrots(x):

<div style="text-align:center"><img src="images/cost_h_with_carrots.png" width="400"></div>

The *nearest_carrot* part is the distance between the possible state and the nearest possible carrot. For example in:

<div style="text-align:center"><img src="images/nearest.PNG" width="150"></div>

For the tested next state **[3,1]**, the nearest carrot will be **[5,0]**; because abs(3-5)+abs(1-0) = **3** and for the other carrot in sight the distance is abs(3-0)+abs(1-5) = **7**.

The *carrots_at_reach* part is how many carrots are at reach if you move to the state. For example, the reach fields are presented in the next images:

<div style="text-align:center"><img src="images/reach_left.PNG" width="150"><img src="images/reach_down.PNG" width="150"><img src="images/reach_right.PNG" width="150"><img src="images/reach_up.PNG" width="150"></div>

where the results for the states [[2,0], [3,1], [2,2], [1,1]] would be **1**.

So, as summary, if we have these scenarios, the costs are:

 <div style="text-align:center"><img src="images/cost_ex_left.PNG" width="150"><img src="images/cost_ex.PNG" width="150"><img src="images/cost_example.PNG" width="150"><img src="images/cost_ex_up.PNG" width="150"></div>

 <div style="text-align:center"><img src="images/cost_ex_down.png" width="150"><img src="images/cost_ex_down.png" width="150"><img src="images/cost_example_right.png" width="150"><img src="images/cost_example_right.png" width="150"></div>

 The best possible states are equally [2,0] and [3,1] with a cost of **6**. In these cases the next state is selected randomly.

Now, we will present the analysis of cost variation when carrots number and vision are changed. Every each of the following experiments are presented after 10 executions. The value below is the mean of the cost. The commented code of this algorithm is in [A_Star.py](../master/tec/ic/ia/pc2/g07/algorithms/A_Star.py).

The used board is presented below and it contains 25x25 boxes and 19 carrots. You can find it on [test_board.txt](../master/test_board.txt).

<div style="text-align:center"><img text="Board" src="images/board.PNG" width="400"></div>

#### Variation in carrots number

<div style="text-align:center"><img src="images/chart_cost_carrots.PNG" width="400"><img src="images/chart_steps_carrots.PNG" width="400"></div>

> The vision field is 2.
<div style="text-align:center"><table>
    <tbody>
        <tr>
            <th>Carrots</th>
            <th>1</th>
            <th>3</th>
            <th>5</th>
            <th>9</th>
            <th>13</th>
            <th>15</th>
            <th>19</th>
        </tr>
        <tr>
            <th>Cost</th>
            <td>25.3</td>
            <td>929.5</td>
            <td>4707.5</td>
            <td>30697.7</td>
            <td>85406.3</td>
            <td>210162.4</td>
            <th>1911582.1</th>
        </tr>
        <tr>
            <th>Steps</th>
            <td>6.6</td>
            <td>41.6</td>
            <td>90.8</td>
            <td>225.7</td>
            <td>375.3</td>
            <td>587.5</td>
            <th>1776</th>
        </tr>
    </tbody>
</table></div>

From these results we can conclude:

* If the rabbit needs to find more carrots will have to move more around the board and the cost will grow.

#### Variation in vision field

<div style="text-align:center"><img src="images/chart_cost_vision.PNG" width="400"><img src="images/chart_steps_vision.PNG" width="400"></div>

> The carrots to find are all of them. (19)
<div style="text-align:center"><table>
    <tbody>
        <tr>
            <th>Carrots</th>
            <th>1</th>
            <th>3</th>
            <th>5</th>
            <th>9</th>
            <th>13</th>
            <th>15</th>
            <th>19</th>
            <th>25</th>
        </tr>
        <tr>
            <th>Cost</th>
            <td>3343809.3</td>
            <td>699767.4</td>
            <td>531807.1</td>
            <td>56611.2</td>
            <td>44365.3</td>
            <th>36510.9</th>
            <td>Inf</td>
            <td>Inf</td>
        </tr>
        <tr>
            <th>Steps</th>
            <td>2203.2</td>
            <td>973</td>
            <td>935</td>
            <td>304.4</td>
            <td>282.6</td>
            <th>257.4</th>
            <td>Inf</td>
            <td>Inf</td>
        </tr>
    </tbody>
</table></div>

From these results we can conclude:

* On vision field of 19 and 20, the rabbit gets in a loop so it will never stop, that's why in the chart we put it a Inf value.

* The loop is caused because the rabbit walk to a certain point where it approaches a carrot and another carrot see as a better approach and viceversa. So it moves in circles.

* As we can see when the vision field gets bigger the rabbit can do better decision, so it reduces the cost and steps. That tendency remains until a certain number of vision field.


### Genetic Algorithm

The main goal was to create a program that evolve the board with directional signals. The algorithm should not make decisions about how to move the rabbit step by step, but assume that the rabbit always moves in one way and it can change its direction with signals. The program, as said before, will have to determine the ideal location of the signals so that the rabbit can collect ALL the carrots on the board in as few steps as possible and with the least amount of signals.

The initial state is given by a file equal to A*. In addition, it should be indicated through a flag, what will be the initial direction of the rabbit, which is key to place the first signal.
Each individual, for the genetic algorithm, will be a complete board with its corresponding carrots, signals and location of the rabbit.

We had to follow certain implementation restrictions:

* Mutations are punctual operations. Add a signal in a random box, change the direction of a signal or remove a signal.
* The fitness function must combine total carrots collected, amount of rabbit steps and number of signals. It must be emphasized that it is valid to have a linear combination
heuristic where it is reflected that there is a greater penalty for adding a signal than for giving a certain number of steps.
* The fitness function does not influence the selection of crossover and mutation. Both basic operations of genetic algorithms are, in essence, completely random
given a policy. The fitness function only serves to order the population of more to less fitness and select those that pass to the next generation.

Next we will explain the mutation, crossover and fitness decisions and implementation:

* Mutation: We had a mutation rate given by parameter, if a random generated number is below the mutation rate, that individual will be mutated. If it qualify to be mutated, a random box is selected, if that random box contains *"C"* or *"Z"* (rabbit or carrot) that mutation will be discarted. Otherwise, a random element is selected from these options *">", "<", "V", "A", " "*, the element that is already on the box is removed from the options. The commented code can be found on [Genetic.py](../master/tec/ic/ia/pc2/g07/algorithms/Genetic.py) at *mutate_population()*
> The original individual is NOT changed, a mutated copy is added in the population instead.

* Crossover: The crossover algorithm is indicated by parameter. We had to implement 2 kind of crossover, we implemented [Random](../master/tec/ic/ia/pc2/g07/algorithms/Genetic_Classes/Random_CrossOver.py) and [Son of sons](../master/tec/ic/ia/pc2/g07/algorithms/Genetic_Classes/Sons_of_Sons_CrossOver.py) crossover. Basically both of them has 2 functions:
  - *select_parents(population)*: This function selects a number (given by parameter) of parents from the population. For both implemented crossovers, the parents are selected randomly.
  - *cross(parents)*: According to each crossover this function works different. Its objective is to cross the selected parents. **Random** crossover divide the parents in segments (same as number of parents) and each parent give the respectively segment according to the position of its selection, finally the son is added to the population. For example: If selected parents are [[1,2,3,4,5,6], [7,8,9,10,11,12]], the child would be [1,2,3,10,11,12]. And it can scalate to *n* parents. **Son of sons** simulates a more *"realistic"* idea of a generation. Taken for example the human life, a typical individual live to create a son and that son create another child. So, that is basically what this crossover do, the selected parentes are divide in two groups, each group creates a son like Random crossover does and then those sons creates a grandson that will be added to the population. The grandson's parents are randomly sorted and are crossed like Random crossover does.

* Fitness: To give each individual a fitness number, *walk_trough_board* and *calculate_fitness* functions were implemented in [Genetic.py](../master/tec/ic/ia/pc2/g07/algorithms/Genetic.py). In order to calculate the fitness we need 4 values given by *walk_trough_board*, those are:
  - Movements: As it's said, is the number of steps made by the rabbit. It can be from 0 to the amount of boxes.
  > The *walk_trough_board* is stopped when movements are the same as number of boxes in the board because that means a loop.
  - Carrots Eaten: Is the number of carrots that the rabbit could find. If the carrot has already been found this number don't increment. It can be from 0 to the total number of carrots.
  - Useful signals: The amount of signals that lead to a carrot. Signals that don't lead to a carrot or weren't used don't increment this number. It can be from 0 to number of boxes minus the total amount of carrots minus one (the rabbit).
  - Has opposite signals: A flag indicating if the board has opossite signals. It can be True or False. For example: [">"," ","<"] woud result as True.

  After we got those values, we give penalties and rewards to the individual, those are:

  <div style="text-align:center"><table>
      <tbody>
          <tr>
              <th>Case</th>
              <th>Points</th>
              <th>Explanation</th>
          </tr>
          <tr>
              <td>Carrot eaten</td>
              <td>+100</td>
              <td>Reward for find a carrot. Applied for each carrot found.</td>
          </tr>
          <tr>
              <td>Movement</td>
              <td>+5</td>
              <td>Reward for step. Applied for each step. Indicating that the individual should explore more.</td>
          </tr>
          <tr>
              <td>Useful Signal</td>
              <td>+3</td>
              <td>Reward for having useful signals. Applied for each useful signal.</td>
          </tr>
          <tr>
              <td>Carrot left</td>
              <td>-50</td>
              <td>Penalty for not find a carrot. Applied for each carrot left.</td>
          </tr>
          <tr>
              <td>Useless signals</td>
              <td>-50</td>
              <td>Penalty for having useless signals (Don't lead to a carrot or weren't used). Applied for each useless signal.</td>
          </tr>
          <tr>
              <td>Starting</td>
              <td>-50</td>
              <td>Penalty for not having signals and don't get all the carrots. Applied once. Works when the algorithm is starting, giving better results to individuals that do something.</td>
          </tr>
          <tr>
              <td>Has opposite signals</td>
              <td>-1000</td>
              <td>Penalty for having opposite signals. Applied once.</td>
          </tr>
          <tr>
              <td>Trap in a loop</td>
              <td>-1000</td>
              <td>Penalty for geting the movements same as the number of boxes in the board. Applied once. Discard the individual completely.</td>
          </tr>
      </tbody>
  </table></div>


Now, we will present the analysis of fitness variation when mutation rate and crossover are changed. Every each of the following experiments are presented after 30 executions. The value below is the mean of the fitness. The commented code of this algorithm is in [Genetic.py](../master/tec/ic/ia/pc2/g07/algorithms/Genetic.py).

The used board is presented below and it contains 10x10 boxes and 6 carrots. You can find it on [board_example.txt](../master/board_example.txt).

<div style="text-align:center"><img text="Board" src="images/board_genetic.PNG" width="300"></div>

#### Mutation Rate Variation

<div style="text-align:center"><table>
  <tbody>
    <tr>
      <th>Left</th>
      <th><img src="images/chart_fitness_left.PNG" width="400"></th>
      <th>Right</th>
      <th><img src="images/chart_fitness_right.PNG" width="400"></th>
    </tr>
    <tr>
      <th>Up</th>
      <th><img src="images/chart_fitness_up.PNG" width="400"></th>
      <th>Down</th>
      <th><img src="images/chart_fitness_down.PNG" width="400"></th>
    </tr>
  </tbody>
</table></div>

> The number of individuals are 100.
>
>The random crossover is selected.
>
>The number of parents is 2.

<div style="text-align:center"><table>
    <thead>
      <tr>
          <th>Direction</th>
          <th>Left</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <th colspan="2">Generation</th>
            <th>1</th>
            <th>5</th>
            <th>10</th>
            <th>15</th>
            <th>25</th>
            <th>50</th>
            <th>75</th>
            <th>100</th>
        </tr>
        <tr>
            <th rowspan="4">Mutation Rate</th>
            <th>5%</th>
            <td>-345</td>
            <td>-344.34</td>
            <td>-327.57</td>
            <td>-283.37</td>
            <td>-223.78</td>
            <td>-70.82</td>
            <td>61.08</td>
            <td>173.93</td>
        </tr>
        <tr>
            <th>15%</th>
            <td>-344.91</td>
            <td>-336.81</td>
            <td>-285.48</td>
            <td>-49.88</td>
            <td>-217.04</td>
            <td>202.808</td>
            <td>360.49</td>
            <td>458.01</td>
        </tr>
        <tr>
            <th>25%</th>
            <td>-344.67</td>
            <td>-325.77</td>
            <td>-249.44</td>
            <td>-145.51</td>
            <td>47.209</td>
            <td>379.55</td>
            <td>577.84</td>
            <td>632.06</td>
        </tr>
        <tr>
            <th>50%</th>
            <td>-344.58</td>
            <td>-310.003</td>
            <td>-143.508</td>
            <td>-12.36</td>
            <td>177.43</td>
            <td>605.52</td>
            <td>711.93</td>
            <th>711.93</th>
        </tr>
    </tbody>
</table></div>
<div style="text-align:center"><table>
    <thead>
      <tr>
          <th>Direction</th>
          <th>Right</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <th colspan="2">Generation</th>
            <th>1</th>
            <th>5</th>
            <th>10</th>
            <th>15</th>
            <th>25</th>
            <th>50</th>
            <th>75</th>
            <th>100</th>
        </tr>
        <tr>
            <th rowspan="4">Mutation Rate</th>
            <th>5%</th>
            <td>-309.72</td>
            <td>-300.31</td>
            <td>-235.91</td>
            <td>-174.97</td>
            <td>-77.63</td>
            <td>50.55</td>
            <td>85.08</td>
            <td>122.6</td>
        </tr>
        <tr>
            <th>15%</th>
            <td>-308.95</td>
            <td>-272.13</td>
            <td>-100.29</td>
            <td>-53.37</td>
            <td>47.003</td>
            <td>247.06</td>
            <td>340.46</td>
            <td>407.512</td>
        </tr>
        <tr>
            <th>25%</th>
            <td>-308.63</td>
            <td>-235.71</td>
            <td>-67.27</td>
            <td>-11.48</td>
            <td>149.78</td>
            <td>371.77</td>
            <td>453.6</td>
            <td>466.8</td>
        </tr>
        <tr>
            <th>50%</th>
            <td>-307.41</td>
            <td>-165.005</td>
            <td>-32.78</td>
            <td>79.47</td>
            <td>282.86</td>
            <td>548.65</td>
            <td>581.53</td>
            <th>581.53</th>
        </tr>
    </tbody>
</table></div>
<div style="text-align:center"><table>
    <thead>
      <tr>
          <th>Direction</th>
          <th>Up</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <th colspan="2">Generation</th>
            <th>1</th>
            <th>5</th>
            <th>10</th>
            <th>15</th>
            <th>25</th>
            <th>50</th>
            <th>75</th>
            <th>100</th>
        </tr>
        <tr>
            <th rowspan="4">Mutation Rate</th>
            <th>5%</th>
            <td>-344.91</td>
            <td>-344.12</td>
            <td>-325.37</td>
            <td>-287.501</td>
            <td>-247.25</td>
            <td>-95.85</td>
            <td>69.17</td>
            <td>123.91</td>
        </tr>
        <tr>
            <th>15%</th>
            <td>-344.75</td>
            <td>-340.26</td>
            <td>-269.709</td>
            <td>-188.32</td>
            <td>-50.72</td>
            <td>236.406</td>
            <td>331.72</td>
            <td>338.37</td>
        </tr>
        <tr>
            <th>25%</th>
            <td>-344.505</td>
            <td>-319.506</td>
            <td>-206.11</td>
            <td>-127.73</td>
            <td>69.65</td>
            <td>290.21</td>
            <td>375.43</td>
            <td>387.3</td>
        </tr>
        <tr>
            <th>50%</th>
            <td>-344.34</td>
            <td>-304.73</td>
            <td>-174.45</td>
            <td>-11.29</td>
            <td>247.91</td>
            <td>541.63</td>
            <td>583.106</td>
            <th>588.73</th>
        </tr>
    </tbody>
</table></div>
<div style="text-align:center"><table>
    <thead>
      <tr>
          <th>Direction</th>
          <th>Down</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <th colspan="2">Generation</th>
            <th>1</th>
            <th>5</th>
            <th>10</th>
            <th>15</th>
            <th>25</th>
            <th>50</th>
            <th>75</th>
            <th>100</th>
        </tr>
        <tr>
            <th rowspan="4">Mutation Rate</th>
            <th>5%</th>
            <td>-309.801</td>
            <td>-301.49</td>
            <td>-225.82</td>
            <td>-145.09</td>
            <td>-64.05</td>
            <td>41.35</td>
            <td>88.12</td>
            <td>159.29</td>
        </tr>
        <tr>
            <th>15%</th>
            <td>-309.29</td>
            <td>-280.55</td>
            <td>-94.39</td>
            <td>-39.86</td>
            <td>44.33</td>
            <td>152.58</td>
            <td>273.103</td>
            <td>311.9</td>
        </tr>
        <tr>
            <th>25%</th>
            <td>-308.84</td>
            <td>-245.0003</td>
            <td>-46.47</td>
            <td>21.093</td>
            <td>111.85</td>
            <td>293.44</td>
            <td>361.28</td>
            <td>385.83</td>
        </tr>
        <tr>
            <th>50%</th>
            <td>-307.73</td>
            <td>-153.14</td>
            <td>-1.006</td>
            <td>54.705</td>
            <td>166.708</td>
            <td>424.99</td>
            <td>508.16</td>
            <th>514.63</th>
        </tr>
    </tbody>
</table></div>

From these results we can conclude:
* As the mutation rate gets higher, also does the average fitness. This tendency goes for every direction.
* Higher mutation rate means more modified individuals and the probability of mutate to a better individual gets higher.


#### Crossover Variation

<div style="text-align:center"><table>
  <tbody>
    <tr>
      <th>Random</th>
      <th><img src="images/chart_fitness_random.PNG" width="400"></th>
    </tr>
    <tr>
      <th>Son of Sons</th>
      <th><img src="images/chart_fitness_sons.PNG" width="400"></th>
    </tr>
  </tbody>
</table></div>

> The number of individuals are 10. A small number of individual is selected to emphasize more on crossover than mutation.
>
>The direction is left because is one of the hardest direction using the specified board.
>
>The mutation rate is 50%.

<div style="text-align:center"><table>
    <thead>
      <tr>
          <th>Crossover</th>
          <th>Random</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <th colspan="2">Generation</th>
            <th>1</th>
            <th>5</th>
            <th>10</th>
            <th>15</th>
            <th>25</th>
            <th>50</th>
            <th>75</th>
            <th>100</th>
        </tr>
        <tr>
            <th rowspan="4">Parents</th>
            <th>2</th>
            <td>-343.77</td>
            <td>-324.16</td>
            <td>-294.3</td>
            <td>-267.43</td>
            <td>-214.48</td>
            <td>-66.77</td>
            <td>55.47</td>
            <td>135.001</td>
        </tr>
        <tr>
            <th>5</th>
            <td>-344.018</td>
            <td>-323.073</td>
            <td>-292.08</td>
            <td>-264.93</td>
            <td>-211.84</td>
            <td>-73.76</td>
            <td>51.46</td>
            <td>152.49</td>
        </tr>
        <tr>
            <th>10</th>
            <td>-344.26</td>
            <td>-328.76</td>
            <td>-290.95</td>
            <td>-252.49</td>
            <td>-160.93</td>
            <td>-2.95</td>
            <td>115.93</td>
            <th>219.77</th>
        </tr>
    </tbody>
</table></div>
<div style="text-align:center"><table>
    <thead>
      <tr>
          <th>Crossover</th>
          <th>Son of Sons</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <th colspan="2">Generation</th>
            <th>1</th>
            <th>5</th>
            <th>10</th>
            <th>15</th>
            <th>25</th>
            <th>50</th>
            <th>75</th>
            <th>100</th>
        </tr>
        <tr>
            <th rowspan="4">Parents</th>
            <th>2</th>
            <td>-344.99</td>
            <td>-329.86</td>
            <td>-293.93</td>
            <td>-250.46</td>
            <td>-194.88</td>
            <td>-31.87</td>
            <td>85.12</td>
            <td>171.18</td>
        </tr>
        <tr>
            <th>5</th>
            <td>-344.25</td>
            <td>-328.62</td>
            <td>-302.38</td>
            <td>-275.8</td>
            <td>-184.56</td>
            <td>-47.95</td>
            <td>59.931</td>
            <td>124.26</td>
        </tr>
        <tr>
            <th>10</th>
            <td>-344.24</td>
            <td>-326.37</td>
            <td>-292.24</td>
            <td>-253.37</td>
            <td>-186.69</td>
            <td>-27.84</td>
            <td>77.43</td>
            <th>176.805</th>
        </tr>
    </tbody>
</table></div>


From these results we can conclude:
* For both crossovers, the best results was given on the maximum amount of parents. That's because all the population gives information to create a new individual.
* However, this configuration (maximum amount of parents) can't be use in real solutions that need hundreds of individuals.
* Both crossovers did it pretty the same but Random did it better at the end. That's because Random crossover leaves more *"clean"* the passed information, meanwhile on Sons of sons crossover there can be details that the sons don't pass to the grandson.
* However, Son of sons can produce the same results using the two parents or the total of them.

## Unit Testing:

For this project we created unit testing for every function that had certain relevance on the algorithm. All the tests can be located at [unit_tests](../master/tec/ic/ia/pc2/g07/unit_tests/) were every test is documented with an objective, tested function and desired outputs.
