from tkinter import *

m = Tk()

m.title("Labels")

lb1 = Label(m, fg="white", text="Red", bg="red", width=20, height=3)
lb2 = Label(m, fg="white", text="Green", bg="green", width=20, height=3)
lb3 = Label(m, fg="white", text="Blue", bg="blue", width=20, height=3)

lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)
lb3.grid(row=1, column=0,columnspan=2, sticky=W+E)

m.mainloop()