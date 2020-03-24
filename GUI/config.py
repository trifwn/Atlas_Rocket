import os
import time
from collections import deque

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_PATH, "data")

def init():
	'''
	Defining globals and initializing them
	'''
	max_length = 100
	global times, temperature, pressure, humidity, altitude, or_x, or_y, or_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z
	
	times = deque(maxlen=max_length)
	temperature = deque(maxlen=max_length)
	pressure = deque(maxlen=max_length)
	humidity = deque(maxlen=max_length)
	altitude = deque(maxlen=max_length)

	#orientation
	or_x = deque(maxlen=max_length)
	or_y = deque(maxlen=max_length)
	or_z = deque(maxlen=max_length)

	#velocity
	vel_x = deque(maxlen=max_length)
	vel_y = deque(maxlen=max_length)
	vel_z = deque(maxlen=max_length)
	
	#acceleration
	acc_x = deque(maxlen=max_length)
	acc_y = deque(maxlen=max_length)
	acc_z = deque(maxlen=max_length)

	global data_dict
	data_dict = {
		'Temperature': temperature,
		'Pressure': pressure,
		'Humidity': humidity,
		'Altitude': altitude,
		'3D Cone plot': (vel_x, vel_y, vel_z, or_x, or_y, or_z),
		'x-y-z-move': (or_x, or_y, or_z),
		'Velocity for x-y-z': (vel_x, vel_y, vel_z),
		'Acceleration for x-y-z': (acc_x, acc_y, acc_z)
	}