from SimpleAglorithm.DDAglorithm import line_point
from SimpleAglorithm.color import fill_color
from Transformation.transformation import *

class Form:
    def __init__(self,*arg):
        self.points = arg
        arr = []
        for i in range(0, len(self.points)-1,2):
            arr.append([self.points[i],self.points[i+1]])
        self.points = arr
        self.mid_point_x = 0
        self.mid_point_y = 0
        self.bolder_color = None
        self.isConnection = False
        self.isFill = False
    def connection(self,color = "white"):
        self.bolder_color = color
        for i in range(0,len(self.points)-1):
            line_point(self.points[i],self.points[i+1],color)
        line_point(self.points[len(self.points)-1],self.points[0],color)
        self.isconnection = True

    def isConnection(self):
        return self.isConnection

    def isFill(self):
        return self.isFill

    def fill(self,color = "white"):
        self.find_mid()
        fill_color(self.mid_point_x,self.mid_point_y,self.bolder_color,color)
        self.isFill = True

    def find_mid(self):
        sum_x = 0
        sum_y = 0
        for i in self.points:
            sum_x += i[0]
        self.mid_point_x = round(sum_x / len(self.points))
        for i in self.points:
            sum_y += i[1]
        self.mid_point_y = round(sum_y / len(self.points))

    def translation(self,x,y):
        for i in range(0,len(self.points)):
            self.points[i] = translation(self.points[i],[x,y])

    def trans_back_to_origin(self,index = 1):
        point = self.points[index-1]
        re = point.copy()
        self.translation(-point[0],-point[1])
        return re

    def clockwise_rotate(self,theta,index = None):
        ori = None
        if index != None:
            ori = self.trans_back_to_origin(index)
        for i in range(0,len(self.points)):
            self.points[i] = clockwise_rotate(self.points[i],theta)
        if index != None:
            self.translation(ori[0],ori[1])

    def anticlockwise_rotate(self,theta,index = None):
        ori = None
        if index != None:
            ori = self.trans_back_to_origin(index)
        for i in range(0,len(self.points)):
            self.points[i] = anticlockwise_rotate(self.points[i],theta)
        if index != None:
            self.translation(ori[0],ori[1])

    def reflection_x(self):
        for i in range(0,len(self.points)):
            self.points[i] = reflection_x(self.points[i])
    def reflection_y(self):
        for i in range(0,len(self.points)):
            self.points[i] = reflection_y(self.points[i])

    def scaling(self,x,y=0,index = 1):
        ori = self.trans_back_to_origin(index)
        for i in range(0,len(self.points)):
            self.points[i] = scaling(self.points[i],x,y)
        self.translation(ori[0], ori[1])