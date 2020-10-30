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


# time variables for accounting acceleration of the Dino
last = 0
total_time = 0

# Area of interest in the screen as rectangle can be formed using two coordinates
# of diagonal
x1, y1, x2, y2 = 0, 293, 1920, 465

# the intervals where the bot will search for obstacles
y_cactie, x_start, x_end = 350, 435, 450
y_bird = 275  # for the birds
# main bot loop
while True:
    # initial time
    t1 = time.time()
    # increase the search width every second to simulate the dino acceleration
    if math.floor(total_time) != last:
        if x_end < x2:
            x_end += 4
        else:
            x_end = x2
        last = math.floor(total_time)

    # Get a screen shot of Area of interest
    AoI = gui.screenshot(region=(x1, y1, x2, y2)).convert("L")
    # AoI.show()
    # Get the color of the world background
    bgColor = getPixel(AoI, 440, 30)
    # print(bgColor)

    for x in reversed(range(x_start, x_end)):
        # if i found a pixel in the search interval with a colour other than the bg colour,
        # then it is an obstacle
        if getPixel(AoI, x, y_cactie) != bgColor or getPixel(AoI, x, y_bird) != bgColor:
            keyboard.press(' ')  # jump
            break
    # final time
    t2 = time.time()-t1
    total_time += t2
    print(total_time)
