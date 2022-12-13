import cv2
import numpy as np
import random

cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cam.set(cv2.CAP_PROP_EXPOSURE, -3)
cam.set(cv2.CAP_PROP_AUTO_WB, 0)

#98-101 206-255 125-255 blue
#64-70 0-226 120-255 green
#155-176 0-255 120-255 red

lower_b = np.array([95, 180, 100])
upper_b = np.array([125, 255, 255])
lower_g = np.array([60, 0, 100])
upper_g = np.array([85, 255, 255])
lower_r = np.array([140, 160, 100])
upper_r = np.array([185, 255, 255])

lst = {0: "blue", 1: "red", 2: "green"}
index = list(lst.keys())
random.shuffle(index)
print("indexes:", index)

while cam.isOpened():
    position = []
    _, frame = cam.read()
    #frame = cv2.GaussianBlur(frame, (25, 25), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_b, upper_b)
    mask2 = cv2.inRange(hsv, lower_r, upper_r)
    mask3 = cv2.inRange(hsv, lower_g, upper_g)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours3, _ = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        position.append(x)
        if radius > 20:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.putText(frame, f"Color = blue", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0))
    if len(contours2) > 0:
        c = max(contours2, key=cv2.contourArea)
        (x2, y2), radius = cv2.minEnclosingCircle(c)
        position.append(x2)
        if radius > 20:
            cv2.circle(frame, (int(x2), int(y2)), int(radius), (0, 255, 255), 2)
            cv2.putText(frame, f"Color = red", (10, 60), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0))
    if len(contours3) > 0:
        c = max(contours3, key=cv2.contourArea)
        (x3, y3), radius = cv2.minEnclosingCircle(c)
        position.append(x3)
        if radius > 20:
            cv2.circle(frame, (int(x3), int(y3)), int(radius), (0, 255, 255), 2)
            cv2.putText(frame, f"Color = green", (10, 90), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0)) 
    cv2.putText(frame, f"Порядок - {lst.get(index[0])}, {lst.get(index[1])}, {lst.get(index[2])}, ", (10, 120), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255))

    if len(position) == 3:
        if position[index[0]] < position[index[1]] < position[index[2]]:
            cv2.putText(frame, f"УГАДАЛИ!!!!", (10, 150), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0))
        else:
            cv2.putText(frame, f"Попробуй еще!", (10, 150), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255))

    cv2.imshow("Image", frame)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
cv2.destroyAllWindows()