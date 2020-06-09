import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollideDay(data):
    for i in range(190, 365):
        for j in range(423, 500):
            if data[i, j] < 100:
                hit("up")
                return
    return
def isCollideNight(data):

    for i in range(190, 380):
        for j in range(423, 500):
            if data[i, j] > 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        for i in range(100, 101):
            for j in range(799, 800):
                if data[i, j] > 100:
                    isCollideDay(data)
                else:
                    isCollideNight(data)
