from tkinter import *
root = Tk()
root.geometry("655x335")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

f3 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
f3.pack(side=BOTTOM, fill="x")

l = Label(f1, text="Welcome To Python Frame_1")
l.pack(pady=142)

l = Label(f2, text="Welcome To Python Frame_2", font="Arial 14 bold", fg="red")
l.pack(padx=50)

l = Label(f3, text="Welcome To Python Frame_3", font="Arial 14 bold", fg="red")
l.pack(padx=50)
root.mainloop()