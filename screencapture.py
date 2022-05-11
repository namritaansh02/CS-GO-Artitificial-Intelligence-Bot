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
    #Values I was testing to filter out walkable area

    map = original_image[30:180, 0:150]
    return map

def process_objects(r_image, ObjectsList):
    if np.shape(ObjectList)[0]==0:
        return
    pos_x, pos_y = pyautogui.position()
    closest_object = 0
    offset = 35
    curr_dist = (ObjectList[0][4]-pos_x)**2 + (ObjectList[0][5]+offset-pos_y)**2
    for i in range(len(ObjectsList)):
        dist = (ObjectList[i][4]-pos_x)**2 + (ObjectList[i][5]+offset-pos_y)**2
        if dist<curr_dist:
            closest_object = i
            curr_dist = dist 
    
    pyautogui.moveTo(ObjectsList[closest_object][4], ObjectsList[closest_object][5]+offset)
    image_x = r_image.shape[1] / 2
    image_y = (r_image.shape[0] / 2) + offset
    target_interval = 20
    cv2.circle(r_image,(int(image_x),int(image_y)), 4, (255,0,255), -1)
    if ObjectsList[closest_object][4] < image_x+target_interval and ObjectsList[closest_object][4] > image_x-target_interval and \
        ObjectsList[closest_object][5]+offset < image_y+target_interval and ObjectsList[closest_object][5]+offset > image_y-target_interval:
            pyautogui.click()

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