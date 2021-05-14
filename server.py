from flask import Flask
import seesaw

seesaw.start()

app = Flask(__name__)

@app.route("/")
def base_path():
    s1, s2 = seesaw.get_values()
    msg_lines = [
        "Sensor 1:",
        "=> Temp: {}".format(s1['temp']),
        "=> Moist: {}".format(s1['moisture']),
        "",
        "Sensor 2:",
        "=> Temp: {}".format(s2['temp']),
        "=> Moist: {}".format(s2['moisture']),
    ]
    return "<br>".join(msg_lines)
