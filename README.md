# 8-puzzle-game-solver
You may visit mypuzzle.org/sliding for a refresher of the rules of the game.
An instance of the N-puzzle game consists of a board holding N = m^2 − 1 (m = 3, 4, 5, ...) distinct movable tiles, plus an empty space. The tiles are numbers from the set {1, …, m^2 − 1}. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it.

Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order ⟨0, 1, …, m^2 − 1⟩. The search space is the set of all possible states reachable from the initial state.

The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time. The cost of moving from one configuration of the board to another is the same and equal to one. Thus, the total cost of path is equal to the number of moves made from the initial state to the goal state.

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
The program would print all the board states it checks. On finding the solution, the program would terminate printing two lines:
Moves: "List of moves"
Number of Moves: 

The board can be solved by moving the blank space on board as instructed by the program output in moves.

## Sample Input and Output:
![image](https://user-images.githubusercontent.com/46916990/78764885-d1391d00-79a4-11ea-9c76-d0a783fa93a1.png)


Enter board state    
1,2,5,3,4,0,6,7,8   
[1, 2, 5]   
[3, 4, 0]   
[6, 7, 8]   
 
[1, 2, 0]   
[3, 4, 5]   
[6, 7, 8]   
 
[1, 2, 5]   
[3, 4, 8]   
[6, 7, 0]   
 
[1, 2, 5]   
[3, 0, 4]   
[6, 7, 8]   
 
[1, 0, 2]    
[3, 4, 5]    
[6, 7, 8]    
 
[1, 2, 5]    
[3, 4, 8]      
[6, 0, 7]   
 
[1, 0, 5]   
[3, 2, 4]    
[6, 7, 8]    
 
[1, 2, 5]    
[3, 7, 4]     
[6, 0, 8]    
 
[1, 2, 5]    
[0, 3, 4]   
[6, 7, 8]    
 
[1, 4, 2]    
[3, 0, 5]    
[6, 7, 8]    
 
[0, 1, 2]    
[3, 4, 5]    
[6, 7, 8]     
 
Moves: ['Up', 'Left', 'Left']   
Number of Moves: 3
