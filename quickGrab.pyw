import PIL.ImageGrab as ImageGrab
import os
import time
"""
 
All coordinates assume a screen resolution of 2560x1080, and Chrome 
maximized with the Bookmarks Toolbar disabled.
x_pad = 321
y_pad = 144
Play area =  x_pad+1, y_pad+1, 959, 623
"""

# Globals
# ------------------
 
x_pad = 321
y_pad = 144

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+479)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()