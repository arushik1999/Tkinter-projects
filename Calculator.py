from tkinter import *
root=Tk()

root.geometry("198x287")
root.minsize(198,287)
root.maxsize(198, 287)

root.title("Calculator")

envalue=StringVar()
en=Frame(root,relief=SUNKEN,borderwidth=4)
en.pack(fill=X,pady=3)
Entry(en,textvariable=envalue,font="lucida 9 bold").pack(fill=X)

f1=Frame(root,relief=GROOVE,borderwidth=2,width=43,bg='#333')
f1.pack(side=LEFT,fill=Y,padx=3)
f1.config(width=150)

def click(event):
        global envalue
        value=str(event.widget.cget("text"))
        if value=='=':
                try:
                        if envalue.get().isdigit():
                                envalue.set(envalue.get())
                        else:
                                x=eval(envalue.get())
                                envalue.set(x)
                except:
                        envalue.set('Error')
        elif value=="c":
                envalue.set("")
        else:
                envalue.set(envalue.get()+value)
k=0
l=0
c=0
for j in range(1,10)[::-1]:
    b1=Button(f1,text=j,padx=16,pady=19)
    b1.place(x=k,y=l)
    b1.bind('<Button-1>',click)
    k+=50
    c+=1
    if c==3:
        l+=65
        c=0
        k=0

b1=Button(f1,text="0",padx=15,pady=15)
b1.place(x=k+50,y=l)
b1.bind('<Button-1>',click)
b1=Button(f1,text=".",padx=15,pady=15)
b1.place(x=k+2,y=l)
b1.bind('<Button-1>',click)
b1=Button(f1,text="00",padx=15,pady=15)
b1.place(x=k+98,y=l)
b1.bind('<Button-1>',click)


f2=Frame(root,relief=GROOVE,borderwidth=2,bg="#333")
f2.pack(side=RIGHT,fill=Y,padx=3)
f2.config(width=150)

x1=0
y1=0
sign=['c','=','+','-','*','/']
for j in sign:
        if j!='-' or j!='c' or j!='*' or j!='/':
                b1=Button(f2,text=j,padx=8,pady=6)
                b1.place(x=x1,y=y1)
                b1.bind('<Button-1>',click)
        if j=='c' or j=='*' or j=='/' or j=='-':
                b1=Button(f2,text=j,padx=9,pady=6,width='1')
                b1.place(x=x1,y=y1)
                b1.bind('<Button-1>',click)
        y1+=43
root.mainloop()