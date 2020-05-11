import pyautogui
import time

while True:
	time.sleep(5)
	img = pyautogui.screenshot('my_screenshot.png')
	img.show()
	break