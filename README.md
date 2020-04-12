# 8-puzzle-game-solver
You may visit [mypuzzle.org/sliding](http://mypuzzle.org/sliding) for a refresher of the rules of the game.
An instance of the N-puzzle game consists of a board holding N = m^2 − 1 (m = 3, 4, 5, ...) distinct movable tiles, plus an empty space. The tiles are numbers from the set {1, …, m^2 − 1}. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it.

Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order ⟨0, 1, …, m^2 − 1⟩. The search space is the set of all possible states reachable from the initial state.

The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time. The cost of moving from one configuration of the board to another is the same and equal to one. Thus, the total cost of path is equal to the number of moves made from the initial state to the goal state.

#### Goal State:   
![image](https://user-images.githubusercontent.com/46916990/78786845-06eefd80-79c7-11ea-9e9e-7eeba858ca37.png)

## Input:

The program requires you to input the initial board configuration.  
Enter a string of integers separated by commas in row-wise manner from the board.  
For the empty space in the board, enter 0.  

#### Example:
The configuration of the following boards are:

![image](https://user-images.githubusercontent.com/46916990/78760160-5c62e480-799e-11ea-8268-738f8c680555.png)
5, 4, 8, 0, 2, 6, 7, 3, 1

![image](https://user-images.githubusercontent.com/46916990/78762198-33901e80-79a1-11ea-993f-99a3986598dd.png)
5, 2, 1, 7, 9, 0, 4, 8, 6, 12, 11, 15, 13, 10, 3, 14

## Output:
The program would print the number of moves it checks for while processing. On finding the solution, the program would terminate by printing The List of moves and the number of moves to the solution.

The board can be solved by moving the blank space on board as instructed by the program output in the List of moves.

## Sample Input and Output:
#### Initial State:  
![image](https://user-images.githubusercontent.com/46916990/78787611-3b16ee00-79c8-11ea-88f6-8a1f21f0579e.png)
#### Finding solution:  
![image](https://user-images.githubusercontent.com/46916990/78787881-a19c0c00-79c8-11ea-8fd6-0eec5a1a6536.png)
#### After applying moves:  
![image](https://user-images.githubusercontent.com/46916990/78788050-e2942080-79c8-11ea-9a7a-941872f9c3d3.png)

## Algorithm: A* heuristic search  
What is A* Search Algorithm? :[http://www.cs.cmu.edu/~cga/ai-course/astar.pdf](http://www.cs.cmu.edu/~cga/ai-course/astar.pdf)  
Heuristic function used= sum of Manhattan distance of each tile in current position to the goal state.  
What is Manhattan Distance? :[https://xlinux.nist.gov/dads/HTML/manhattanDistance.html](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html)
Admissible: Yes  
Complete: Yes  
Optimal: Yes   
