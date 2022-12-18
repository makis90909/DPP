import pygame
import paho.mqtt.client as mqtt
import math
import json
import csv
import time
from threading import Thread

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
    move_speed = 20.0
    turn_speed = 5.0
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
            self.end()
        if (s["cmd"] == "forward"):
            self.forward(float(s["val"]))
        if (s["cmd"] == "backward"):
            self.backward(float(s["val"]))
        if (s["cmd"] == "left"):
            self.left(float(s["val"]))
        if (s["cmd"] == "right"):
            self.right(float(s["val"]))
        
        
        self.print_params(RobotModel.path)

def mqtt_cmd():
    aapp.set_connection("aa")

    bot1.set_connection("bot1")
    bot1.start()

    time.sleep(10)
    string = '{"cmd":"left","val":"2.0"}'
    aapp.pub(string)

    time.sleep(10)
    string = '{"cmd":"forward","val":"5.0"}'
    aapp.pub(string)

    time.sleep(10)
    string = '{"cmd":"backward","val":"2.0"}'
    aapp.pub(string)

def game():
    SX = 300
    SY = 300
    rect = pygame.Rect((SX, SY), (10, 10))
    image = pygame.Surface((10, 10))
    image.fill(WHITE)
    done = False
    while not done:
        clock.tick(FPS)
        rect.move_ip((SX + bot1.x) - rect.x, (SY + bot1.y) - rect.y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
        screen.fill(BLACK)
        screen.blit(image, rect)
        pygame.display.update()


topic = "abotcmd1"

aapp = APP()
bot1 = RobotModel()

#

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#

start_time = time.perf_counter()
t1 = Thread(target = mqtt_cmd)
t2 = Thread(target = game)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.perf_counter()
print(f'It took {end_time - start_time: 0.2f} second(s) to comlite.')
