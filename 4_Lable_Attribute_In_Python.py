# Label Attribute

from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("GUI Application")   # this code for changing title

# Important Label Options In Python
# text - add the text
# bd - background
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text ='''
Doston kya aap budget me "Video Editing" or "Gaming" ke liye PC \n build karne ke baare me soch rahe hai \n to aaj mai aapko is Article "Best budget video editing Pc build kaise kare" or \n "Best budget gaming Pc build kaise kare"\n ke baare me subkuch batane wala hu, to chaliye jaante hai "best video editing pc in 2019" \n or "best gaming pc in 2019" ke baare me.
''', bg="red", fg="white", padx=75, pady=95, font="Castellar 12 bold", borderwidth=3,relief=SUNKEN)

# Important Pack Options

# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady


# title_label.pack(anchor ="nw")
# title_label.pack(anchor ="se")
# title_label.pack(side=BOTTOM, anchor ="se")
# title_label.pack(side=LEFT, fill=X)
# title_label.pack(side=LEFT, fill=Y)




title_label.pack()

root.mainloop()

