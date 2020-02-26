# Basic GUI Program

from tkinter import *

root = Tk()

# first width x second height

root.geometry("400x300")

# width, height (by using we can give min size of window

root.minsize(300,200)

# width, height (by using we can give max size of window

root.maxsize(500, 400)

name = Label(text="We are printing demo text in GUI")

name.pack()

root.mainloop()