import pyautogui
import os


img_capture = pyautogui.locateOnScreen("chaos.jpg", confidence=0.7)
print(img_capture)

print(list(img_capture))
paths = list(img_capture)

pyautogui.moveTo(paths[0] + 45, paths[1] + 360)
pyautogui.sleep(1)
pyautogui.mouseDown()
pyautogui.sleep(0.5)
pyautogui.mouseUp()

