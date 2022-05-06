import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D  
from realtime_detect import process_image

# for i in list(range(4))[::-1]:
#     print(i+1)
#     time.sleep(1)

def debug_keypress(request):    
    while(request):
        print('down')
        PressKey(W)
        time.sleep(3)
        print('up')
        ReleaseKey(W)

last_time = time.time()

while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,1280,640)))
    new_screen = process_image(cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 