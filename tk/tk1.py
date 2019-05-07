import tkinter as tk

root = tk.Tk()

root.title("OwO")

lab1 = tk.Label(root, text="Hello tkinter!", fg="white", bg="red", padx=24, font=("Arial",24))
lab1.pack()

btn1 = tk.Button(root, text="Close", bg="gray", command=root.quit, font=("Arial",18))
btn1.pack(fill=tk.X)

root.mainloop()