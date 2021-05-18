import zmq
import json
import threading

class Subscriber:

    def __init__(self, port):
        self.values = None
        self.port = port

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)

        self.socket.connect ("tcp://127.0.0.1:%s" % port)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, '')

    def get_values(self):
        return self.values

    def read(self):
        while True:
            msg = self.socket.recv_string()
            print("Port {} Received {}".format(self.port, msg))
            self.values = json.loads(msg)

    def start(self, daemon=True):
        # Start it non-blocking on a different thread
        t = threading.Thread(target=self.read, daemon=daemon)
        t.start()


if __name__ == '__main__':
    # For debug, start the script if run directly
    s = Subscriber(port=10655)
    s.start(daemon=False)
