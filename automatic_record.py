import pyautogui
import time
from PIL import ImageGrab

def recording_loop():
    time.sleep(sleeplong)#close excel tab, open axie replay
    pyautogui.hotkey('ctrl', 'w')
    print('ctrl w')
    time.sleep(sleepnormal)
    pyautogui.press('left')
    print('left')
    time.sleep(sleepshort)
    pyautogui.press('enter')
    print('enter')
    x, y = 460, 460
    loss_color = (148, 141, 120)
    victory_color = (248, 198, 58)
    while True:
        print('scanning (once per 2 seconds)')
        screenshot = ImageGrab.grab()
        pixel_color = screenshot.getpixel((x, y))
        if pixel_color == loss_color:
            print("Loss detected.")
            break
        elif pixel_color == victory_color:
            print("Victory detected.")
            break
        time.sleep(sleeplong)
    time.sleep(sleepnormal)
    pyautogui.click(460, 460)
    time.sleep(sleeplong)
    pyautogui.press('esc')
    time.sleep(sleepshort)
    pyautogui.press('esc')
    time.sleep(sleepshort)
    pyautogui.press('enter')

sleepnormal = 1
sleepshort = 0.5
sleeplong = 3


i = 0
while i < 16:
    time.sleep(sleepnormal)
    pyautogui.hotkey('alt', 'f9') #start recording, make sure tabs are already open, chrome window is selected

    for loop in range(4):
        print('currently in loop: ' + str(loop+1))
        recording_loop()

    time.sleep(sleepnormal)
    pyautogui.hotkey('alt', 'f9') #stop recording
    time.sleep(sleeplong)
    i = i + 1
