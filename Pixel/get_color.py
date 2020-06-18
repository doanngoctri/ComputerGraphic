
from Pixel.Put_pixel import put_pixel,trans_x,trans_y

def get_pixel_color(canvas, x, y):
    x = trans_x(x)
    x+=1
    y = trans_y(y)
    y-=1
    ids = canvas.find_overlapping(x, y, x, y)

    if len(ids) > 0:
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        color = color.upper()
        if color != '':
            return color

    return "WHITE"

