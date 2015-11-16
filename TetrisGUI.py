import Tkinter as tk
import time

import TetrisClass as tcg

# Field dimensions
field_height = 40
field_width = 15

BLOCK_elem_width = 20

WIDTH = field_width * BLOCK_elem_width
HEITH = field_height * BLOCK_elem_width

field = tcg.pole(field_height, field_width)


str_wind_size = str(field_width * BLOCK_elem_width) + 'x' + str(field_height * BLOCK_elem_width)
root = tk.Tk()  # defines the main window, assigned variable name 'root'

root.geometry(str_wind_size+"+100+100")

# """
 # creates window 600WIDTH x 800HEITH pixels that is offset 230 pix in x and
 # 180 pix in y from upper left corner of YOUR window.  To see the benefit
 # of the optional '+230+180' code comment out root.geometry(...) above
 # and uncomment the next line and note the new window is too high and left
  # """
# root.geometry(str_wind_size)

frame1.grid(row = 0, column = 0)

canvas = Canvas(root, width = field_width*BLOCK_elem_width, height = field_height*BLOCK_elem_width, bg = "#1C1C1C")
canvas.grid(row = 2, column = 0)

# #canvas.pack(fill='both', expand=True)

label1 = Label(frame1, text = "Tetris").grid(row=0,column=0, sticky="nw")
Button1 = Button(frame1,text = "New game").grid(row = 1,column = 0, sticky = "we")


FILL_BLOCK_CIRCLES = "green"   # color fill for unselected circles
FILL_POLE_CIRCLES = "blue"   # color fill for unselected circles

# ball = canvas.create_oval( (WIDTH - BLOCK_elem_width)/2, 0, (WIDTH + BLOCK_elem_width)/2, BLOCK_elem_width, width = 2, fill = FILL_CIRCLES)
# rectang = canvas.create_rectangle(80, 80, 120, 120, fill="blue")

def leftKey(event):
    if field.current_pos:
        field.move_figure('left')
    
def rightKey(event):
    if field.current_pos:
        field.move_figure('right')
    
def upKey(event):
    if field.current_fig:
        field.current_fig.rotate_r()
    
def downKey(event):
    global speed
    if field.current_pos:
        time.sleep(0.25)
        
def spKey(event):
    if field.current_fig:
        field.current_fig, field.next_fig = field.next_fig, field.current_fig 


frame1.focus_set()

block = field.get_copy_grid()
for row in xrange(len(block)):
    for col in xrange(len(block[0])):
        if block[row][col] == 1:
            paint_pos_row = field.current_pos[0] + row
            paint_pos_col = field.current_pos[0] + col
            ball = canvas.create_oval(((paint_pos_col - 1) * BLOCK_elem_width)/2,\
                                         paint_pos_row * BLOCK_elem_width,\
                                       ((paint_pos_col + 1) * BLOCK_elem_width)/2,\
                                        (paint_pos_row + 1) * BLOCK_elem_width,\
                                         width = 2, fill = FILL_POLE_CIRCLES)   

if field.current_fig:
    block = field.current_fig.get_figure()
    for row in xrange(len(block)):
        for col in xrange(len(block[0])):
            if block[row][col] == 1:
                paint_pos_row = field.current_pos[0] + row
                paint_pos_col = field.current_pos[0] + col
                ball = canvas.create_oval( ((paint_pos_col - 1) * BLOCK_elem_width)/2, \
                                            paint_pos_row * BLOCK_elem_width, \
                                            ((paint_pos_col + 1) * BLOCK_elem_width)/2, \
                                            (paint_pos_row + 1) * BLOCK_elem_width, \
                                            width = 2, fill = FILL_BLOCK_CIRCLES)

while True:
#    block_pos [1] +=1
    field.current_fig.run()
    time.sleep(0.025)

#    canvas.move(ball, 0, 1)
    
    frame1.bind('<Left>', leftKey)
    frame1.bind('<Right>', rightKey)
    frame1.bind('<Up>', upKey)
    frame1.bind('<Down>', downKey)
    frame.bind('<space>', spKey)
#    if block_pos [1] + BLOCK_elem_width + 200 == HEITH:
#        break
    
    canvas.update()

 mainloop()

