#!/usr/bin/python3

from map_funcs import *
import os
import json
from threading import Thread

from dotenv import dotenv_values

from kafka import KafkaConsumer as kc
from kafka import TopicPartition
from kafka.admin import KafkaAdminClient

from kafka import KafkaProducer as kp
from login import *
import time

import signal

def signalExit(signum, frame):
    print("\n\nEXIT")
    exit(1)
signal.signal(signal.SIGINT, signalExit)

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

config = dotenv_values(".env")

KAFKA_IP = config['KAFKA_IP']
KAFKA_PORT = config['KAFKA_PORT']
BROKER = KAFKA_IP + ":" + KAFKA_PORT
GRPC_WTS_IP = config['GRPC_WTS_IP']
GRPC_WTS_PORT = config['GRPC_WTS_PORT']

LOGED = []
AFORO_MAX=int(config['AFORO_MAX'])
AFORO=0

def exit_delete_topics(mapa, id_vis, name):
    updatePosition(mapa, id_vis, -1 , -1)
    LOGED.remove(name)
    global AFORO
    AFORO -= 1
    print("[CLOSING CONNECTION] Visitor \"" + name + "\" disconnected.")
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=BROKER)
        admin_client.delete_topics(topics=[name + 'Topic', name + 'TopicRecv'])
    except:
        exit(1)
    exit(1)


def handleVisitor(name, id_vis):
    consumer = kc(name + 'Topic', bootstrap_servers = BROKER, consumer_timeout_ms=3000)
    producer = kp(bootstrap_servers = BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')
    print("[ESTABLISHED CONNECTION] Visitor \"" + name + "\" connected.")
    mapa = getMap()

    try:
        while True:
            msg = json.loads(next(consumer).value.decode('utf-8'))
            mapa, attrs = getMap()
            mapa, newPos = updatePosition(mapa, id_vis, msg['pos'], msg['next_pos'])
            time.sleep(0.2)

            producer.send(name+"TopicRecv", {'ok': True, 'mapa' : mapa , 'attrs' : attrs, 'new_pos': newPos})

            if not msg['ok']:
                break
    except:
        print('Connection lost with visitor "'+name+'"')
    finally:
        exit_delete_topics(mapa, id_vis, name)
            


def main():
    global AFORO_MAX
    global AFORO
    global LOGED
   
    login_consumer = kc("loginTopic", bootstrap_servers = BROKER)
    producer = kp(bootstrap_servers = BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'),acks='all')

    while True:
        print("[LOGIN] Awaiting for info on Kafka Server")
        msg = json.loads(next(login_consumer).value.decode('utf-8'))
        time.sleep(0.1)

        aforoOk = AFORO_MAX > AFORO
        loginOk, id_vis = login(msg['name'], msg['password'])
        loginOk = loginOk and not msg['name'] in LOGED
        if loginOk and aforoOk:
            AFORO += 1
            LOGED.append(msg['name'])
            
            mapa, _ = getMap()
            firstPos = getRandomEmpty(mapa)
            producer.send("loginResponsesTopic", {'ok': True, 'firstPos' : firstPos, 'id_vis': id_vis, 'msg' : 'Login ok'})
            time.sleep(0.2)

            new_thread = Thread(target=handleVisitor, args=(msg['name'], id_vis))
            new_thread.start()

        else:
            producer.send("loginResponsesTopic", {'ok': False, 'msg' : 'ERROR login' if aforoOk else 'Aforo completo'})

main()
