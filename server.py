from flask import Flask, render_template
from subscriber import Subscriber

dht = Subscriber(port=10555)
dht.start()

seesaw1 = Subscriber(port=10655)
seesaw1.start()

print('Starting')

app = Flask(__name__,
        static_url_path='',
        static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/')
def data():
    data = {
            'seesaw1': seesaw1.get_values(),
            'dht': dht.get_values(),
        }
    return data
