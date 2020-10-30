import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)
    time.sleep(0.05)
    pyautogui.keyUp(key)
    return


def isCollide(data):
    for i in range(240, 350):
        for j in range(410, 558):
            if data[i, j] == 83:
                hit("down")
                return
    for i in range(240, 400):
        for j in range(560, 662):
            if data[i, j] == 83:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Welcome to Dino bot v1 your game will start in 3 sec")
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        isCollide(data)

        # for i in range(240, 325):
        #     for j in range(560, 662):
        #         data[i, j] = 86
        #
        # for i in range(240, 390):
        #     for j in range(410, 558):
        #         data[i, j] = 171
        #
        # image.show()
        # break
