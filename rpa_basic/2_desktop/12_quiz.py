import pyautogui
import sys
import pyperclip

pyautogui.hotkey("win", "r")  # 단축키 : win + r 입력
pyautogui.write("mspaint")  # 프로그램 명  입력
pyautogui.press("enter")  # 엔터 키 입력

# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]  # 그림판 1개만 띄워져 있다고 가정
if window.isMaximized == False:
    window.maximize()  # 최대화

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png", confidence=0.8)
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
# pyautogui.click(500, 500, duration=0.5)

# tip
btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 200, btn_brush.top + 200)


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


my_write("참 찾했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n")  # 저장하지 않음
