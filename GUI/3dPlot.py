from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

ax = plt.axes(projection='3d')

graph_data = open('data.txt','r').read()
lines = graph_data.split('\n')

or_x,or_y,or_z = [],[],[]
for line in lines:
    if len(line) > 1:
        # Expected file: x,y,z coordinates , humidity, x,y,z acceleration
        elements = []
        elements = line.split(',')
        # Orientation
        or_x.append(float(elements[0]))
        or_y.append(float(elements[1]))
        or_z.append(float(elements[2]))

ax.plot3D(or_x, or_y, or_z, 'red')

plt.show()