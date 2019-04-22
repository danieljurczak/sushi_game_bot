import PIL.ImageGrab as ImageGrab
import os
import time
import win32api, win32con
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

class Cord:
     
    f_shrimp = (33, 330)
    f_rice = (91, 333)
    f_nori = (22, 392)
    f_roe = (124, 388)
    f_salmon = (14, 441)
    f_unagi = (99, 435)

#--------------------------------

    phone = (589, 355)
 
    menu_toppings = (556, 270)
     
    t_shrimp = (507, 218)
    t_nori = (577, 224)
    t_roe = (491, 273)
    t_salmon = (566, 274)
    t_unagi = (498, 334)
    t_exit = (587, 330)
 
    menu_rice = (540, 292)
    buy_rice = (546, 272)
     
    delivery_norm = (498, 292)
"""
Plate cords: 
    45 207
    141 204
    245 208
    340 207
    440 215
    546 213

"""
def clear_tables():
    mousePos((45, 207))
    leftClick()
 
    mousePos((141, 204))
    leftClick()
 
    mousePos((245, 208))
    leftClick()
 
    mousePos((340, 207))
    leftClick()
 
    mousePos((440, 215))
    leftClick()
 
    mousePos((546, 213))
    leftClick()
    time.sleep(1)

def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print('Making a onigiri')
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0],y_pad + cord[1]))

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+479)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
    '.png', 'PNG')

def startGame():
    #location of first menu
    mousePos((321, 198))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((304, 394))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((588, 458))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((302, 374))
    leftClick()
    time.sleep(.1)

def main():
    pass

 
if __name__ == '__main__':
    main()