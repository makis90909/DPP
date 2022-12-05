import cv2
import os
import sys

#os.system("C:/Progs/mosquitto/mosquitto -v")

def rec_click(event, x, y, flags, param):
    global recs
    if event == cv2.EVENT_LBUTTONDOWN:
        os.system("C:/Progs/mosquitto/mosquitto_pub -t clickXY -m \"({}, {})\"".format(x, y))
        recs.append((x-25, y-25))

recs = []
args = sys.argv
if len(args) == 1:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(args[1])

while(True):
    ret, frame = cap.read()
    cv2.namedWindow(winname='frame_fulcolor')
    cv2.setMouseCallback('frame_fulcolor', rec_click)
    
    for i in recs:
        cv2.rectangle(frame, i, (i[0]+50, i[1]+50), (0, 0, 255), 3)

    cv2.imshow('frame_fulcolor', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
        recs = []
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()