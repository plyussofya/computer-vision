import cv2
import numpy as np 
import pyautogui as pag
import keyboard
import time
    
while True:   
    image = pag.screenshot() 
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    area = image[320:450, 90:900]

    # cv2.imshow("frame",  area)
    # cv2.imshow("object1", area[40:85, 140:200])
    # cv2.imshow("object2", area[17:45,75:135])    
    # cv2.waitKey(0)                
    
    object1 = area[40:85, 140:200].mean()
    object2 = area[40:70,140:230].mean()                     
        
    if object2 < 247.0: 
        keyboard.press("space")
        time.sleep(0.1)
        keyboard.release("space")        
                     
    if object1 < 247.0:
        keyboard.press("space")
        time.sleep(0.05)
        keyboard.release("space") 

#     key = cv2.waitKey(50)
#     if key == ord('q'):
#         break
# cv2.destroyAllWindows()