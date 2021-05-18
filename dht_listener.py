import zmq
import json
import threading


# Port used by the DHT sensor
dht_port = 10555
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://127.0.0.1:%s" % dht_port)
socket.setsockopt_string(zmq.SUBSCRIBE, '')

dht_values = None

def get_dht_values():
    return dht_values

def read_dht():
    global dht_values
    while True:
        msg = socket.recv_string()
        print("Received string: %s ..." % msg)
        dht_values = json.loads(msg)

def start(daemon=True):
    # Start it non-blocking on a different thread
    t = threading.Thread(target=read_dht,daemon=daemon)
    t.start()

if __name__ == '__main__':
    # For debug, start the script if run directly
    start(daemon=False)
