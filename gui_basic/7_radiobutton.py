from tkinter import *

root = Tk()
root.title("kkyu GUI")
root.geometry("640x480")

Label(root, text="Select the menu").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root,
                          text="Hamburger",
                          value=1,
                          variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root,
                          text="Cheese burger",
                          value=2,
                          variable=burger_var)
btn_burger3 = Radiobutton(root,
                          text="Chicken burger",
                          value=3,
                          variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="Select the drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Soda", value="Soda", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())


btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()
