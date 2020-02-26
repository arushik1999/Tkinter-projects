from tkinter import *
##import Prog2 as ofnew
import sys
##from Tkinter import *
import time, datetime
##from numpy import arange

class AddOffset():

    def getOffsetsPipe1FWD(self):
        print('correct')
        temp1 = self.StartFreqOffsets.get()
        print ('temp1')

    def __init__(self, top):
        self.mOffsets = Toplevel(top)
        ## all new windows will be at the same location
        ## (on top of each other)
        self.mOffsets.geometry('1000x600+100+100')
        self.mOffsets.title('Enter the Offsets')
        self.StartFreqOffsets = DoubleVar()
        self.StartFreqOffsets.set(1)
        labelenterStartFreqOffsets = Label(self.mOffsets, text = 'Enter the Start Frequency (in MHz):')
        labelenterStartFreqOffsets.place(x = 0, y = 50)
        Entry(self.mOffsets, textvariable = self.StartFreqOffsets).place(x = 250, y = 50)

        buttonPipe1FWD = Button(self.mOffsets, text = 'Pipe 1 FWD',
                                command = self.getOffsetsPipe1FWD)
        buttonPipe1FWD.place(x = 30, y = 300)

def askOffsets():
    print
    'Correct till here'
    of = AddOffset(mGui)


mGui = Tk()
mGui.geometry('1000x600+150+100')
buttonYesOffsets = Button(text='YES', command=askOffsets)
buttonYesOffsets.place(x=300, y=350)
mGui.mainloop()