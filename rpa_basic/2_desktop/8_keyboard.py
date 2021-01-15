import pyautogui
import pyperclip

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("nodocoding", interval=1) # 입력속도
# pyautogui.write("한글은안됌.", interval=1)

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "1", "a", "enter", "enter", "enter"], interval=0.25)

# 특수 문자
# pyautogui.keyDown("shift")
# pyautogui.press("4") # '$'
# pyautogui.keyUp("shift")

# 조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl") # ctrl + a

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# pyautogui.hotkey("ctrl", "a")

# 한글 입력
# pip install pyperclip = 클립보드에 집어넣음
# pyperclip.copy("나도코딩, ")  # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v")  # 클립보드에 있는 내용 붙여넣기


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


my_write("너도코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q
