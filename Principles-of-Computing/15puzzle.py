"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui


def position_tile(puzzle, solved_row, solved_col,move_string = None):
    """
    puzzle helper function
    """
    if move_string != None :
        #print move_string
        puzzle.update_puzzle(move_string)
    cur_row,cur_col = puzzle.current_position(solved_row,solved_col)
    zero_row,zero_col = puzzle.current_position(0,0)
    return cur_row,cur_col,zero_row,zero_col


def move_zero_target(puzzle,target_row,target_col):
    """
    puzzle helper function
    """
    zero_row,zero_col = puzzle.current_position(0,0)
    #print zero_row,zero_col
    move_string =""
      
    if target_col < zero_col :
        for _ in range(target_col,zero_col) :
            move_string += 'l'
    else :
        for _ in range(zero_col,target_col) :
            move_string += 'r'
    
    for _ in range(zero_row,target_row) :
        move_string += 'd'
        
    position_tile(puzzle,target_row,target_col,move_string) 
    return move_string

def move_right_down(puzzle,target_row,target_col):  
    """
    puzzle helper function
    """
    cur_row,cur_col,_,_ = position_tile(puzzle,target_row,target_col)
    move_string =""
    while cur_col < target_col :
        if cur_row == 0 :
            cur_row,cur_col,_,_ = position_tile(puzzle,target_row,target_col,'drrul')
            move_string += 'drrul'
        else :
            cur_row,cur_col,_,_ = position_tile(puzzle,target_row,target_col,'urrdl')
            move_string += 'urrdl'
    while cur_row < target_row :
        cur_row,cur_col,_,_ = position_tile(puzzle,target_row,target_col,'druld')
        move_string += 'druld'
    return move_string
    
def move_left_down(puzzle,target_row,target_col):
    """
    puzzle helper function
    """
    cur_row,cur_col,_,zero_col = position_tile(puzzle,target_row,target_col)
    move_string =""
    while cur_col > target_col :
        if cur_row == 0 :
            cur_row,cur_col,_,_ = position_tile(puzzle,target_row,target_col,'dllur')
            move_string += 'dllur'  
        else :
            cur_row,cur_col,_,_ = position_tile(puzzle,target_row,target_col,'ulldr')
            move_string += 'ulldr'
    while cur_row < target_row :
        if cur_row == 0 :
            cur_row,cur_col,_,zero_col = position_tile(puzzle,target_row,target_col,'dluld')
            move_string += 'dluld'
            #print puzzle
        else :
            if zero_col < target_col :
                cur_row,cur_col,_,zero_col = position_tile(puzzle,target_row,target_col,'druld')
                move_string += 'druld'
            else :
                cur_row,cur_col,_,zero_col = position_tile(puzzle,target_row,target_col,'ullddruld')
                move_string += 'ullddruld'
            #print puzzle
    return move_string
                
def move_down(puzzle, target_row,target_col) :
    """
    puzzle helper function
    """
    cur_row,_,_,_ = position_tile(puzzle,target_row,target_col)
    move_string =""
    while cur_row < target_row :
        cur_row,_,_,_ = position_tile(puzzle,target_row,target_col,'lddru')
        move_string += 'lddru'
    puzzle.update_puzzle('ld')
    move_string += 'ld'
    return move_string
    
def move_to_target(puzzle,target_row,target_col) :
    """
    puzzle helper function
    """
    cur_row,cur_col = puzzle.current_position(target_row,target_col)
    move_string = ""
    for _ in range(cur_row,target_row) :
        move_string += 'u'
    if target_col < cur_col :
        for _ in range(target_col,cur_col) :
            move_string += 'r'
    else :
        for _ in range(cur_col,target_col) :
            move_string += 'l'
            
    position_tile(puzzle,target_row,target_col,move_string)
    return move_string


