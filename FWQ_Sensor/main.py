#!/usr/bin/python3

import os
import json
import random
import time
import signal

from kafka import KafkaProducer as kp

from dotenv import dotenv_values


def signalExit(signum, frame):
    os.system('rm -rf active_sensors/' + str(sensor_id))
    exit(1)

signal.signal(signal.SIGINT, signalExit)

config = dotenv_values('.env')
ENGINE_KAFKA_IP = config['ENGINE_KAFKA_IP']
ENGINE_KAFKA_PORT = config['ENGINE_KAFKA_PORT']
BROKER = ENGINE_KAFKA_IP +':'+ ENGINE_KAFKA_PORT


attrs = os.listdir('fisic_attractions')
attrs = [a[0:-5] for a in attrs]
attrs = [a[4:] for a in attrs]

sensor_id = -1
active_sensors = os.listdir('active_sensors')
if len(active_sensors) == 0:
    sensor_id = 1
else:
    for i in range(len(active_sensors)):
        if int(active_sensors[i]) != attrs[i]:
            sensor_id = attrs[i]

if sensor_id != -1:
    os.system('touch active_sensors/' + str(sensor_id))
else:
    print('Todas las atracciones tienen un sensor activo')
    exit()

timePassed = 0

while True:

    try:
        with open('../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json', 'r') as a:
            attr_queue = json.load(a)
        names = list(attr_queue.keys())

        prod = kp(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
        prod.send('SensorsTopic', {'attr': sensor_id, 'people_count' : len(names)})

        if len(names) > 0:
            attr_queue[names[0]] -= timePassed

        os.system('rm -rf ../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json')

        with open('../FWQ_Sensor/fisic_attractions/attr'+str(sensor_id)+'.json', 'w') as a:
            json.dump(attr_queue, a)

        timePassed = random.randrange(1,4)
        time.sleep(timePassed)

    except:
        pass