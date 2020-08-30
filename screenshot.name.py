#In this program a new name is generated for each screenshot according to the time. So there will be no chance for the overwritten of previous clicked screenshots.
import time
import pyautogui
def screenshot():
    name=int(round(time.time()*100))
    name='{}.png'.format(name)
    time.sleep(5)
    img=pyautogui.screenshot(name)
    img.show()
     
screenshot()              
