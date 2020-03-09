import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random 

style.use('fivethirtyeight')

# Figures
fig1 = plt.figure('x-y-z-move')
fig2 = plt.figure('Humidity')
fig3 = plt.figure('Acceleration for x-y-z')
ax1 = fig1.add_subplot(1,1,1)
ax2 = fig2.add_subplot(1,1,1)
ax3 = fig3.add_subplot(1,1,1)

def produceNewData():
	graph_data = open('data.txt','a')
	orx = str(random.randint(1,10))
	ory = str(random.randint(1,1000))
	orz = str(random.randint(1,3000))
	hum = str(random.randint(10000,15000))
	accx = str(random.randint(0,1000))
	accy = str(random.randint(0,10000))
	accz = str(random.randint(0,30000))

	values = "\n" + orx + "," + ory + "," + orz + "," + hum + "," + accx + "," + accy + "," + accz
	
	graph_data.write(values)

def animate(i):
	for _ in range(1):
		produceNewData()
	time = []
	or_x,or_y,or_z = [],[],[]
	humidity = []
	acc_x,acc_y,acc_z = [],[],[]
	
	graph_data = open('data.txt','r').read()
	lines = graph_data.split('\n')
	total_elements = 1
	for line in lines:
		if len(line) > 1:
			# Expected file: x,y,z coordinates , humidity, x,y,z acceleration
			elements = []
			elements = line.split(',')
			# Orientation
			or_x.append(float(elements[0]))
			or_y.append(float(elements[1]))
			or_z.append(float(elements[2]))
			
			# Humidity
			humidity.append(float(elements[3]))

			# Acceleration
			acc_x.append(float(elements[4]))
			acc_y.append(float(elements[5]))
			acc_z.append(float(elements[6]))

			# Time
			time.append(total_elements)
			total_elements += 0.01
			
	ax1.clear() 
	ax2.clear()
	ax3.clear()
 
	ax1.plot(time,or_x, label = 'x-axis', color = 'g')
	ax1.plot(time,or_y, label = 'y-axis', color = 'b')
	ax1.plot(time,or_z, label = 'z-axis', color = 'r')
	ax1.set_xlabel('time')
	ax1.set_ylabel('x-y-z orientation')

	ax2.plot(time,humidity,color = 'k')
	ax2.set_xlabel('time')
	ax2.set_ylabel('humidity')

	ax3.plot(time,acc_x, label = 'x-axis', color = 'y')
	ax3.plot(time,acc_y, label = 'y-axis', color = 'c')
	ax3.plot(time,acc_z, label = 'z-axis', color = 'm')
	ax3.set_xlabel('time')
	ax3.set_ylabel('x-y-z acceleration')

	
ani1 = animation.FuncAnimation(fig1, animate, interval=250) # x,y,z
ani2 = animation.FuncAnimation(fig2, animate, interval=250) # humidity
ani3 = animation.FuncAnimation(fig3, animate, interval=250) # acc x,y,z
plt.show()