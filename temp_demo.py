""" Temperature + humidity publisher

This will publish the current temp + humidity periodically

"""
# sudo apt-get install libgpiod2
# pip3 install adafruit-circuitpython-dht

import time
import board
import adafruit_dht
import zmq
import json

# Sensor
dhtDevice = adafruit_dht.DHT22(board.D17)
interval = 5.0 # Seconds

# ZMQ
port = 10555
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket_addr = "tcp://127.0.0.1:%s" % port
print("DHT publishing on {}".format(socket_addr))
socket.bind(socket_addr)

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C Humidity: {}% ".format( temperature_c, humidity))   
        data = {
                "temp": temperature_c,
                "humidity": humidity,
                "time": int(time.time() * 1000),
        }
        msg = json.dumps(data)
        print("This is the msg: {}".format(msg))
        socket.send_string(msg)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print("Runtime Error")
        print(error.args[0])
        time.sleep(interval)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(interval)

