import zmq
import json
import asyncio

# Port used by the DHT sensor
dht_port = 10555
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://localhost:%s" % dht_port)
socket.setsockopt_string(zmq.SUBSCRIBE, '')


async def read_dht():
    print('waiting for message')
    while True:
        msg = socket.recv_string()
        print("Received string: %s ..." % msg)

print('here')
asyncio.run(read_dht())

