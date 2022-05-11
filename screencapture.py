import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, ReleaseKey, W, A, S, D  
from realtime_detect import process_image

def process_map(original_image):
    lower = np.array([0,0,0])
    upper = np.array([255,10,255])

    map = original_image[30:180, 0:150]
    # map = cv2.cvtColor(map, cv2.COLOR_RGB2HSV)
    # map = cv2.inRange(map, lower, upper)
    return map

def debug_keypress(request):    
    while(request):
        print('down')
        PressKey(W)
        time.sleep(3)
        print('up')
        ReleaseKey(W)

def process_objects(r_image, ObjectsList):
    for i in range(len(ObjectsList)):
        offset = 35
        pyautogui.moveTo(ObjectsList[i][4], ObjectsList[i][5]+offset)
        image_x = r_image.shape[1] / 2
        image_y = (r_image.shape[0] / 2) + offset

        target_interval = 20
        cv2.circle(r_image,(int(image_x),int(image_y)), 4, (255,0,255), -1)
        if ObjectsList[i][4] < image_x+target_interval and ObjectsList[i][4] > image_x-target_interval and \
            ObjectsList[i][5]+offset < image_y+target_interval and ObjectsList[i][5]+offset > image_y-target_interval:
                pyautogui.click()
        return 

last_time = time.time()
bool_shoot = True
x_TL = 0 #(x,y) of top left
y_TL = 40
x_BR = 1280 #(x,y) of bottom right
y_BR = 600
current_score = 0

while(True):
    screen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x_TL,y_TL,x_BR,y_BR))), cv2.COLOR_BGR2RGB)
    
    #map = process_map(screen)

    new_screen, ObjectList = process_image(screen)
    process_objects(new_screen, ObjectList)
    
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    #cv2.imshow('map', map)
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 