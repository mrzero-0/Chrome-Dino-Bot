'''
This is the Version 2 of the dino bot. in this bot we tried to take screenshot
of the area that is of interest. then we take an arbitrary pixel of background
and scan for that pixel in the bounding boxes of bird and cactie if the pixel is
not equal to bgpixel then its an obstical, now we jump only when the two level of
birds are there because the hightest bird can be passed without doing anything
'''
import pyautogui as gui
import keyboard
import time
import math

# Function to get pixel value


def getPixel(img, x, y):
    pxl = img.load()
    return pxl[x, y]


# Area of interest in the screen as rectangle can be formed using two coordinates
# of diagonal
x1, y1, x2, y2 = 0, 293, 1920, 465

# main bot loop
while True:
    # Get a screen shot
    sct_img = gui.screenshot(region=(x1, y1, x2, y2)).convert("L")
    # sct_img.show()
    # Get the color of the world background
    bgColor = getPixel(sct_img, 440, 30)
    print(bgColor)
    break
