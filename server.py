from flask import Flask, render_template
import seesaw
import dht_listener

seesaw.start()
dht_listener.start()

app = Flask(__name__,
        static_url_path='',
        static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/')
def data():
    s1, s2 = seesaw.get_values()
    dht_data = dht_listener.get_dht_values()
    data = {
            'sensor2': s2,
            'dht': dht_data,
        }
    return data
