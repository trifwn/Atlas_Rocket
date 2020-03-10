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
	global times, temperature, pressure, humidity, altitude, orientation, velocity, acceleration
	
	times = deque(maxlen=max_length)
	temperature = deque(maxlen=max_length)
	pressure = deque(maxlen=max_length)
	humidity = deque(maxlen=max_length)
	altitude = deque(maxlen=max_length)
	orientation = deque(maxlen=max_length) # Contains tuples of (or_x, or_y, or_z)
	velocity = deque(maxlen=max_length)	# Contains tuples of (vel_x, vel_y, vel_z)
	acceleration = deque(maxlen=max_length) # Contains tuples of (acc_x, acc_y, acc_z)

	global data_dict
	data_dict = {
		'Temperature': temperature,
		'Pressure': pressure,
		'Humidity': humidity,
		'Altitude': altitude,
		'x-y-z-move': orientation,
		'Velocity for x-y-z': velocity,
		'Acceleration for x-y-z': acceleration
	}