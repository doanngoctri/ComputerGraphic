import numpy as np
import math
def clockwise_rotate(matrix,theta):
    t = theta / 180 * math.pi
    cal = np.array(((math.cos(t),math.sin(t)),(math.sin(t),math.cos(t))))
    matrix = np.array(matrix)
    matrix = matrix.dot(cal)
    for i in range(0,len(matrix)):
        matrix[i] = round(matrix[i])
    return matrix.tolist()


def anticlockwise_rotate(matrix,theta):
    t = theta * math.pi / 180
    cal = np.array(((math.cos(t), math.sin(t)), (-math.sin(t), math.cos(t))))
    matrix = np.array(matrix)
    matrix = matrix.dot(cal)
    for i in range(0,len(matrix)):
        matrix[i] = round(matrix[i])
    return matrix.tolist()

def translation(matrix1,matrix2):
    for i in range(0,len(matrix1)):
        matrix1[i]+=matrix2[i]
    return matrix1

def reflection_x(matrix):
    cal = np.array(((-1, 0), (0, 1)))
    matrix = np.array(matrix)
    matrix = matrix.dot(cal)
    return matrix

def reflection_y(matrix):
    cal = np.array(((1, 0), (0, -1)))
    matrix = np.array(matrix)
    matrix = matrix.dot(cal)
    return matrix

def scaling(matrix, x, y = 0):
    if y==0:
        y = x
    cal = np.array(((x, 0), (0, y)))
    matrix = np.array(matrix)
    matrix = matrix.dot(cal)
    return matrix
