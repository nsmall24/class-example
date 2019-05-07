# :)

from tkinter import *

m = Tk()
m.title("Tkinter Color Labels")

v = StringVar()

l1 = 0
l2 = 0
l3 = 0

def togglelab1():
    global l1
    if l1 == 0:
        lab1.config(bg="teal", text="Teal Label")
    else:
        lab1.config(bg="red", text="Red Label")
    l1 = 1 - l1
    v.set("Label 1 Changed!")

def togglelab2():
    global l2
    if l2 == 0:
        lab2.config(bg="purple", text="Purple Label")
    else:
        lab2.config(bg="green", text="Green Label")
    l2 = 1 - l2
    v.set("Label 2 Changed!")

def togglelab3():
    global l3
    if l3 == 0:
        lab3.config(bg="#878700", text="Yellow Label")
    else:
        lab3.config(bg="blue", text="Blue Label")
    l3 = 1 - l3
    v.set("Label 3 Changed!")

# frame 1 with labels
fr1 = Frame(m)
lab1 = Label(fr1, text="Red Label", fg="white",bg="red", width=12, height=6, font=("Cambria", 24))
lab2 = Label(fr1, text="Green Label", fg="white", bg="Green", width=12, height=6, font=("Cambria", 24))
lab3 = Label(fr1, text="Blue Label", fg="white", bg="Blue", width=12, height=6, font=("Cambria", 24))

# frame 2 with buttons and text changed label
fr2 = Frame(m, pady=12)
btn1 = Button(fr2, text="Change Label 1", padx=6, font=("none", 16), command=togglelab1)
btn2 = Button(fr2, text="Change Label 2", padx=6, font=("none", 16), command=togglelab2)
btn3 = Button(fr2, text="Change Label 3", padx=6, font=("none", 16), command=togglelab3)
lab4 = Label(fr2, textvariable=v, fg="red", font=("Cambria", 20))

# pack everything
fr1.pack()
lab1.pack(side=LEFT, fill=Y)
lab2.pack(side=LEFT, fill=Y)
lab3.pack(side=LEFT, fill=Y)
fr2.pack()
lab4.pack(side=BOTTOM)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)

m.mainloop()