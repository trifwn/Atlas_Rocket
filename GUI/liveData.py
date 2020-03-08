import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import csv

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
	x_axis = []
	x = []
	y = []
	z = []	
	
	graph_data = open('file.txt','r').read()
	lines = graph_data.split('\n')
	total_elements = 1
	for line in lines:
		if len(line) > 1:
			# Expected file: x,y,z coordinates
			elements = []
			elements = line.split(',')
			x.append(float(elements[0]))
			y.append(float(elements[1]))
			z.append(float(elements[2]))
			x_axis.append(total_elements)
			total_elements += 1
			
	ax1.clear()
	ax1.plot(x_axis,x, label = 'x-axis', color = 'g')
	ax1.plot(x_axis,y, label = 'y-axis', color = 'b')
	ax1.plot(x_axis,z, label = 'z-axis', color = 'r')
	plt.xlabel('time')
	plt.ylabel('distance')

	plt.title('x-y-z Graph')

ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()
