"""
Clone of 2048 game.
"""

import random
import poc_2048_gui        

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # Helper function that merges a single row or column in 2048
    result_list = []
    locator = 0
    can_merge = True
    
    #Initialise result_list to be the same length as 'line' with 0's as values
    for dummy_times in range(len(line)):
        result_list.append(0)

    #Iterate through 'line' input and mutate result_list appropriately
    for dummy_num in line:
        if dummy_num != 0:
            if locator == 0: #This will only happen once, at the start of the iteration
                result_list[locator] = dummy_num
                locator += 1
            elif dummy_num == result_list[locator-1] and can_merge:
                result_list[locator-1] += dummy_num
                can_merge = False
            else:
                result_list[locator] = dummy_num
                locator += 1
                can_merge = True
    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self._rows = grid_height
        self._columns = grid_width
        self._grid = self.reset()

        up_list = []
        down_list = []
        left_list = []
        right_list = []
        for item in range(grid_width):
            up_list.append((0,item))
            down_list.append((grid_height-1,item))
        for item in range(grid_height):
            left_list.append((item,0))
            right_list.append((item,grid_width-1))

        self._grid_index = {1: up_list, 2: down_list, 3: left_list, 4: right_list}
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """ 
        #Resets the grid to be the right size, with 0's as values
        #Grid is a list of lists.
        grid = []
        for dummy_i in range(self._rows):
            grid.append([])
            for dummy_j in range(self._columns):
                grid[dummy_i].append(0)
        self._grid = grid     
        return self._grid
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        cells = self._grid
        return str(cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        grid_height = self._rows
        return grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        grid_width = self._columns
        return grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # This is the main logic method.
        # It slides all the tiles in the given direction.
        #Initialise loop duration
        loop_duration = 0
        # Get the correct offset from the dictionary
        offset = OFFSETS.get(direction)
        # Store all the initial 'origin' tiles for the move
        initial_tiles = self._grid_index.get(direction)
        has_changed = False
        do_once = 0

        # Sets the duration of the loop during which we get the associated row or column
        if direction == 1 or direction == 2:
            loop_duration = self._rows-1
        elif direction == 3 or direction == 4:
            loop_duration = self._columns-1

        # Main loop has three things it's doing:
        # 1) Accesses the list of initial 'origin' tiles, depending on direction
        # 2) Use the 'merge' function to create a list of new values
        # 3) Assign those new values to the grid
        for tile in initial_tiles:
            temp_list = []
            tile_value = self.get_tile(tile[0], tile[1])
            temp_list.append(tile_value)
            col = tile[0]
            row = tile[1]
            


            #'Get' the values in each row / column and write them to a list
            for dummy_times in range(loop_duration):
                col += offset[0]
                row += offset[1]
                tile_value = self.get_tile(col, row)
                temp_list.append(tile_value)

            # 'Merge' the values in each list
            merged_list = merge(temp_list)

            # Re-initialize the temp variables
            temp_list = []
            tile_value = self.get_tile(tile[0], tile[1])
            temp_list.append(tile_value)
            col = tile[0]
            row = tile[1]

            # Set the grid's tiles to the new values from the merged list
            for value in merged_list:
                check_tile = self.get_tile(col, row)
                self.set_tile(col, row, value)
                change_tile = self.get_tile(col, row)
                if check_tile != change_tile:
                    has_changed = True



                col += offset[0]
                row += offset[1]

        if has_changed == True and do_once == 0:
            do_once = 1
            self.new_tile()

        return self._grid

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #Choses a random tile whose value is 0. 
        #Assigns a new value to the tile.
        #This tile has a 90% chance of becoming 2, 10% chance of becoming 4
        grid = self._grid
        board_height = self.get_grid_height()
        board_width = self.get_grid_width()
        list_of_indeces = []
        list_of_values = [2,2,2,2,2,2,2,2,2,4]

        for y_index in range(board_height):
            for x_index in range(board_width):
                if grid[y_index][x_index] == 0:
                    list_of_indeces.append([y_index, x_index])

        #Returns a [Y, X] coordinate            
        random_index = random.choice(list_of_indeces)
        #Returns a random value of 2 or 4
        random_value = random.choice(list_of_values)

        self.set_tile(random_index[0],random_index[1], random_value)
        
        return self._grid
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """ 
        #Set a certain specified tile to a certain specified value
        grid = self._grid
        grid[row][col] = value
        self._grid = grid
        return self._grid

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """ 
        #Gets the value of the tile
        grid = self._grid
        return grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))