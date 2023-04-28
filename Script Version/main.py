import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

# Make sure to put all mathematical equations in numpy format

def f(xVal):
    return np.cos(xVal)

graphtype = '3d'
dataType = 'function'
# Go to this link for details on all 2D line type tags
# https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D   
lineType = 'red'

x3D = [4];
y3D = [3];
z3D = [3];

xLabel = 'Test'
yLabel = 'Test'
zLabel = 'Test'

x2DPoints = [2, 3, 4, 5]
y2DPoints = [1, 2, 3, 4]

# Minimum x value in function
x2DfuncStart = 0
# Maximum x value in function
x2DfuncStop = 10
# Number of samples to generate default is 50 more samples means greater detail
x2DfuncSamples = 200

x2Dfunc = np.linspace(x2DfuncStart, x2DfuncStop, x2DfuncSamples)

# Four functions for multifunction graphing
def y1(xVal):
    return np.cos(0.5*xVal)
def y2(xVal):
    return np.cos(xVal)
def y3(xVal):
    return np.cos(1.5*xVal)
def y4(xVal):
    return np.cos(2*xVal)

# Minimum Z value in 3d function
z3DfuncStart = 0
# Maximum Z value in 3d function
z3DfuncStop = 10
# Number of samples to generate default is 50 more samples means greater detail
z3DfuncSamples = 200

z3Dfunc = np.linspace(z3DfuncStart, z3DfuncStop, z3DfuncSamples)

# Functions for 3D graphing
def xFunc(zVal):
    return np.cos(0.5*zVal)

def yFunc(zVal):
    return np.sin(zVal)

with open("Script Version\graphScript.py") as graphScript:
    exec(graphScript.read())