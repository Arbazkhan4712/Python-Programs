from PIL import Image, ImageGrab
import pyautogui
from time import sleep
from numpy import asarray

# def draw():



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

# def bird(data):
#     for i in range(300,415):
#         for j in range(400,450):
#             if data[i, j] < 100:
#     return False
#                 return True


if __name__ == "__main__":
    sleep(2)
    pyautogui.keyDown('up')
    while True:
        img = ImageGrab.grab().convert('L')
        data = img.load()
        crash(data)