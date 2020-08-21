
from tkinter import *
from tkinter.ttk import *  #imports thettkor themed Tk widget library

root = Tk()  # create root window
root.title("Planner Frame")
root.config(bg="pink")

# create frame widget
left_frame = Frame(root, width=400, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)


root.mainloop()
