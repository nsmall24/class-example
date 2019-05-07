from tkinter import *

m = Tk()
m.title("Tkinter Color Labels")

v = StringVar()

def changepurple():
    lab1.config(bg="purple", text="Purple Label")
    showmessage()

def changered():
    lab1.config(bg="red", text="Red Label")
    showmessage()

def showmessage():
    v.set("Label Changed!")

# frame 1 with labels
fr1 = Frame(m)
lab1 = Label(fr1, text="Red Label", fg="white",bg="red", width=12, height=6, font=("Cambria", 24))
lab2 = Label(fr1, text="Green Label", fg="white", bg="Green", width=12, height=6, font=("Cambria", 24))
lab3 = Label(fr1, text="Blue Label", fg="white", bg="Blue", width=12, height=6, font=("Cambria", 24))

# frame 2 with buttons and text changed label
fr2 = Frame(m, pady=12)
btn1 = Button(fr2, text="Button 1", padx=6, font=("none", 16), command=changepurple)
btn2 = Button(fr2, text="Button 2", padx=6, font=("none", 16), command=changered)
btn3 = Button(fr2, text="Button 3", padx=6, font=("none", 16))
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