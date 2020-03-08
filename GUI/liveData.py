import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random 

style.use('fivethirtyeight')

fig1 = plt.figure('x-move on time')
fig2 = plt.figure('y-move on time')
fig3 = plt.figure('z-move on time')
ax1 = fig1.add_subplot(1,1,1)
ax2 = fig2.add_subplot(1,1,1)
ax3 = fig3.add_subplot(1,1,1)

def produceNewData():
	graph_data = open('data.txt','a')
	x = str(random.randint(1,10))
	y = str(random.randint(1,1000))
	z = str(random.randint(1,3000))
	values = "\n" + x + "," + y + "," + z
	graph_data.write(values)

def animate(i):
	produceNewData()
	x_axis = []
	x = []
	y = []
	z = []	
	
	graph_data = open('data.txt','r').read()
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
	ax2.clear()
	ax3.clear()
 
	ax1.plot(x_axis,x, label = 'x-axis', color = 'g')
	ax2.plot(x_axis,y, label = 'y-axis', color = 'b')
	ax3.plot(x_axis,z, label = 'z-axis', color = 'r')

ani1 = animation.FuncAnimation(fig1, animate, interval=400)
ani2 = animation.FuncAnimation(fig2, animate, interval=400)
ani3 = animation.FuncAnimation(fig3, animate, interval=400)
plt.show()