from datetime import datetime
from Pixel.Put_pixel import  put_pixel
import math
import time
def drawCircle(xc, yc, x, y,limit_w,limit_h,r,degree = 360,color = "red"):

    if degree < 90:
        if x < limit_w:
            put_pixel(xc + x, yc + y,color)
        if x > limit_h:
            put_pixel(xc + y, yc + x,color)
    else:
        put_pixel(xc + x, yc + y,color)
        put_pixel(xc + y, yc + x,color)
        if degree < 180:
            if x > limit_h:
                put_pixel(xc + x, yc - y,color)
            if x < limit_w:
                put_pixel(xc + y, yc - x,color)
        else:
            put_pixel(xc + x, yc - y,color)
            put_pixel(xc + y, yc - x,color)

            if degree < 270:

                if x < limit_w:
                    put_pixel(xc - x, yc - y,color)
                if x > limit_h:
                    put_pixel(xc - y, yc - x,color)
            else:
                put_pixel(xc - x, yc - y,color)
                put_pixel(xc - y, yc - x,color)
                if degree < 360:
                    if x > limit_h:
                        put_pixel(xc - x, yc + y,color)
                    if x < limit_w:
                        put_pixel(xc - y, yc + x,color)
                else:
                    put_pixel(xc - x, yc + y,color)
                    put_pixel(xc - y, yc + x,color)

def circle_degree(r, degree = 360,color = "red",xc=0,yc=0):
    x = 0
    y = r
    d = 3 - 2 * r
    angle = degree % 90
    limit_x = r * math.sin(angle / 180 * math.pi)
    limit_y = r * math.cos(angle / 180 * math.pi)
    drawCircle(xc, yc, x, y,limit_x,limit_y,r,degree,color)
    while (y >= x):
        x+=1
        if (d > 0):
            y-=1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        drawCircle(xc, yc, x, y,limit_x,limit_y,r,degree,color)



now = datetime.now().time()


