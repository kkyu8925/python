import pyautogui

# fw = pyautogui.getActiveWindow()  # 현재 활성화된 창 (vscode)
# print(fw.title)  # 창의 제목 정보
# print(fw.size)  # 창의 크기 정보 (width, height)
# print(fw.left, fw.right, fw.top, fw.bottom)  # 창의 좌표 정보

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

w = pyautogui.getWindowsWithTitle("제목 없음")
print(w)
# if w.isActive == False:  # 현재 활성화가 되지 않았다면
#     w.activate()  # 활성화 (맨 앞으로 가져오기)

# if not w.isMaximized:  # 현재 최대화가 되지 않았다면
#     w.maximize()  # 최대화

# if not w.isMinimized:  # 현재 최소화가 되지 않았다면
#     w.maximize()  # 최소화

pyautogui.sleep(1)

w.restore()  # 화면 회복

w.close()  # 윈도우 닫기
