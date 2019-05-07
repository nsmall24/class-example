# I really don't like using wildcard imports, even if it is more typing
import tkinter as tk
import csv
import datetime

m = tk.Tk()
m.title("Running Pace Calculator")
m.configure(padx=15, pady=15, bg="#CCEECC")

# because not using wildcard import
N, S, E, W = tk.N, tk.S, tk.E, tk.W

# easier than keeping track of which entry field is which
mins = tk.StringVar()
secs = tk.StringVar()
miles = tk.StringVar()
month = tk.StringVar()
day = tk.StringVar()
year = tk.StringVar()
pace = tk.StringVar()

def usetoday():
    today = datetime.date.today()
    today_year, today_month, today_day = str(today).split("-")
    month.set(today_month)
    day.set(today_day)
    year.set(today_year)

def calc_pace(minutes, seconds, distance):
    total_seconds = (minutes * 60) + seconds # total seconds
    pace_total = total_seconds / distance    # pace in seconds
    pace_min = int(pace_total / 60)          # minutes part of pace
    pace_sec = round(pace_total % 60)        # seconds part of pace
    return f"{pace_min}:{pace_sec:02}"

def showpace():
    pace.set(calc_pace(int(mins.get()), float(secs.get()), int(miles.get())))

def savepace():
    global month, day, year
    pace = calc_pace(int(mins.get()), float(secs.get()), int(miles.get()))
    month, day, year = month.get(), day.get(), year.get()
    print(pace, month, day, year)
    clearfields()

def clearfields():
    mins.set("")
    secs.set("")
    miles.set("")
    month.set("")
    day.set("")
    year.set("")
    pace.set("")

# title label
lb1 = tk.Label(
    m, text="Running Pace Calculator", fg="darkblue", font=("Cambria Bold", 20), bg="#CCEECC")
# time input
lb2 = tk.Label(m, text="Time (mm:ss):  ", font=("none", 14), bg="#CCEECC")
fr1 = tk.Frame(m, bg="#CCEECC")
en1 = tk.Entry(fr1, width=4, font=("none", 14), textvariable=mins)
lb3 = tk.Label(fr1, text=":", font=("none", 14), bg="#CCEECC")
en2 = tk.Entry(fr1, width=4, font=("none", 14), textvariable=secs)
# miles input
lb4 = tk.Label(m, text="Miles:  ", font=("none", 14), bg="#CCEECC")
en3 = tk.Entry(m, font=("none", 14), textvariable=miles)
# date input
lb5 = tk.Label(m, text="Date:  ", font=("none", 14), bg="#CCEECC")
bt1 = tk.Button(m, text="Use Today", font=("none", 12), command=usetoday)
# numbering is off because I added lb10 afterward (layout was initially different)
lb10 = tk.Label(m, text="Or enter past date:", font=("none", 11, "italic"), bg="#CCEECC")
lb6 = tk.Label(m, text="Month", font=("none", 13), bg="#CCEECC")
lb7 = tk.Label(m, text="Day", font=("none", 13), bg="#CCEECC")
lb8 = tk.Label(m, text="Year", font=("none", 13), bg="#CCEECC")
en4 = tk.Entry(m, font=("none", 14), width=5, textvariable=month)
en5 = tk.Entry(m, font=("none", 14), width=5, textvariable=day)
en6 = tk.Entry(m, font=("none", 14), width=5, textvariable=year)
lb9 = tk.Label(m, text="(ex: 4 8 2019)  ", font=("none", 11, "italic"), bg="#CCEECC")
# show pace
bt2 = tk.Button(m, text="Show Pace", font=("none", 13), command=showpace)
lb11 = tk.Label(m, text="Pace/Mile:  ", font=("none", 14), bg="#CCEECC")
en7 = tk.Entry(m, font=("none", 14), textvariable=pace)
# save button
bt3 = tk.Button(m, text="Save", font=("none", 14, "bold"), command=savepace)

# grid everything
lb1.grid(row=0, column=0, columnspan=4, pady=(0, 10))
lb2.grid(row=1, column=0, sticky=E, pady=5)
fr1.grid(row=1, column=1, columnspan=3, sticky=W)
lb4.grid(row=2, column=0, sticky=E, pady=5)
en3.grid(row=2, column=1, sticky=W, columnspan=3)
lb5.grid(row=3, column=0, sticky=E)
bt1.grid(row=3, column=1, columnspan=3, sticky=W, pady=(8, 0))
lb10.grid(row=4, column=1, columnspan=3, sticky=W, pady=5)
lb6.grid(row=5, column=1, sticky=S+W)
lb7.grid(row=5, column=2, sticky=S+W)
lb8.grid(row=5, column=3, sticky=S+W)
en4.grid(row=6, column=1, sticky=W, padx=(0, 8))
en5.grid(row=6, column=2, sticky=W, padx=(0, 8))
en6.grid(row=6, column=3, sticky=W+E)
lb9.grid(row=6, column=0, sticky=E, pady=(5, 0))
bt2.grid(row=7, column=1, columnspan=3, sticky=W, pady=15)
lb11.grid(row=8, column=0, sticky=E)
en7.grid(row=8, column=1, sticky=W, columnspan=3)
bt3.grid(row=9, column=1, sticky=W, columnspan=3, pady=(15, 0))
# inside fr1
en1.grid(row=0, column=0)
lb3.grid(row=0, column=1)
en2.grid(row=0, column=2)

m.mainloop()