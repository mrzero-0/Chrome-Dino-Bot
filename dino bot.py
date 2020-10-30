'''
This is the Version 1 of the dino bot. in this bot we tried to take screen shot
of the screen and scan for pixels that is equal to the gray value 83,if we find
that pixel we hit key accordingly
'''
import pyautogui
from PIL import ImageGrab
import time

# helper Function gor handling key press


def hit(key):
    pyautogui.keyDown(key)
    time.sleep(0.05)
    pyautogui.keyUp(key)
    return

# helper function to scan for gray pixel in the two boxes ie cactie and bird


def isCollide(data):
    # scanning for gray pixel in Bird box
    for i in range(240, 350):
        for j in range(410, 558):
            if data[i, j] == 83:
                hit("down")
                return
    # scanning for gray pixel in cactie box
    for i in range(240, 400):
        for j in range(560, 662):
            if data[i, j] == 83:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Welcome to Dino bot v1 your game will start in 3 sec")
    time.sleep(2)
# main game loop
    while True:
        # takes the screenshot
        image = ImageGrab.grab().convert("L")
        data = image.load()
        # send the arrray to the scanning function
        isCollide(data)

        # for tuning of the box in the screen shot

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
