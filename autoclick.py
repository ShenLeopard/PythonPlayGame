"""三國無雙霸，實現坐騎特質自動洗煉"""
import threading
import keyboard
import cv2
import numpy as np
import pyautogui
import time
# 定義擷取範圍(要擷取的區域)
x1, y1, x2, y2 = 315, 201, 347, 247
def do_something():
    global stopFlag
    while not stopFlag:
        # 擷取螢幕畫面
        screenshot = pyautogui.screenshot()

        # 將圖片轉換為 numpy 的數組格式，並轉換顏色空間為 BGR
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # 裁剪擷取範圍
        screen_region = img[y1:y2, x1:x2]

        # 計算擷取範圍的平均像素值
        avg_pixel_value = np.mean(screen_region, axis=(0, 1))
        time.sleep(0.3)
        # 判斷平均像素值屬於紅色還是綠色
        # avg_pixel_value[1]是綠色通道，#avg_pixel_value[2]是紅色通道
        if avg_pixel_value[1] > avg_pixel_value[2]:
            print('green')
            pyautogui.click(x=1582, y=831)  # 先按保留特質
            time.sleep(0.5)
            pyautogui.click(x=1360, y=826)  # 繼續開始
            time.sleep(0.5)
        else:
            print('red')
            pyautogui.click(x=1203, y=823)  # 繼續洗練
            time.sleep(0.3)
        # 顯示圖像
        # cv2.imshow('Screen', img)

def detect_keypress():
    global stopFlag
    keyboard.wait('esc')
    print('ESC key pressed')
    stopFlag = True

stopFlag = False
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=detect_keypress)
t1.start()
t2.start()

t1.join()
t2.join()
# 釋放資源
cv2.destroyAllWindows()
