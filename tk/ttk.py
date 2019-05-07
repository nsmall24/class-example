import tkinter as tk
from tkinter import ttk

m = tk.Tk()

lb1 = tk.Label(m, text="Default button: ")
bt1 = tk.Button(m, text="Button")

lb2 = tk.Label(m, text="ttk button: ")
bt2 = ttk.Button(m, text="Button")

lb1.grid(row=0, column=0, sticky=tk.E, pady=10)
lb2.grid(row=1, column=0, sticky=tk.E, pady=10)
bt1.grid(row=0, column=1, sticky=tk.W, pady=10)
bt2.grid(row=1, column=1, sticky=tk.W, pady=10)

m.mainloop()