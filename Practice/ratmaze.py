def solveMazeUtil(maze, i, j, sol, length_column, length_row):
    
    if i < 0 or i >= length_row or j < 0 or j >= length_column or maze[i][j] == 0:
        return False
    sol[i][j] = 1
    if i == length_row-1 and j == length_column - 1:
        return True
    
    if solveMazeUtil(maze, i+1, j, sol, length_column, length_row):
        return True
    
    if solveMazeUtil(maze, i, j+1, sol, length_column, length_row):
        return True
    
    sol[i][j] = 0
    return False
    

def solveMaze(maze):
    length_column = len(maze[0])
    length_row = len(maze)
    
    sol = [[0]*length_column for _ in range(length_row)]

    if solveMazeUtil(maze, 0, 0, sol, length_column, length_row) is False:
        print(sol)
        return False
    else:
        print(sol)
        return True


maze = [ 
            [1, 0, 0, 0], 
            [1, 1, 1, 1], 
            [0, 1, 0, 1], 
            [1, 1, 0, 1] 
        ] 
               
print(solveMaze(maze))