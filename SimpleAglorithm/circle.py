from Pixel.Put_pixel import put_pixel

def drawCircle(xc, yc, x, y,color):

    put_pixel(xc+x, yc+y,color)
    put_pixel(xc-x, yc+y,color)
    put_pixel(xc+x, yc-y,color)
    put_pixel(xc-x, yc-y,color)
    put_pixel(xc+y, yc+x,color)
    put_pixel(xc-y, yc+x,color)
    put_pixel(xc+y, yc-x,color)
    put_pixel(xc-y, yc-x,color)

def circle(r,xc=0,yc=0,color = "while"):
    x = 0
    y = r
    d = 3 - 2 * r
    # qua = int(degree/90) * 90
    # degree = degree - qua
    # limit = r*math.sin(degree/180*math.pi)
    drawCircle(xc, yc, x, y,color)
    while (y >= x):
        x+=1
        if (d > 0):
            y-=1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        drawCircle(xc, yc, x, y,color)

