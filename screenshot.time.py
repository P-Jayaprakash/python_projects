'''
it will take a screenshot after 5 seconds
The disadvantage of this program is it overwrites the existing screenshot with the new one clicked
'''

import time
import pyautogui
def screenshot():
    time.sleep(5)
    img=pyautogui.screenshot('test.png')
    img.show()
screenshot()    
