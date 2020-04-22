# Sudoku_Solver

Python sudoku solver with a tkinter GUI


# About

Initially, the tkinter GUI creates a 9x9 grid of entries, split into 9 3x3 boxes using extra spacing. The clear and solve buttons are also generated. Then the user input the intial values into the entries grid. The clear button serves to clear all the values in the cells and the soove button runs the solve function.

The solve function starts with checking the initial values, for the values being an integer between 0 and 9, that the values entered have a possibilty of giving a unique solution and also that there are no violations of the sudoku rules at the start (i.e. none of the same digit in the same row, column or box). 

The function starts to solve the sudoku by running through the empty cells in order and checks the possible values for that cell, if there is only one then the value is entered. This process is repeated until a full run through of the empty cells is performed and no more values can be entered. 

The backtracking algorithm then comes into play to finish solving the sudoku by trying the first of the possible values for a cell, then moving on and repeating untill there are no possible values for a cell. The algorithm then backtracks through the cell values it just entered untill it reaches a cell that has another possible value, it removes the current value from the list of possible values and tries the next possible value. This is repeated untill a solution is found.

Finally the solution is displayed by adding the new found cell values to the appropriate entry in the grid and displaying them in a different colour for ease of use.


# How to use

Run Sudoku_GUI.py.
Fill in the initial cells.
Click the solve button.

If you wish to solve a different sudoku then click the clear button and repeat the previous steps as required.

# Additional files

The full solving process and jsut the backtracking algorithm are repeated in seperate files for ease of reading

# Bug, feature requests and contact

If you encounter any issues, or have a feature request please open an issue, or if there is one already opened that is of the same nature please leave a comment. If you have any question about the code or anything else about this project please fell free to contact me.
