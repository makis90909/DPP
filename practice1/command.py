import sys
import os
import numpy as np
import math
import time

path = './practice1/way.txt'
d_speed = 5
d_angle = 1

def read_file(readpath):
    arr = []
    if not os.path.exists(readpath):
        print('file not found')
    else:
        arr = np.loadtxt(readpath, dtype = float)
    return arr

def calcul(arr):
    vec = [[0.0, 0.0]] * (len(arr)-1)
    for i in range(len(vec)):
        vec[i] = [arr[i + 1][0] - arr[i][0], arr[i + 1][1] - arr[i][1]]

    param = [0]*len(vec)
    for i in range(len(vec)):
        if (vec[i][0] != 0):
            if vec[i][0] >= 0:
                param[i] = [math.atan(vec[i][1]/vec[i][0]), (vec[i][0]**2 + vec[i][1]**2)**0.5]
            else:
                param[i] = [math.pi+math.atan(vec[i][1]/vec[i][0]), (vec[i][0]**2 + vec[i][1]**2)**0.5]
        else:
            if vec[i][1] >= 0:
                param[i] = [ math.pi/2, (vec[i][0]**2 + vec[i][1]**2)**0.5]
            else:
                param[i] = [-math.pi/2, (vec[i][0]**2 + vec[i][1]**2)**0.5]

    for i in range(1,len(param)):
        param[i][0] = (param[i][0] - param[i-1][0])
    return param

def send_cmd(cmd_params):
    for i in cmd_params:
        if i[0] < 0:
            string = f'{{"cmd": "left", "val": "{abs(i[0]/a_s)}"}}'
        else:
            string = f'{{"cmd": "right", "val": "{abs(i[0]/a_s)}"}}'
        print(string)
        print(f'C:/Progs/mosquitto/mosquitto_pub -t {topic} -m "' + string + '"')
        os.system(f'C:/Progs/mosquitto/mosquitto_pub -t {topic} -m "' + string + '"')
        time.sleep(abs(i[0]/a_s))

        string = f'{{"cmd": "forward", "val": "{i[1]/m_s}"}}'
        print(string)
        os.system(f'C:/Progs/mosquitto/mosquitto_pub -t {topic} -m "' + string + '"')
        time.sleep(abs(i[1]/m_s))
    string = f'{{"cmd": "stop"}}'
    print(string)
    os.system(f'C:/Progs/mosquitto/mosquitto_pub -t {topic} -m "' + string + '"')

if __name__ == "__main__":
    args = sys.argv
    ip = args[1]
    port = args[2]
    topic = args[3]
    a_s = float(args[4])
    m_s = float(args[5])

    ##os.system(f"C:/Progs/mosquitto/mosquitto -v -d -p {port}")
    #time.sleep(5)

    arr = read_file(path)
    params = calcul(arr)
    send_cmd(params)