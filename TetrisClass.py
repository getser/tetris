import random

init_figures = {'L' : [[1,0],[1,0],[1,1]], 
            'bL' :  [[0,1],[0,1],[1,1]],
            'Z' : [[1,1,0], [0,1,0],[0,1,1]],
            'bZ' : [[0,1,1], [0,1,0],[1,1,0]],
            'T' : [[1,1,1], [0,1,0],[0,1,0]],
            'l' : [[1],[1],[1],[1]],
            'E' : [[1,0], [1,1],[1,0]],
            'O' : [[1,1],[1,1]]}

direction_steps = {'right':(0,1), 
                   'left':(0,-1),
                   'down':(1,0)}

class pole(object):
    """
    Creates a grid "pole", where everything is running.
    Takes integers "height" and "width" as dimensions.
    Uses figure class to create figures.
    """
    def __init__(self, height, width):
        self._h = height
        self._w = width
        self._raw_grid = [[0 for col in range(self._w)] 
                             for row in range(self._h)] 
        self.next_fig = None
        self.current_fig = None
        self.state = "stop"  # indicates if current figure can move down
        self.current_pos = None

    def get_raw_grid(self):
        """
        Returns "raw" grid, which contains all elements, that became static.
        """
        return self._raw_grid
        
    def get_copy_grid(self):
        """
        Returns a copy of "raw" grid for any use.
        """
        return self._raw_grid[:]
        
    def get_height(self):
        """
        Returns height of grid for any use.
        """
        return self._h
    
    def get_width(self):
        """
        Returns width of grid for any use.
        """
        return self._w
    
    def __str__(self):
        """
        Returns a string representation of "raw" grid.
        """
        res = ""
        for s in self.get_raw_grid():
            res += (str(s) + '\n')
        return res[:-1]
        
    def clear_full_lines(self):
        """
        Clears lines of grid, which contain only ones.
        Returns integer "count" to count players score.
        """
        full_line = [1 for col in range(self._w)]
        empty_line = [0 for col in range(self._w)]
        count = 0
        if full_line not in self._raw_grid:
            return count
        else:
            for line in self._raw_grid:
                if line == full_line:
                    count += 1
                    self._raw_grid.remove(line)
                    self._raw_grid.insert(0, empty_line)
        return count
        
    def curr_fig(self):
        """
        Creates new next and current figures.
        """
        shape = init_figures[random.choice(init_figures.keys())]
        fig = figure(shape)
        rotate = random.randrange(4)
        for i in xrange(rotate):
            fig.rotate_r()
         
        if self.next_fig == None:
            self.next_fig = fig
            return self.curr_fig() #recursively creates the very first current figure
        else:
            current_fig = self.next_fig
            self.next_fig = fig
            return current_fig
            
            
    def start_pos(self, figure):
        """
        Returns start_pos - tuple of row and col of grid.
        'start_pos' is where leftmost upper corner (0.0) of current figure be placed at start.
        """
        row = 0
        col = (self._w - len(figure.get_figure()[0]))/2
        return (row, col)
    
    def can_move_invariant(self, figure, current_pos, direction):
        """
        Determines if given figure being at given position is able to move one step
        to given direction.
        If direction == "down" and figure can't move - changes game state to "stop".
        """
        tested_shape = []
        if direction == 'right':
            step = (0, 1)
            
            if current_pos[1] + len(figure.get_figure()[0]) + 1 > self._w:
                return False
                
            num_shape_cells = len(figure.get_figure())
            first_line = len(figure.get_figure()[0]) - 1 #last figure's column
                        
            tested_rows = range(len(figure.get_figure()))
            tested_cols = list(reversed(range(len(figure.get_figure()[0]))))

            for col in tested_cols:
                for row in tested_rows:
                    if figure.get_figure()[row][col] == 1:
                        if not tested_shape:
                            tested_shape.append ((row, col))
                        else:
                            to_append = True
                            for cell in tested_shape:
                                if cell[0] == row:
                                    to_append = False
                            if to_append:
                                tested_shape.append ((row, col))
            
        elif direction == 'left':
            step = (0, -1)
            
            if current_pos[1] - 1 < 0:
                return False            
            
            num_shape_cells = len(figure.get_figure())
            first_line = 0 #first figure's column

            tested_rows = range(len(figure.get_figure()))
            tested_cols = range(len(figure.get_figure()[0]))

            for col in tested_cols:
                for row in tested_rows:
                    if figure.get_figure()[row][col] == 1:
                        if not tested_shape:
                            tested_shape.append ((row, col))
                        else:
                            to_append = True
                            for cell in tested_shape:
                                if cell[0] == row:
                                    to_append = False
                            if to_append:
                                tested_shape.append ((row, col))
            
        elif direction == 'down':
            step = (1, 0)
            
            if current_pos[0] + len(figure.get_figure()) + 1 > self._h:
                self.state = "stop"
                return False            
            
            num_shape_cells = len(figure.get_figure()[0])
            first_line = len(figure.get_figure()) - 1 #last figure's row
            
            tested_rows = list(reversed(range(len(figure.get_figure()))))
