import os

def read_f(path_f = "./FF.txt"):
    os.system("mosquitto -v")
    file = open(path_f, 'r')
    str_f = file.readlines()
    for i in str_f:
        #print("mosquitto_pub -t file_topic -m " + i)
        os.system("mosquitto_pub -t file_topic -m " + i)

def sub_topic():
    os.system("mosquitto_sub -t file_topic")

read_f()