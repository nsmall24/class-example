from tkinter import *

def down5():
    tip_percent.set(tip_percent.get() - 5)
def down1():
    tip_percent.set(tip_percent.get() - 1)
def up1():
    tip_percent.set(tip_percent.get() + 1)
def up5():
    tip_percent.set(tip_percent.get() + 5)

def calc():
    try:
        meal = float(meal_total.get())
    except ValueError:  # if no value was entered
        meal_total.set("0.00")
        meal = 0
    t = tip_percent.get() / 100
    tipamt = meal*t
    tip_amount.set(f"${tipamt:.2f}")
    meal_and_tip.set(f"${meal+tipamt:.2f}")

m = Tk()
m.title("Tip Calculator")
m.configure(bg="#EECCEE", padx=14, pady=14)

# again doing it like this
meal_total = StringVar()  # not int so that it can be empty by default
tip_percent = IntVar(value=20)
tip_amount = StringVar()
meal_and_tip = StringVar()

# Labels - title an first 3
labt=Label(m, text='Tip Calculator', 
    fg='#0000AA', bg="#EECCEE", pady=6, font=('Cambria', 24, 'bold'))
lab1=Label(m, text='Meal Total ', bg="#EECCEE", font=('none', 14), pady=6)
lab2=Label(m, text='Tip Percent ', bg="#EECCEE", font=('none', 14), pady=6)
lab3=Label(m, text='Adjust Tip % ', bg="#EECCEE", font=('none', 14), pady=6)

# Entry - first 2
ent1 = Entry(m, font=("none", 14), width=10, textvariable=meal_total)
ent1.focus() # have it focused by default
ent2 = Entry(m, font=("none", 14), width=10, textvariable=tip_percent)

fra1 = Frame(m, bg="#CCEECC") # for 4 buttons
btn1=Button(fra1, text='<<', font=("none", 10), command=down5)
btn2=Button(fra1, text='<', font=("none", 10), command=down1)
btn3=Button(fra1, text='>', font=("none", 10), command=up1)
btn4=Button(fra1, text='>>', font=("none", 10), command=up5)

btn5=Button(m, text='Calculate', font=("none", 14, 'bold'), command=calc)
lab4=Label(m, text='Tip Amount ', bg="#EECCEE", font=('none', 14), pady=6)
lab5=Label(m, text='Meal & Tip ', bg="#EECCEE", font=('none', 14), pady=6)
# Entry - bottom 2
ent3 = Entry(m, font=("none", 14), width=10, textvariable=tip_amount, state="readonly")
ent4 = Entry(m, font=("none", 14), width=10, textvariable=meal_and_tip, state="readonly")

# grid layout
labt.grid(row=0, columnspan=2)
lab1.grid(row=1, column=0, sticky=E)
lab2.grid(row=2, column=0, sticky=E)
lab3.grid(row=3, column=0, sticky=E)
ent1.grid(row=1, column=1, sticky=W)
ent2.grid(row=2, column=1, sticky=W)
fra1.grid(row=3, column=1, sticky=W)
btn1.grid(row=0, column=0, sticky=W) # fra1
btn2.grid(row=0, column=1, sticky=W) # fra1
btn3.grid(row=0, column=2, sticky=W) # fra1
btn4.grid(row=0, column=3, sticky=W) # fra1
btn5.grid(row=4, column=1, sticky=W)
lab4.grid(row=5, column=0, sticky=E)
lab5.grid(row=6, column=0, sticky=E)
ent3.grid(row=5, column=1, sticky=W)
ent4.grid(row=6, column=1, sticky=W)

m.mainloop()