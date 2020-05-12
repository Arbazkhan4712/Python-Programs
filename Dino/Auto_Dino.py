from PIL import Image, ImageGrab #pip install pillow
import pyautogui #pip install pyautogui
from time import sleep
from numpy import asarray #pip install numpy


def crash(data):
    for i in range(300,415):
        for j in range(210,370):
            if data[i, j] < 100:
                # pyautogui.keyDown('down')
                return True

    for i in range(300,415):
        for j in range(400,450):
            if data[i, j] < 100:
                pyautogui.keyDown('up')
                return True
    return False


if __name__ == "__main__":
    sleep(2)
    pyautogui.keyDown('up')
    while True:
        img = ImageGrab.grab().convert('L')
        data = img.load()
        crash(data)