def move_col0_tile_right_down(puzzle,target_row,target_col) :
    """
    puzzle helper function
    """
    cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col)
    move_string =""
    
    if (cur_row,cur_col) == (target_row -1, 0) and (zero_row,zero_col) == (cur_row,1) :
        cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'l')
        move_string += 'l'
        return move_string
    
    #print cur_row,cur_col,zero_row,zero_col
    while cur_col > target_col+1 :
        if cur_row == 0 :
            cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'dllur')
            move_string += 'dllur'  
        else :
            cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'ulldr')
            move_string += 'ulldr'
    #print puzzle
    while cur_row < target_row-1 :
        if cur_row == 0 :
            if zero_row == 0 and zero_col == 1 :
                cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'ldruld')
                move_string +='ldruld'
            else : 
                cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'dluld')
                move_string += 'dluld'
        else:
            if zero_col > cur_col :
                if zero_row == cur_row and zero_col == 1 :
                    cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'ldruld')
                    move_string +='ldruld' 
                else:
                    cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'ullddruld')
                    move_string +='ullddruld'
            else:
                cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'druld')
                move_string += 'druld'
    #print puzzle
    if (zero_row,zero_col) == (cur_row-1,0) and (cur_row,cur_col) == (target_row-1,0) :
        cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'rdl')
        move_string += 'rdl'
    if (zero_row,zero_col) ==(1,1) and (cur_row,cur_col) == (1,0) :
        print puzzle,cur_row,cur_col,zero_row,zero_col
        cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col,'l')
        move_string += 'l'
    #print puzzle    
    
    cur_row,cur_col,zero_row,zero_col = position_tile(puzzle,target_row,target_col)
    if cur_row == target_row-1 and zero_col == cur_col+1 :
        cur_row,cur_col,_,zero_col = position_tile(puzzle,target_row,target_col,'ulld')
        move_string += 'ulld'
    
    return move_string 


def move_row0_right_down(puzzle,target_col) :
    """
    puzzle helper function
    """
    cur_row,cur_col,_,_ = position_tile(puzzle,0,target_col)
    move_string =""
    while cur_col < target_col-1 :
        if cur_row == 0 :
            cur_row,cur_col,_,_ = position_tile(puzzle,0,target_col,'drrul')
            move_string += 'drrul'
        else :
            cur_row,cur_col,_,_ = position_tile(puzzle,0,target_col,'urrdl')
            move_string += 'urrdl'
    while cur_row < 1 :
        cur_row,cur_col,_,_ = position_tile(puzzle,0,target_col,'druld')
        move_string += 'druld'
    return move_string
def move_row1_right_down(puzzle,target_col) :
    """
    puzzle helper function
    """
    cur_row,cur_col,zero_row,_ = position_tile(puzzle,1,target_col)
    move_string =""
    while cur_col < target_col :
        #print puzzle , move_string
        if cur_row == 0 :
            cur_row,cur_col,zero_row,_ = position_tile(puzzle,1,target_col,'drrul')
            move_string += 'drrul'
        else :
            if zero_row == 0 :
                cur_row,cur_col,zero_row,_ = position_tile(puzzle,1,target_col,'rdl')
                move_string += 'rdl'
            else :
                cur_row,cur_col,zero_row,_ = position_tile(puzzle,1,target_col,'urrdlur')
                move_string += 'urrdlur'
    while cur_row < 1 :
        cur_row,cur_col,zero_row,_ = position_tile(puzzle,1,target_col,'dru')
        move_string += 'dru'
    return move_string
    
