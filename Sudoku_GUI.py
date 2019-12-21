from tkinter import Frame,Entry,Button,messagebox

class app(Frame):
    def __init__(self):     #Initialising
        Frame.__init__(self)
        self.grid()
        self.create_grid()      #Creating the sudoku grid
        self.create_buttons()       #Creating the reset and solve buttons

    
    def create_grid(self):
        self.cells = {}       #Creating a dict for the cells in the grid
        self.tableheight = 9
        self.tablewidth = 9
        counter = 0
        for row in range(self.tableheight):     #Iterating through the rows and columns creating entries
            for col in range(self.tablewidth):
                self.cells[counter] = Entry(self,width=5,justify='center')      #Creating the Entry
                if (counter % 3==2):        #Creating extra vertical breaks to split into 3x3 boxes
                    pad_x = (3,10)
                else:
                    pad_x = 3
                 
                if ((counter // 9) == 2) or ((counter // 9) == 5):      #Creating extra horizontal breaks to split into 3x3 boxes
                    pad_y = (3,10)
                else:
                    pad_y = 3

                if (counter % 9) == 0:      #Extra space to the sides of the board
                    pad_x = (25,3)
                elif (counter % 9) == 8:
                    pad_x = (3,25)

                if (counter // 9) == 0:
                    pad_y = (25,3)
                elif (counter // 9) == 8:
                    pad_y = (3,25)

                
                self.cells[counter].grid(row=row,column=col,padx=pad_x,pady=pad_y)      #Setting in a grid and adding padding
                counter+=1

        self.master.bind('<Up>',self.up)        #Key bindings to move between cells
        self.master.bind('<Left>',self.left)
        self.master.bind('<Right>',self.right)
        self.master.bind('<Down>',self.down)
                
    def up(self,event):
        current_cell = str(self.focus_get())[12:]       #Splitting the string of default entry names to get the number
        if len(current_cell) == 0:      #Naming started with no number at the end so setting to 1
            current_cell = '1'
        current_cell = int(current_cell) - 1        #Getting the current cell index
        row = current_cell//9       #Finding the row the cell is on
        if row == 0:        #Getting new row
            new_row = 8
        else:
            new_row = row -1
        next_cell = new_row*9 + (current_cell % 9)      #Getting index of target cell       
        self.cells[next_cell].focus_set()       #Setting focus to new entry 
    
    def left(self,event):
        current_cell = str(self.focus_get())[12:]       #Splitting the string of default entry names to get the number
        if len(current_cell) == 0:      #Naming started with no number at the end so setting to 1
            current_cell = '1'
        current_cell = int(current_cell) - 1        #Getting the current cell index
        if (current_cell == 0):     #Index of new entry
            next_cell = 80
        else:
            next_cell = current_cell - 1
        self.cells[next_cell].focus_set()       #Setting focus to new entry 

    def right(self,event):
        current_cell = str(self.focus_get())[12:]       #Splitting the string of default entry names to get the number
        if len(current_cell) == 0:      #Naming started with no number at the end so setting to 1
            current_cell = '1'
        current_cell = int(current_cell) - 1        #Getting the current cell index
        if (current_cell == 80):        #Index of new entry
            next_cell = 0
        else:
            next_cell = current_cell + 1        
        self.cells[next_cell].focus_set()       #Setting focus to new entry 

    def down(self,event):
        current_cell = str(self.focus_get())[12:]       #Splitting the string of default entry names to get the number
        if len(current_cell) == 0:      #Naming started with no number at the end so setting to 1
            current_cell = '1'
        current_cell = int(current_cell) - 1        #Getting the current cell index
        row = current_cell//9       #Finding the row the cell is on
        if row == 8:        #Getting new row
            new_row = 0
        else:
            new_row = row + 1
        next_cell = new_row*9 + (current_cell % 9)      #Getting index of target cell       
        self.cells[next_cell].focus_set()       #Setting focus to new entry 

    def create_buttons(self):       #Creating buttons
        self.reset = Button(self,text='Reset',command=self.reset_values)        #Reset
        self.reset.grid(row=11,column=1)    
        self.solve = Button(self,text='Solve',command=self.solve_sudoku)        #Solve
        self.solve.grid(row = 11, column=7)
        
    
    def reset_values(self):     #Reset entries
        for counter in range(81):
            self.cells[counter].delete(0,'end')
            self.cells[counter].configure(fg='black')

    def check_values(self):     #Checks cell values are allowed
        self.fetch_values ()        #Fetching values
        self.cells_given = 0
        for x in self.cells_list:       #Checking the number of cells intially filled is greater than 17 to allow for unique solution
            if x != 0:
                self.cells_given += 1
        if (self.cells_given < 17):         #Less than 17 enteries results in non unique solution
            messagebox.showwarning('Non Unique Solution','Entering less that 17 initial cells means the solution can not be unique')
        self.different_values_given = len(list(set(self.cells_list)))       #Getting length of the list of unique cell values given
        if self.different_values_given < 9:     #Checking the number of different values given is greater than 9 (8 for unique sudoku but this also counts 0)
            messagebox.showwarning('Non Unique Solution','Entering less than 8 different intial values means the solution can not be unique.')
        self.convert_to_board()     #Getting the list of cell values in a board format
        for row in range(9):        #iterating through each cell
            for col in range(9):
                value = self.board[row][col]
                if value!=0:
                    if (self.check_valid(row,col,value)):     #Check for violations of sudoku rules at start
                        print(row,col)
                        messagebox.showerror('Entry Error','Initial board contains violation of Sudoku rules')

    def fetch_values(self):     #Gets cell values from board
        self.cells_list = list(self.cells.values())     #Getting the cell values as a list
        for x in range(81):
            self.cells_list[x] = self.cells_list[x].get()
            if (self.cells_list[x] not in ['','0','1','2','3','4','5','6','7','8','9']):  #Checking the cell values are allowed
                messagebox.showerror('Value Error','Please ensure all enteries are between 1-9.\nLeave empty cells blank.')
                self.reset_values()
                raise Sudoku_Error()
            if (self.cells_list[x] == ''):      #Converting empty cells to 0s
                self.cells_list[x] = '0'
                self.cells[x].configure(fg='blue')
            self.cells_list[x] = int(self.cells_list[x])        #Converting cell values from strings to integers
    
    def convert_to_board(self):     #Converting from a list length 81 to list of 9 lists length 9
        self.board = [] 
        for iteration in range(9):  #Iterating through different rows
            row = []
            for pos in range(iteration*9,(iteration+1)*9):      #Iterating through different columns in the set row
                row.append(self.cells_list[pos])        #Appending to the current rows list
            self.board.append(row)      #Appending row list to the board
            
    def check_valid(self,row,col,value):        #Checking if a test value is valid

        row_valid = all([value != x for x in self.board[row]])#grid[row][x] for x in range(9)])      #Check if value violates row condition
        col_valid = all([value != self.board[y][col] for y in range(9)])      #Check if value violates column condition

        if not(row_valid and col_valid):        #Returning false unless value is valid for both row and column constraints
            return False

        box_start_row,box_start_col = 3*(row//3),3*(col//3)       #Finding the position values for top left of the 3x3 box which the current test cell resides in

        for y in range(box_start_row,box_start_row + 3):        #Checking if test value violates box condition
            for x in range(box_start_col,box_start_col + 3):
                if self.board[y][x] == value:
                    return False

        return True
    
    def solve_sudoku(self):        #Solving
        self.check_values()     #Checking intitial 
        self.solve_initial()        #Initial solving algorithm
        self.publish_answer()       #Publishing results
        

    def solve_initial(self):
        repeat = False      #Setting a variable to repeat if grid was changed this iteration
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    possible_values = [1,2,3,4,5,6,7,8,9]       #Setting possible values before other cell's value contraints

                    row_values = [self.board[row][x] for x in range(9)]       #Getting values from the cells row
                    col_values = [self.board[y][col] for y in range(9)]       #Getting values from the cells column
                    box_values = []
                    box_start_row,box_start_col = 3*(row//3),3*(col//3) 
                    for y in range(box_start_row,box_start_row + 3):        #Getting values from the cells box
                        for x in range(box_start_col,box_start_col + 3):
                            box_values.append(self.board[y][x])

                    restricted_values = row_values + col_values + box_values        #Combining to get the total list of values not allowed
                    restricted_values = list(set(restricted_values))        #Removing duplicates

                    restricted_values.remove(0)     #Have to remove 0 as that isnt a possible value for completed suduko

                    for value in restricted_values:     #Removing the restricted values from the possible value list
                        possible_values.remove(value)

                    if len(possible_values) == 1:       #If only one possible value, set that value and set repeat to true
                        self.board[row][col] = possible_values[0]
                        repeat = True
    
        if repeat:      #Repeating if repeat is true
            self.solve_initial()        
    

        if (self.solve_brute()):      #If not repeating attempt brute force to check if solved and if not then finish
            return

    def solve_brute(self,row = 0,col = 0):        #Solve function with inital params for row and col set

        row, col = self.next_cell(row,col)

        if (row == -1) and (col == -1):     #If no more cells to solve, return completed grid
            return True

        for value in range(1,10):
            if self.check_valid(row,col,value):
                self.board[row][col] = value      #Updating the cell to the new value if it is valid

                if self.solve_brute(row,col):     
                    return True
                self.board[row][col] = 0      #Reset the current cell to unfilled for backtracking
        return False

    def next_cell(self,row,col):        #Finding the next cell to fill
        for y in range(row,9):      #Check grid from min row col values for unfilled cells (treating 0 as unfilled)
            for x in range(col,9):
                if self.board[y][x] == 0:
                    return y,x
        for y in range(9):      #Check entire grid for unfilled cells
            for x in range(9):
                if self.board[y][x] == 0:
                    return y,x
        return -1,-1        #Returns -1,-1 if all cells filled

    def publish_answer(self):
        self.answer_cells = []
        for y in range(9):
            for x in range(9):
                self.answer_cells.append(self.board[y][x])
        for pos in range(81):
            if (self.cells_list[pos] == 0):
                self.cells[pos].insert(0,self.answer_cells[pos])


class Sudoku_Error(Exception):
    pass   
        

prog = app()
prog.master.title('Sudoku Solver')
prog.mainloop()