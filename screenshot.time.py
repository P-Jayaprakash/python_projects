'''
it will take a screenshot after 5 seconds
'''

import time
import pyautogui
def screenshot():
    time.sleep(5)
    img=pyautogui.screenshot('test.png')
    img.show()
screenshot()    
