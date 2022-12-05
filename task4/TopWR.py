import os
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))

def on_message(client, userdata, msg):
    print("Message received->" + msg.topic + " " + (msg.payload).decode('utf-8')) #отправка подписчику есть, но он не читает сообщение

def read_f(path_f = "./FF.txt"):
    os.system("mosquitto")
    file = open(path_f, 'r')
    str_f = file.readlines()
    for i in str_f:
        #print("mosquitto_pub -t file_topic -m " + i)
        os.system("mosquitto_pub -t \"file_topic\" -m \"" + i + '"')

client = mqtt.Client("reader")
client.on_connect = on_connect
client.connect('127.0.0.1', 1883)
client.subscribe("file_topic")
client.on_message = on_message
read_f()
client.loop_forever()