grid_initial = [                  #Setting an initial test puzzle
    [0,0,0,6,0,0,4,0,0],
    [7,0,0,0,0,3,6,0,0],
    [0,0,0,0,9,1,0,8,0],
    [0,0,0,0,0,0,0,0,0],
    [0,5,0,1,8,0,0,0,3],
    [0,0,0,3,0,6,0,4,5],
    [0,4,0,2,0,0,0,6,0],
    [9,0,3,0,0,0,0,0,0],
    [0,2,0,0,0,0,1,0,0]
]



def next_cell(grid,row,col):        #Finding the next cell to fill
    for y in range(row,9):      #Check grid from min row col values for unfilled cells (treating 0 as unfilled)
        for x in range(col,9):
            if grid[y][x] == 0:
                return y,x
    for y in range(9):      #Check entire grid for unfilled cells
        for x in range(9):
            if grid[y][x] == 0:
                return y,x
    return -1,-1        #Returns -1,-1 if all cells filled

def check_valid(grid,row,col,value):        #Checking if a test value is valid

    row_valid = all([value != grid[row][x] for x in range(9)])      #Check if value violates row condition
    col_valid = all([value != grid[y][col] for y in range(9)])      #Check if value violates column condition

    if not(row_valid and col_valid):        #Returning false unless value is valid for both row and column constraints
        return False

    box_start_row,box_start_col = 3*(row//3),3*(col//3)       #Finding the position values for top left of the 3x3 box which the current test cell resides in

    for y in range(box_start_row,box_start_row + 3):        #Checking if test Value violates box condition
        for x in range(box_start_col,box_start_col + 3):
            if grid[y][x] == value:
                return False

    return True

def solve(grid,row = 0,col = 0):        #Solve function with inital params for row and col set

    row, col = next_cell(grid,row,col)

    if (row == -1) and (col == -1):     #If no more cells to solve, return completed grid
        return grid

    for value in range(1,10):
        if check_valid(grid,row,col,value):
            grid[row][col] = value      #Updating the cell to the new value if it is valid

            if solve(grid,row,col):     
                return grid
            grid[row][col] = 0      #Reset the current cell to unfilled for backtracking
    return False


print(solve(grid_initial))




