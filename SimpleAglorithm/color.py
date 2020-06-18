from Pixel.get_color import get_pixel_color
from Pixel.Put_pixel import put_pixel
from UI.graphic import root,current_canvas
import time

def fill_color(x,y,defaultColor,fillColor = "GREEN"):
    global current_canvas
    cur_color = get_pixel_color(current_canvas,x, y)
    cur_color = cur_color.lower()
    if (cur_color!= defaultColor and  cur_color != fillColor):
        put_pixel(x, y, fillColor)
        fill_color(x + 1, y, defaultColor, fillColor)
        fill_color(x - 1, y, defaultColor, fillColor)
        fill_color(x, y + 1, defaultColor, fillColor)
        fill_color(x, y - 1, defaultColor, fillColor)
        # fill_color(x + 1, y+1, defaultColor, fillColor)
        # fill_color(x - 1, y+1, defaultColor, fillColor)
        # fill_color(x+1, y - 1, defaultColor, fillColor)
        # fill_color(x-1, y - 1, defaultColor, fillColor)