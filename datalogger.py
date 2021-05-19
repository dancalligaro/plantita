from dotenv import load_dotenv

import os
import time
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from subscriber import Subscriber

load_dotenv()

interval = 2
dht = Subscriber(port=10555)
dht.start()

# Influx Stuff
token = os.environ['INFLUX_TOKEN']
org = os.environ['INFLUX_ORG']
bucket = os.environ['INFLUX_BUCKET']
influx_url = os.environ['INFLUX_URL']

client = InfluxDBClient(url=influx_url, token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

def write(data):
    msg = ''.join([
        'dht ',
        ",".join(["{}={}".format(k,v) for k,v in data.items() if k !='time']),
        ' ',
        str(data['time']),
        '000000' #nanoseconds
        ])
    print('Writing msg {}'.format(msg))
    write_api.write(bucket, org, msg)


def start():
    last_timestamp = 0
    while True:
        data = dht.get_values()
        if data and last_timestamp != data['time']:
            write(data)
            last_timestamp = data['time']
        time.sleep(interval)

start()

