from tkinter import *

window = Tk()

frame = Frame(window, bd=5, relief=SUNKEN)
frame.pack()

button1 = Button(frame, text="W", font=('Arial', 30, "bold")).pack(side=TOP)

button2 = Button(frame, text="A", font=('Arial', 30, "bold")).pack(side=LEFT)

button1 = Button(frame, text="S", font=('Arial', 30, "bold")).pack(side=LEFT)

button1 = Button(frame, text="D", font=('Arial', 30, "bold")).pack(side=LEFT)

window.mainloop()