import pyautogui

# pyautogui.mouseInfo()

# pyautogui.FAILSAFE = False # 계속 동작
pyautogui.PAUSE = 1  # 모든 동작에 1초 sleep 적용

for i in range(10):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)
