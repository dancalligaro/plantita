""" SeeSaw Sampler 

This module samples the SeeSaw sensors periodically and averages the values 
over N samples (defined by NUMBER_OF_SAMPLES)

"""

import time
import board
from adafruit_seesaw.seesaw import Seesaw
from collections import deque
from apscheduler.schedulers.background import BackgroundScheduler

i2c_bus = board.I2C()

# ss0 = Seesaw(i2c_bus, addr=0x36)
ss1 = Seesaw(i2c_bus, addr=0x37)

NUMBER_OF_SAMPLES = 1

# One queue of samples for each one of the sensors
samples1 = deque(maxlen=NUMBER_OF_SAMPLES)
samples2 = deque(maxlen=NUMBER_OF_SAMPLES)

# Holds the averages, updated every read
avg1 = None
avg2 = None

# Make sure start is only called once
started = False

def read_sensor(s):
    moisture = s.moisture_read()
    temp = s.get_temp()
    rval= {'moisture': moisture, 'temp': temp}
    return rval

def calculate_averages(samples):
    moisture_avg = sum(s['moisture'] for s in samples) / len(samples)
    temp_avg = sum(s['temp'] for s in samples) / len(samples)
    return {'moisture': moisture_avg, 'temp': temp_avg }

def update_samples():
    global avg1
    global avg2
    #samples1.append(read_sensor(ss0))
    samples2.append(read_sensor(ss1))
    #avg1 = calculate_averages(samples1)
    avg2 = calculate_averages(samples2)

def get_values():
    return [avg1, avg2]

def scheduled_function():
    update_samples()

def start():
    global started
    if started:
        print("Already started. Skipping.")
        return

    started = True
    print('scheduler start')
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_function, 'interval', seconds=2)
    scheduler.start()

