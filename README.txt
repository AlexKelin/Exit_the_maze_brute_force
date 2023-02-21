Matrix Traversal: Finding the path to the exit

This code uses recursive algorithms to find the path to the exit of a 4x10 matrix. The starting and endpoint are the top left and bottom right corners, respectively.

The code generates a random 4x10 binary matrix, where the available steps are represented by 0's, and the walls or obstacles are represented by 1's. Starting at the top-left corner, the code recursively searches for the shortest path to the bottom right corner.

The code uses a counting list to store the visited steps, which is initialized at the beginning of the code. When the code finds an available path, it appends the steps to the counting list, and when there are no further steps to take, it stops the search.

The code can output the path of steps taken to reach the exit, the distance to the exit, and the total number of steps taken. To ensure the recursion function runs smoothly without errors, the sys.setrecursionlimit function has been called to increase the recursion limit to 10000.

Note that the current implementation assumes that the matrix has a size of 4x10 and has the endpoint located at position 39, and thus may not be easily adapted to matrices of other sizes.

The program employs dynamic programming and Dijkstra's algorithm to find the route and stop changing the matrix as soon as such a path is created.

#Alex_K
