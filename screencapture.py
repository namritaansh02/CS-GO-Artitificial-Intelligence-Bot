import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D  
#from realtime_detect import process_image, Shoot

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

def process_objects(ObjectList):
    if bool_shoot:
        for object in ObjectList:
            top, left, bottom, right, mid_v, mid_h, label, scores = object 
            if float(scores)>0.5:
                print(object)
                Shoot(mid_h, mid_v)

last_time = time.time()
bool_shoot = False
x_TL = 0 #(x,y) of top left
y_TL = 240
x_BR = 930 #(x,y) of bottom right
y_BR = 750
current_score = 0

while(True):
    screen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x_TL,y_TL,x_BR,y_BR))), cv2.COLOR_BGR2RGB)
    
    map = process_map(screen)

    # new_screen, ObjectList = process_image(screen)
    # process_objects(ObjectList)
    
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('map', map)
    #cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 