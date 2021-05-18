from flask import Flask, render_template
import seesaw

seesaw.start()

app = Flask(__name__,
        static_url_path='',
        static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/')
def data():
    s1, s2 = seesaw.get_values()
    data = {
            'sensor2': {
                'temp': s2['temp'],
                'moisture': s2['moisture'],
            },
        }
    return data
