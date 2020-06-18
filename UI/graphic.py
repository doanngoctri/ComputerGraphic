from tkinter import *
from tkinter import simpledialog
from Pixel.colour import get_inverse_color
import time
root = Tk()
root.title("Computer Graphic")
width_root = root.winfo_screenwidth()
height_root = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(width_root, height_root))
color_background = "#ffffff"

width = int(width_root*0.7)
height = height_root

width_pixel = 5
mid_w = 0
mid_h = 0


current_canvas = Canvas(root,width = width,height = height)
current_canvas.grid(column = 0,row = 0)

re = current_canvas.create_rectangle(0,0,width,height,fill = "white",outline = "white")
other = Label(root).grid(column = 1,row = 0)

axis = True

def adjust(width_pixel):
    global mid_h
    global mid_w
    mid_w = int(int(width / 2) / width_pixel) * width_pixel
    mid_h = int(int(height / 2) / width_pixel) * width_pixel

adjust(width_pixel)

def pop_up_adj():
    s = simpledialog.askstring("Pixel","Type your value here")
    if s != None:
        global width_pixel
        width_pixel = int(s)
        adjust(width_pixel)
        clearEverything()
        global axis
        axis = True
        white_grid()
        coordinate()


def coordinate():
    color = "#669999"
    global current_canvas
    canvas = current_canvas
    global axis
    if axis :
        canvas.create_rectangle(0, mid_h, width, mid_h - width_pixel, fill=color)
        canvas.create_rectangle(mid_w, 0, mid_w + width_pixel, height, fill=color)
    else :
        rm_coordinate()
    axis = not(axis)
def rm_coordinate():
    global color_background
    if color_background == "#000000":
        black_blank()
    else:
        white_grid()


def clearEverything():
    global current_canvas
    canvas = current_canvas
    canvas.delete("all")
    # grid_display()

def black_blank():
    global current_canvas
    global color_background
    current_canvas.create_rectangle(0, 0, width, height, fill="#000000", outline="#000000")
    color_background = "#000000"
def white_grid():
    global current_canvas
    current_canvas.create_rectangle(0, 0, width, height, fill="#ffffff", outline="#ffffff")
    for i in range(0, height, width_pixel):
        current_canvas.create_rectangle(0, i, width, i+1, fill="#ffffff",outline="#f0f0f0")
    for i in range(0, width, width_pixel):
        current_canvas.create_rectangle(i, 0, i+1, height, fill="#ffffff",outline="#f0f0f0")
    global color_background
    color_background = "#ffffff"

# def grid_display(color = "black"):
#     global current_canvas
#     canvas = current_canvas
#     global grid
#     if grid:
#
#     grid = not (grid)

def refresh_canvas(second,intervalt = 1):
    global current_canvas
    canvas = current_canvas
    flag = False
    if intervalt == 0:
        flag = True
    while intervalt != 0 or flag:
        time.sleep(second)
        canvas.update()
        clearEverything()
        intervalt -= 1

#menu
my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File",menu=file_menu)
file_menu.add_command(label = "Exit",command=root.quit)

option_menu = Menu(my_menu)
my_menu.add_cascade(label = "Option",menu=option_menu)
option_menu.add_command(label = "Pixel",command=pop_up_adj)
option_menu.add_command(label = "Clear",command=clearEverything)

view_menu = Menu(my_menu)
my_menu.add_cascade(label = "View",menu=view_menu)
view_menu.add_command(label = "Coordinate Axis",command=coordinate)
view_menu.add_command(label = "Black blank",command=black_blank)
view_menu.add_command(label = "Grid",command=white_grid)


white_grid()
#rm_coordinate()

