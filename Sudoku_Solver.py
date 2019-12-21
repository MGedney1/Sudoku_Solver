import time


 
grid_initial = [[5,1,7,6,0,0,0,3,4],
        [2,8,9,0,0,4,0,0,0],
        [3,4,6,2,0,5,0,9,0],
        [6,0,2,0,0,0,0,1,0],
        [0,3,8,0,0,6,0,4,7],
        [0,0,0,0,0,0,0,0,0],
        [0,9,0,0,0,0,0,7,8],
        [7,0,3,4,0,0,5,6,0],
        [0,0,0,0,0,0,0,0,0]]



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

    row_valid = all([value != x for x in grid[row]])#grid[row][x] for x in range(9)])      #Check if value violates row condition
    col_valid = all([value != grid[y][col] for y in range(9)])      #Check if value violates column condition

    if not(row_valid and col_valid):        #Returning false unless value is valid for both row and column constraints
        return False

    box_start_row,box_start_col = 3*(row//3),3*(col//3)       #Finding the position values for top left of the 3x3 box which the current test cell resides in

    for y in range(box_start_row,box_start_row + 3):        #Checking if test Value violates box condition
        for x in range(box_start_col,box_start_col + 3):
            if grid[y][x] == value:
                return False

    return True

def solve_brute(grid,row = 0,col = 0):        #Solve function with inital params for row and col set

    row, col = next_cell(grid,row,col)

    if (row == -1) and (col == -1):     #If no more cells to solve, return completed grid
        return grid

    for value in range(1,10):
        if check_valid(grid,row,col,value):
            grid[row][col] = value      #Updating the cell to the new value if it is valid

            if solve_brute(grid,row,col):     
                return grid
            grid[row][col] = 0      #Reset the current cell to unfilled for backtracking
    return False

def solve_initial(grid):
    repeat = False      #Setting a variable to repeat if grid was changed this iteration
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                possible_values = [1,2,3,4,5,6,7,8,9]       #Setting possible values before other cell's value contraints

                row_values = [grid[row][x] for x in range(9)]       #Getting values from the cells row
                col_values = [grid[y][col] for y in range(9)]       #Getting values from the cells column
                box_values = []
                box_start_row,box_start_col = 3*(row//3),3*(col//3) 
                for y in range(box_start_row,box_start_row + 3):        #Getting values from the cells box
                    for x in range(box_start_col,box_start_col + 3):
                        box_values.append(grid[y][x])

                restricted_values = row_values + col_values + box_values        #Combining to get the total list of values not allowed
                restricted_values = list(set(restricted_values))        #Removing duplicates

                restricted_values.remove(0)     #Have to remove 0 as that isnt a possible value for completed suduko

                for value in restricted_values:     #Removing the restricted values from the possible value list
                    possible_values.remove(value)

                if len(possible_values) == 1:       #If only one possible value, set that value and set repeat to true
                    grid[row][col] = possible_values[0]
                    repeat = True
    
    if repeat:      #Repeating if repeat is true
        solve_initial(grid)        
    

    return solve_brute(grid)       #If not repeating attempt brute force to check if solved and if not then finish


start = time.time()
print(solve_initial(grid_initial))
print('Time taken: '+str(time.time()-start))






