import math
from UI.graphic import width_pixel,mid_w,mid_h
from UI.graphic import current_canvas
#tạo độ trục ra pixel
def trans_x(x):
    return (mid_w + x*width_pixel)
def trans_y(y):
    return (mid_h - y*width_pixel)

def rm_pixel(x,y,color = "black"):
    global current_canvas
    canvas = current_canvas
    put_pixel(x,y,canvas, color)

#pixel ra tọa độ trục
def trans_x_back(x): 
    return math.floor((x-mid_w)/width_pixel)
def trans_y_back(y):
    return math.floor((mid_h-y)/width_pixel)

def put_pixel(x, y,color = 'red'):
    x = trans_x(x)
    y = trans_y(y)
    global current_canvas
    canvas = current_canvas
    canvas.create_rectangle(x, y, x + width_pixel, y - width_pixel, fill=color, outline = color)