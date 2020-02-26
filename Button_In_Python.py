from tkinter import *
root = Tk()
root.geometry("655x335")

def add():
    a=5
    b=4
    print(a+b)

f1 = Frame(root, bg="grey", borderwidth=1)
f1.pack(side=LEFT, anchor="nw")

b1 = Button(f1, fg="red", text="Click", font="Arial 14 ", command=add)
b1.pack(side=LEFT, padx=15)

root.mainloop()