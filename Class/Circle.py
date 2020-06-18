from Class.Form import Form
from SimpleAglorithm.circle import circle
from Transformation.transformation import *
class Circle(Form):
    def __init__(self,point_x,point_y,r):
        self.mid_point_x = point_x
        self.mid_point_y = point_y
        self.points = [[self.mid_point_x,self.mid_point_y]]
        self.r = r
        self.bolder_color = None
        self.isConnection = False
        self.isFill = False


    def connection(self,color = "white"):
        self.bolder_color = color
        circle(self.r,self.points[0][0],self.points[0][1],color)
        self.isConnection = True

    def scaling(self,t):
        self.r = round(self.r*t)

    def fill(self,color = "white"):
        self.mid_point_x = self.points[0][0]
        self.mid_point_y = self.points[0][1]
        super().fill(color)
        self.isFill = True

