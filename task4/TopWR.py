import os
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))

def on_message(client, userdata, msg):
    #print("Message received->" + msg.topic + " " + (msg.payload.decode("utf-8"))) #отправка подписчику есть, но он не читает сообщение
    m_data.append(int((msg.payload.decode("utf-8"))))
    
    l = len(m_data)
    if (l >= 3):
        print("Скользящее среднее: ", m_data[l-1]*0.6 + m_data[l-2]*0.3 + m_data[l-3]*0.1)

def read_f(path_f = "./FF.txt"):
    os.system("mosquitto")
    file = open(path_f, 'r')
    str_f = file.readlines()
    for i in str_f:
        #print("mosquitto_pub -t file_topic -m " + i)
        os.system("mosquitto_pub -t \"file_topic\" -m \"" + i + '"')

m_data = []
client = mqtt.Client("reader")
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1')
client.loop_start()
client.subscribe("file_topic")
read_f()
time.sleep(5)
client.loop_stop()
print(m_data)