def move_row1_left_down(puzzle,target_col) :
    """
    puzzle helper function
    """
    cur_row,cur_col,_,_ = position_tile(puzzle,1,target_col)
    move_string =""
    while cur_col > target_col :
        #print cur_col,target_col,cur_row
        if cur_row == 0 :
            cur_row,cur_col,_,_ = position_tile(puzzle,1,target_col,'dllur')
            move_string += 'dllur'  
        else :
            cur_row,cur_col,_,_ = position_tile(puzzle,1,target_col,'ulldr')
            move_string += 'ulldr'
    while cur_row < 1 :
        if cur_row == 0 :
            cur_row,cur_col,_,_ = position_tile(puzzle,1,target_col,'dlurd')
            move_string += 'dlurd'
        else :    
            cur_row,cur_col,_,_ = position_tile(puzzle,1,target_col,'ullddruld')
            move_string += 'ullddruld'        
    return move_string


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction + str(zero_col)
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction + str(zero_row)
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # replace with your code
        assert target_row > 1, "invalid input" + str(target_row)
        if self.get_number(target_row,target_col) !=0 :
            return False
        for lower_row in range(target_row+1,self.get_height()) :
            for col in range(self.get_width()) :
                if self.current_position(lower_row,col) != (lower_row,col) :
                    return False
        for col in range(target_col+1,self.get_width()) :
            if self.current_position(target_row,col) != (target_row,col) :
                return False
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert target_row > 1 and target_col > 0 , "Invalid input"

               
        cur_row,cur_col = self.current_position(target_row,target_col)
        if(cur_row,cur_col) == (target_row,target_col) :
            return ""
        
        move_string = ""
        if self.lower_row_invariant(target_row,target_col) == False :
            move_string += move_zero_target(self,target_row,target_col)
  
        #print self
        move_string += move_to_target(self,target_row,target_col)
        
        
        #print self
        cur_row,cur_col,_,zero_col = position_tile(self,target_row,target_col)
        if cur_row == target_row and cur_col == target_col and zero_col == (target_col-1) :
            return move_string
        
        if zero_col < cur_col :
            move_string += move_right_down(self,target_row,target_col)
            return move_string
        if zero_col > cur_col :
            move_string += move_left_down(self,target_row,target_col)
            return move_string
        if zero_col == cur_col :
            move_string += move_down(self,target_row,target_col)
            return move_string
    
    
    
    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert target_row > 1, "Inavalid input" + target_row
        
                
        cur_row,cur_col = self.current_position(target_row,0)
        if(cur_row,cur_col) == (target_row,0) :
            return ""
        move_string = ""
        move_string_temp =""
        cur_row,cur_col,zero_row,zero_col = position_tile(self,target_row,0)
        if target_row == cur_row + 1 and (zero_row,zero_col) == (cur_row,1) :
            cur_row,cur_col,_,zero_col = position_tile(self,target_row,0,'lruldrdlurdluurddlur')
            move_string += 'lruldrdlurdluurddlur'
            for _ in range(zero_col,self.get_width()-1):
                self.update_puzzle('r')
                move_string += 'r'
            return move_string
                    
        
        for _ in range(cur_row,target_row) :
            move_string_temp += 'u'
        for _ in range(cur_col) :
            move_string_temp += 'r'
        
        #print move_string_temp
        
        cur_row,cur_col,_,zero_col = position_tile(self,target_row,0,move_string_temp)
        #print self ,cur_row,cur_col,_,zero_col
        move_string += move_string_temp
        
        if target_row == cur_row and cur_col == 0 :
            for _ in range(zero_col,self.get_width()-1):
                self.update_puzzle('r')
                move_string += 'r'
            return move_string
       
        target_col = 0
        
        move_string += move_col0_tile_right_down(self,target_row,target_col)
        
        cur_row,cur_col,_,zero_col = position_tile(self,target_row,target_col,'ruldrdlurdluurddlur')
        move_string += 'ruldrdlurdluurddlur'
        for _ in range(zero_col,self.get_width()-1):
            self.update_puzzle('r')
            move_string += 'r'
        return move_string


    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        
        
        zero_row,zero_col = self.current_position(0,0)
        if (zero_row,zero_col) != (0,target_col):
            return False
        
        for col in range(target_col+1,self.get_width()) :
            if self.current_position(0,col) != (0,col) :
                return False
        
        for col in range(target_col,self.get_width()) :
            if self.current_position(1,col) != (1,col) :
                return False
        
        for lower_row in range(2,self.get_height()) :
            for col in range(self.get_width()) :
                if self.current_position(lower_row,col) != (lower_row,col) :
                    return False
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        
        zero_row,zero_col = self.current_position(0,0)
        if (zero_row,zero_col) != (1,target_col):
            return False
        for lower_row in range(2,self.get_height()) :
            for col in range(self.get_width()) :
                if self.current_position(lower_row,col) != (lower_row,col) :
                    return False
        for col in range(target_col+1,self.get_width()) :
            if self.current_position(1,col) != (1,col) :
                return False
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert target_col > 1 , "Invalid Input"
        cur_row,cur_col = self.current_position(0,target_col)
        move_string =""
        if (cur_row,cur_col) == (0,target_col) :
           return move_string
        cur_row,cur_col,zero_row,zero_col = position_tile(self,0,target_col)
        if zero_row < 1 :
            cur_row,cur_col,_,zero_col = position_tile(self,0,target_col,'ld')
            move_string = 'ld'
        cur_row,cur_col,zero_row,zero_col = position_tile(self,0,target_col)
        move_string_temp = ""
        if (cur_row,cur_col) == (0,target_col) :
           return move_string
        
        if cur_row == 0 :
            move_string_temp += 'u'
        if (target_col-1) < cur_col :
            for _ in range(target_col-1,cur_col) :
                move_string_temp +='r'
        else :
            for _ in range(cur_col,target_col-1) :
                move_string_temp +='l'
       
        #print move_string_temp
        cur_row,cur_col,_,zero_col = position_tile(self,0,target_col,move_string_temp)
        move_string += move_string_temp
        #print self , cur_row,cur_col,zero_col
        if zero_col < cur_col :
            move_string += move_row0_right_down(self,target_col)    
        
        if zero_col == cur_col and (cur_row,cur_col) == (1,target_col - 1 ) :
            cur_row,cur_col,_,zero_col = position_tile(self,0,target_col,'ld')
            move_string += 'ld'
        
        cur_row,cur_col,_,zero_col = position_tile(self,0,target_col,'urdlurrdluldrruld')    
        move_string += 'urdlurrdluldrruld'
        return move_string

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert target_col > 1 , "Invalid input"
        cur_row,cur_col = self.current_position(0,target_col)
        move_string =""
        if (cur_row,cur_col) == (1,target_col) :
           return move_string
        
        if self.row1_invariant(target_col) == False :
            move_string += move_zero_target(self,1,target_col)
        
        
        cur_row,cur_col,_,zero_col = position_tile(self,1,target_col)
        move_string_temp =""

        if cur_row == 0 :
            move_string_temp += 'u'
        if target_col < cur_col :
            for _ in range(target_col,cur_col) :
                move_string_temp +='r'
        else :
            for _ in range(cur_col,target_col) :
                move_string_temp +='l'
        
        cur_row,cur_col,_,zero_col = position_tile(self,1,target_col,move_string_temp)
        move_string += move_string_temp

        if cur_row == 1 and cur_col == target_col and zero_col == (target_col-1) :
            cur_row,cur_col,_,zero_col = position_tile(self,1,target_col,'ur')
            move_string += 'ur'
            return move_string
        
        if zero_col < cur_col :
            move_string += move_row1_right_down(self,target_col) 
            return move_string
        
        if zero_col > cur_col :
            move_string += move_row1_left_down(self,target_col)
            return move_string
       
        return move_string
    

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        
        # replace with your code
        if check_solved_2x2(self.clone()) :
           return ""
           
        move_string = ""
        self.update_puzzle('lu')
        move_string += 'lu'

        if check_solved_2x2(self.clone()) :
            return move_string
        while check_solved_2x2(self.clone()) != True :
            self.update_puzzle('rdlu')
            move_string += 'rdlu'
        return move_string

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
       
        # replace with your code
        
        print self
        move_string = ""
        for row in range(self.get_height()-1, 1,-1):
            for col in range(self.get_width()-1,0,-1):
                move_string += self.solve_interior_tile(row,col)
            move_string += self.solve_col0_tile(row)
        
        for col in range(self.get_width()-1,1,-1) :
            move_string += self.solve_row1_tile(col)
            move_string += self.solve_row0_tile(col)
        
        move_string += self.solve_2x2()
        return move_string
    

    
    
def check_solved_2x2(board) :
    """
    help function for 2X2
    """
    if board.get_number(0,0) != 0 :
        return False
    if board.get_number(0,1) != 1 :
        return False
    if board.get_number(1,0) != 1*board.get_width() :
        return False
    if board.get_number(1,1) != 1*board.get_width() + 1 :
        return False
    return True
    
# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))