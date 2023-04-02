import pyautogui
import time
while True:
    # 獲取當前滑鼠的座標
    x, y = pyautogui.position()
    print(f'Current mouse position: ({x}, {y})')
    time.sleep(0.1)