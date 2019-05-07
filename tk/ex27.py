from tkinter import *
import csv

m =  Tk()
m.title("Attendees List")
m.configure(padx=20, pady=20, bg="#CCCCEE")

def showname():
    name_disp = f"{en1.get()} {en2.get()}"
    en3.delete(0, END)
    en3.insert(0, name_disp)

def clearfields():
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)

def addattendee():
    attendee = []
    firstname = en1.get()
    lastname = en2.get()
    attendee.append(firstname)
    attendee.append(lastname)
    with open("attendees.csv", "a", newline="") as writefile:
        writer = csv.writer(writefile)
        writer.writerow(attendee)

    clearfields()  # no need to enter same names again, probably

# entry labels
lb1 = Label(m, text="First", padx=6, pady=6, bg="#CCCCEE")
lb2 = Label(m, text="Last", padx=6, pady=6, bg="#CCCCEE")
# spacer labels
lb3 = Label(m, bg="#CCCCEE")
lb4 = Label(m, bg="#CCCCEE")
lb5 = Label(m, bg="#CCCCEE")
# entry fields
en1 = Entry(m, font=("none", 14))
en2 = Entry(m, font=("none", 14))
en3 = Entry(m, font=("none", 14))
# buttons (with more useful names)
bt1 = Button(m, padx=6, pady=6, text="Show full name", command=showname)
bt2 = Button(m, padx=6, pady=6, text="Clear fields", command=clearfields)
bt3 = Button(m, padx=6, pady=6, text="Add attendee", command=addattendee)

en1.grid(row=0, column=1, sticky=E)
en2.grid(row=1, column=1, sticky=E)
lb1.grid(row=0, column=0, sticky=W)
lb2.grid(row=1, column=0, sticky=W)
lb3.grid(row=2, column=1)
bt1.grid(row=3, column=1, sticky=E)
bt2.grid(row=3, column=0, sticky=W)
lb4.grid(row=4, column=1)
en3.grid(row=5, column=0, columnspan=2, sticky=E+W)
lb5.grid(row=6, column=1)
bt3.grid(row=7, column=1, sticky=E)

m.mainloop()