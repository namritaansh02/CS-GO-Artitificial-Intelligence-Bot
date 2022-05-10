import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D  
from realtime_detect import process_image, Shoot

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

while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,1280,640)))
    
    new_screen, ObjectList = process_image(cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    process_objects(ObjectList)
    
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 