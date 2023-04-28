import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from main import *

ax = plt

if graphtype == '2d' and dataType == 'point':
    ax.scatter(x2DPoints, y2DPoints, lineType)
    ax.ylabel(yLabel)
    ax.show()
elif graphtype == '2d' and dataType == 'line':
    ax.plot(x2DPoints, y2DPoints, lineType)
    ax.ylabel(yLabel)
    ax.xlabel(xLabel)
    ax.show()
elif graphtype =='2d' and dataType == 'function':
    ax.plot(x2Dfunc, f(x2Dfunc))
    ax.xlabel(xLabel)
    ax.ylabel(yLabel)
    ax.show()
elif graphtype == '2d' and dataType == 'multiFunction':
    # To use less than four functions simply comment out the unused functions
    ax.plot(x2Dfunc, y1(x2Dfunc))
    ax.plot(x2Dfunc, y2(x2Dfunc))
    ax.plot(x2Dfunc, y3(x2Dfunc))
    ax.plot(x2Dfunc, y4(x2Dfunc))
    ax.show()
elif graphtype == '3d' and dataType == 'point':
    ax = ax.figure().add_subplot(projection=graphtype)
    ax.scatter(x3D, y3D, z3D)
    ax.view_init(elev=20., azim=-35, roll=0)
elif graphtype == '3d' and dataType == 'function':
    ax = ax.figure().add_subplot(projection=graphtype)
    ax.plot(xFunc(z3Dfunc), yFunc(z3Dfunc), z3Dfunc)
    ax.view_init(elev=26., azim=-35, roll=0)