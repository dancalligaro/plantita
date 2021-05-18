""" SeeSaw Sampler 

This module samples the SeeSaw sensors periodically and averages the values 
over N samples (defined by NUMBER_OF_SAMPLES)

"""

import zmq
import json
import time
import board
from adafruit_seesaw.seesaw import Seesaw
from apscheduler.schedulers.background import BackgroundScheduler

interval = 2  # seconds

i2c_bus = board.I2C()

# ss0 = Seesaw(i2c_bus, addr=0x36)
sensor = Seesaw(i2c_bus, addr=0x37)

# ZMQ
port = 10655
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket_addr = "tcp://127.0.0.1:%s" % port
print("SeeSaw publishing on {}".format(socket_addr))
socket.bind(socket_addr)


def read_sensor():
    data = {
            'moisture': sensor.moisture_read(),
            'temp': sensor.get_temp(),
            'time': int(time.time() * 1000)
            }
    msg = json.dumps(data)
    print("This is the msg: {}".format(msg))
    socket.send_string(msg)


def start():
    while True:
        read_sensor()
        time.sleep(interval)

start()