#            print tested_rows
            tested_cols = range(len(figure.get_figure()[0]))
#            print tested_cols

            for row in tested_rows:
                for col in tested_cols:
                    if figure.get_figure()[row][col] == 1:
                        if not tested_shape:
                            tested_shape.append ((row, col))
                        else:
                            to_append = True
                            for cell in tested_shape:
                                if cell[1] == col:
                                    to_append = False
                            if to_append:
                                tested_shape.append ((row, col))
#                        tested_cols.remove(col)
        
        print tested_shape
        print num_shape_cells
        
        assert num_shape_cells == len(tested_shape) 
        
        for cell in tested_shape:
            tested_row = current_pos[0] + cell[0] + step[0]
            tested_col = current_pos[1] + cell[1] + step[1]
            if self._raw_grid[tested_row][tested_col] == 1:
                if direction == 'down': self.state = "stop"
                return False
                
        return True

    def move_figure(self, direction):
        """
        Tests if current figure is able to move to given direction. 
        (Uses can_move_invariant.)
        If is able to move - changes current position for a step to given direction.
        """
        if self.current_pos:
            if can_move_invariant(self.current_fig, self.current_pos, direction):
                step = direction_steps[direction]
                self.current_pos[0] += step[0]
                self.current_pos[1] += step[1]
            else:
                print '"self.current_pos" is absend' 
        
    def insert_figure(self):
        """
        Inserts current figure to "raw" grid at current position.
        """
        if self.current_pos:
            for row in xrange(len(self.current_fig.get_figure())):
                for col in xrange(len(self.current_fig.get_figure()[0])):
                    if self.current_fig.get_figure()[row][col] == 1:
                        pos_row = row + self.current_pos[0]
                        pos_col = col + self.current_pos[1]
                        assert self._raw_grid[pos_row][pos_col] == 0
                        print "trying to insert at pos:", (pos_row, pos_col)
                        self._raw_grid[pos_row][pos_col] = 1
        else:
            print '"self.current_pos" is absend' 

        

        
class figure(object):
    """
    Used to create figures for a game.
    Takes a "matrix" of figure (list of lists with '0' and '1') as argument
    """
    def __init__(self, matrix):
        self._fig = matrix
        
    def get_figure(self):
        """
        Returns a list representation figure (to make indexing, for example).
        """
        return self._fig    
        
    def __str__(self):
        """
        Returns a string representation of a figure.
        """
        res = ""
        for s in self.get_figure():
            res += (str(s) + '\n')
        return res[:-1]
        
    def rotate_r(self):
        """
        Rotates a figure 90 degree to the right.
        """
        res_rows = len(self._fig[0])
        res_cols = len(self._fig)
        res = [[0 for col in range(res_cols)] for row in range(res_rows)]
        
        for row in range(len(self._fig)):
            for col in range(len(self._fig[0])):
                res[col][(len(res[0]) - 1) - row] = self._fig[row][col]       
        self._fig = res
    
    def rotate_l(self):
        """
        Rotates a figure 90 degree to the left.
        """
        res_rows = len(self._fig[0])
        res_cols = len(self._fig)
        res = [[0 for col in range(res_cols)] for row in range(res_rows)]
        
        for row in range(len(self._fig)):
            for col in range(len(self._fig[0])):
                res[(len(res) - 1) - col][row] = self._fig[row][col]       
        self._fig = res
            

# T_fig.rotate_r()
# print T_fig
# print

#T_fig.rotate_l()
#print T_fig
#print

        
# T_fig = figure(init_figures['T'])
# print T_fig
# print


# T_fig.rotate_l()
# print T_fig  
# print

# T_fig.rotate_l()
# print T_fig
# print

# T_fig.rotate_r()
# print T_fig
# print

#T_fig.rotate_l()
#print T_fig
#print


# l_fig = figure(init_figures['l'])
# print l_fig
# print

# l_fig.rotate_l()
# print l_fig
# print

# l_fig.rotate_l()
# print l_fig
# print


        
t = pole( 40, 15 )

t.current_fig = t.curr_fig()
print t.current_fig
print
# print t.current_fig.get_figure()[0]
# print

start = t.start_pos(t.current_fig)
print start
print

#start = 36, 6
#move = 'left'
move = 'down'
print start
print move
print

print t.can_move_invariant(t.current_fig, start, move)
print
# print t.can_move_invariant(t.current_fig, start, 'right')
# print
# print t.can_move_invariant(t.current_fig, start, 'down')
# print


#print t.next_fig
#print


# t.current_fig.rotate_r()
# print t.current_fig
# print

# t.current_fig.rotate_l()
# print t.current_fig
# print

# E_fig.rotate_r()
# print E_fig
# print

#print t