import pyautogui

# 화면 스크린 샷 만들기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 3059,19 60,63,65 #3C3F41
pixel = pyautogui.pixel(3059, 19)
print(pixel)

# print(pyautogui.pixelMatchesColor(3059, 19, (60, 63, 65)))
print(pyautogui.pixelMatchesColor(3059, 19, pixel))
