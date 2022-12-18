import paho.mqtt.client as mqtt
import math
import json
import csv
import time

class APP:
    #def __init__(self):

    def set_connection(self, name = "bot1"):
        self.client = mqtt.Client(name)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect('127.0.0.1')
        
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code {0}".format(str(rc)))

    def on_message(self, client, userdata, msg):
        print("Message received->" + msg.topic + " " + (msg.payload.decode("utf-8"))) #отправка подписчику есть, но он не читает сообщение
        m_data = (msg.payload.decode("utf-8"))
        self.process_msg(m_data)

    def pub(self, msg):
        self.client.publish(topic, msg)

    def start(self):
        self.client.loop_start()
        self.client.subscribe(topic)

    def end(self):
        self.client.loop_stop()

    def process_msg(self, data): #абстрактная функция
        pass

class RobotModel(APP):
    move_speed = 5.0
    turn_speed = 2.0
    x = 0.0
    y = 0.0
    angle = 0.0
    path = "./practice2/bot1_data.csv"

    #def __init__(self):

    def forward(self, time):
        RobotModel.x = RobotModel.x + RobotModel.move_speed * time * math.cos(RobotModel.angle)
        RobotModel.y = RobotModel.y + RobotModel.move_speed * time * math.sin(RobotModel.angle)

    def backward(self, time):
        RobotModel.x = RobotModel.x - RobotModel.move_speed * time * math.cos(RobotModel.angle)
        RobotModel.y = RobotModel.y - RobotModel.move_speed * time * math.sin(RobotModel.angle)

    def left(self, time):
        RobotModel.angle = (RobotModel.angle + RobotModel.turn_speed * time)
        if (RobotModel.angle > 2 * math.pi):
            RobotModel.angle = RobotModel.angle - 2 * math.pi

    def right(self, time):
        RobotModel.angle = RobotModel.angle - RobotModel.turn_speed * time
        if (RobotModel.angle < -2 * math.pi):
            RobotModel.angle = RobotModel.angle + 2 * math.pi

    def print_params(self, path):
        print("X: ", RobotModel.x, ', Y: ', RobotModel.y, ', Angle: ', RobotModel.angle)

        with open(path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([RobotModel.x, RobotModel.y, RobotModel.angle])

    def process_msg(self, data):
        s = json.loads(data)
        
        if (s["cmd"] == "stop"):
            bot1.end()
        if (s["cmd"] == "forward"):
            bot1.forward(float(s["val"]))
        if (s["cmd"] == "backward"):
            bot1.backward(float(s["val"]))
        if (s["cmd"] == "left"):
            bot1.left(float(s["val"]))
        if (s["cmd"] == "right"):
            bot1.right(float(s["val"]))
        
        self.print_params(RobotModel.path)

if (__name__ == "__main__"):
    topic = "abotcmd1"

    aapp = APP()
    bot1 = RobotModel()

    aapp.set_connection("aa")

    bot1.set_connection("bot1")
    bot1.start()

    time.sleep(1)
    string = '{"cmd":"left","val":"2.0"}'
    aapp.pub(string)

    string = '{"cmd":"forward","val":"5.0"}'
    aapp.pub(string)

    string = '{"cmd":"backward","val":"2.0"}'
    aapp.pub(string)