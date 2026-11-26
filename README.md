# The Maze Problem
## Description
It's a very simple python maze solver that uses recursive backtracking to find a path from the starting point (S) to the exit (E).
## How does it work
I know its a simple program, but here is an explanation anyway.

The algorithm starts at the initial position and explores the maze in four directions including down, up, right and left.
it marks visited cells to avoid revisiting them. if it reaches a dead end, it backtracks and tries another direction.

When the exit is found, the program prints the path from the start to the exit.

## Symbols
- 'S' stands for the starting point.  
- 'E' stands for the exit.  
- '0' stands for open path.  
- '1' stands for wall.  
- '2' stands for visited cells.  

## Algorithm
this program uses Recursion, Backtracking and Depth-First Search (DPS)

## Time and space complexity
If we count R as the number of rows and C as the number of columns,  
- Time Complexity: O(R × C)  
- Space Complexity: O(R × C)  

## Possible future improvements
- Visualize the maze and the solution path.  
- Turn the maze solver into an interactive maze game.
