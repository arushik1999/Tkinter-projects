# Showing PNG Image on GUI

from tkinter import *

root = Tk()

root.geometry("400x300")

# Note: Only PNG Image Can be used

photo = PhotoImage(file="1.png")

Label = Label(image=photo)

Label.pack()

root.mainloop()