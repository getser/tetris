import random

init_figures = {'L' : [[1,0],[1,0],[1,1]], 
            'bL' :  [[0,1],[0,1],[1,1]],
            'Z' : [[1,1,0], [0,1,0],[0,1,1]],
            'bZ' : [[0,1,1], [0,1,0],[1,1,0]],
            'T' : [[1,1,1], [0,1,0],[0,1,0]],
            'l' : [[1],[1],[1],[1]],
            'E' : [[1,0], [1,1],[1,0]],
            'O' : [[1,1],[1,1]]}

class pole(object):
    def __init__(self, height, width):
        self._h = height
        self._w = width
        self._raw_grid = [[0 for col in range(self._w)] for row in range(self._h)]
        self.next_fig = None
        self.current_fig = None
        self.state = "stop"
        self.current_pos = None

    def get_raw_grid(self):
        return self._raw_grid
        
    def get_copy_grid(self):
        return self._raw_grid[:]
        
    def get_height(self):
        return self._h
    
    def get_width(self):
        return self._w
    
    def __str__(self):
        res = ""
        for s in self.get_raw_grid():
            res += (str(s) + '\n')
        return res[:-1]
        
    def clear_full_lines(self):
        pass
        
    def curr_fig(self):
        pass
            
            
    def start_pos(self, figure):
        pass
    
    def can_move_invariant(self, figure, current_pos, direction):
        pass

        

        
class figure(object):
    pass

