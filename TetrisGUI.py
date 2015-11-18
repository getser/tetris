import Tkinter as tk
import time

import TetrisClass as tcg

# Field dimensions
field_height = 30
field_width = 10

BLOCK_elem_width = 20

score = 0

WIDTH = field_width * BLOCK_elem_width
HEITH = field_height * BLOCK_elem_width

field = tcg.pole(field_height, field_width)

# field.run()# test string

# field.current_fig = field.curr_fig() # test string
# print 'field.current_fig' # test string
# print field.current_fig # test string
# print 'field.next_fig' # test string
# print field.next_fig # test string
# field.current_pos = field.start_pos(field.current_fig) # test string
# print 'field.current_pos' # test string
# print field.current_pos # test string



str_wind_size = str(field_width * BLOCK_elem_width + 40) + \
                    'x' + str(field_height * BLOCK_elem_width + 80)
root = tk.Tk()  # defines the main window, assigned variable name 'root'

root.geometry(str_wind_size+"+600+200")

# """
 # creates window 600WIDTH x 800HEITH pixels that is offset 230 pix in x and
 # 180 pix in y from upper left corner of YOUR window.  To see the benefit
 # of the optional '+230+180' code comment out root.geometry(...) above
 # and uncomment the next line and note the new window is too high and left
  # """
# root.geometry(str_wind_size)

frame1 = tk.Frame(root)

frame1.grid(row = 0, column = 0)

canvas = tk.Canvas(root, width = field_width*BLOCK_elem_width, \
                   height = field_height*BLOCK_elem_width, bg = "#1C1C1C")
canvas.grid(row = 2, column = 0)

# #canvas.pack(fill='both', expand=True)

label1 = tk.Label(frame1, text = "Tetris").grid(row=0,column=0, sticky="nw")
label2 = tk.Label(frame1, text = "Your current score is: " + str(score)).grid(row=0,column=1, sticky="nw")

FILL_NEXT_BLOCK_CIRCLES = "grey"   # color fill for unselected circles
FILL_BLOCK_CIRCLES = "green"   # color fill for unselected circles
FILL_POLE_CIRCLES = "blue"   # color fill for unselected circles

# ball = canvas.create_oval( (WIDTH - BLOCK_elem_width)/2, 0, (WIDTH + BLOCK_elem_width)/2, BLOCK_elem_width, width = 2, fill = FILL_CIRCLES)
# rectang = canvas.create_rectangle(80, 80, 120, 120, fill="blue")

def leftKey(event):
    print "< key pressed"
    if field.current_pos:
        field.move_figure('left')
    
def rightKey(event):
    print "< key pressed"
    if field.current_pos:
        field.move_figure('right')
    
def upKey(event):
    print "^ key pressed"
    if field.current_fig:
        field.current_fig.rotate_r()
    
def downKey(event):
    print "Down key pressed"    
    if field.current_pos:
        field.run_down()
        
def spKey(event):
    print "_____ key pressed"
    if field.current_fig:
        field.current_fig, field.next_fig = field.next_fig, field.current_fig 

frame1.focus_set()


def paint_pole():
    #print "Painting pole"
    #ball = canvas.create_oval(((15 - 1) * BLOCK_elem_width)/2, 0 * BLOCK_elem_width,((15 + 1) * BLOCK_elem_width)/2,(0 + 1) * BLOCK_elem_width, width = 2, fill = FILL_POLE_CIRCLES)
    block = field.get_copy_grid()
    for row in xrange(len(block)):
        for col in xrange(len(block[0])):
            paint_pos_row = row
            paint_pos_col = col            
            if block[row][col] == 1:
                ball = canvas.create_oval(((paint_pos_col) * BLOCK_elem_width),\
                                             paint_pos_row * BLOCK_elem_width,\
                                           ((paint_pos_col + 1) * BLOCK_elem_width),\
                                            (paint_pos_row + 1) * BLOCK_elem_width,\
                                             width = 2, fill = FILL_POLE_CIRCLES)
            else:
                ball = canvas.create_rectangle(((paint_pos_col) * BLOCK_elem_width),\
                                             paint_pos_row * BLOCK_elem_width,\
                                           ((paint_pos_col + 1) * BLOCK_elem_width),\
                                            (paint_pos_row + 1) * BLOCK_elem_width,\
                                             width = 2, fill = "#1C1C1C")


def paint_curr_figure():
    # ball = canvas.create_oval(((15 - 1) * BLOCK_elem_width)/2 + 30, 0 * BLOCK_elem_width,((15 + 1) * BLOCK_elem_width)/2 + 30,(0 + 1) * BLOCK_elem_width, width = 2, fill = FILL_BLOCK_CIRCLES)
    #print "Paint c_f"                                                
    if field.current_fig:
        block = field.current_fig.get_figure()
        for row in xrange(len(block)):
            for col in xrange(len(block[0])):
                if block[row][col] == 1:
                    paint_pos_row = field.current_pos[0] + row
                    paint_pos_col = field.current_pos[1] + col
                    ball = canvas.create_oval( ((paint_pos_col) * BLOCK_elem_width), \
                                                paint_pos_row * BLOCK_elem_width, \
                                                ((paint_pos_col + 1) * BLOCK_elem_width), \
                                                (paint_pos_row + 1) * BLOCK_elem_width, \
                                                width = 2, fill = FILL_BLOCK_CIRCLES)
                                               
def paint_next_figure():
    #ball = canvas.create_oval(((15 - 1) * BLOCK_elem_width)/2-30, 0 * BLOCK_elem_width,((15 + 1) * BLOCK_elem_width)/2-30,(0 + 1) * BLOCK_elem_width, width = 2, fill = FILL_NEXT_BLOCK_CIRCLES)
    #print "Paint n_f" 
    if field.next_fig:
        block = field.next_fig.get_figure()
        for row in xrange(len(block)):
            for col in xrange(len(block[0])):
                if block[row][col] == 1:
                    paint_pos_row = row
                    paint_pos_col = field_width + col
                    ball = canvas.create_oval( ((paint_pos_col) * BLOCK_elem_width * 0.7), \
                                                paint_pos_row * BLOCK_elem_width * 0.7, \
                                                ((paint_pos_col + 1) * BLOCK_elem_width * 0.7), \
                                                (paint_pos_row + 1) * BLOCK_elem_width * 0.7, \
                                                width = 2, fill = FILL_NEXT_BLOCK_CIRCLES)                                                

def game_play():
    global score

#    global field                                            
#    print 'Started'
#    field = tcg.pole(field_height, field_width)
    
    while True:
        
        print "Runing" 
        field.current_fig = field.curr_fig()
        field.current_pos = field.start_pos(field.current_fig)
        d_move = 'down'
        while field.state == "run":
            field.move_figure(d_move)
            
            
            frame1.bind('<Left>', leftKey)
            frame1.bind('<Right>', rightKey)
            frame1.bind('<Up>', upKey)
            frame1.bind('<Down>', downKey)
            frame1.bind('<space>', spKey)
            
            paint_pole()
            paint_curr_figure()
            paint_next_figure()

            if field.state != "run": 
                continue
            canvas.update()
            
        else:
            field.insert_figure()
            curr_count = field.clear_full_lines()
            score = curr_count * 20
            field.state = "run"
            canvas.update()
        
        label2 = tk.Label(frame1, text = "Your current score is: " + str(score)).grid(row=0,column=1, sticky="nw")
        time.sleep(0.01)

#        canvas.update()

canvas.update()        
Button1 = tk.Button(frame1,text = "New game", command = game_play).grid(row = 1,column = 0, sticky = "we")
#Button1.pack()        
               
root.mainloop()