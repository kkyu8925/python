import os
from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("680x450")

filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename):  # 파일 있으면 True, 없으면 False
        with open("mynote.txt", "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())


def save_file():
    with open("mynote.txt", "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))  # 모든 내용을 가져와서 저장


menu = Menu(root)
# File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# Edit Menu
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집")

# Templeate Menu
menu.add_cascade(label="서식")

# View Menu
menu.add_cascade(label="보기")

# Help Menu
menu.add_cascade(label="도움말")

# scroll-bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Text
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", expand=True, fill="both")

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
