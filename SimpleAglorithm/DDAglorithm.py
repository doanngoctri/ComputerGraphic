from Pixel.Put_pixel import put_pixel

def DDAgloritthm(x1, y1, x2, y2,color = "white"):
    dx = x2 - x1
    dy = y2 - y1
    step = None
    if(abs(dx)>abs(dy)):
        step = abs(dx)
    else:
        step = abs(dy)
    x_inc = dx/step
    y_inc = dy/step
    for i in range(step+1):
        put_pixel(round(x1), round(y1),color)
        x1 += x_inc
        y1 += y_inc

def line(x1, y1, x2, y2,color = "white"):
    DDAgloritthm(x1, y1, x2, y2,color)

def line_point(point1,point2,color = "white"):
    DDAgloritthm(point1[0],point1[1],point2[0],point2[1],color)
