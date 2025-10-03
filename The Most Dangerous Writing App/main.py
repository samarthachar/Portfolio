import tkinter
from tkinter import *

time_left = 5

def check_type():
    global time_left
    text = notes.get("1.0", END)
    if text.strip():
        if notes.edit_modified():
            time_left = 5
            notes.edit_modified(False)
        else:
            time_left -= 1

        if time_left < 1:
            window.clipboard_clear()
            window.clipboard_append(text)
            notes.delete("1.0", END)
            time_left = 5
    timer.config(text=f"{time_left}")
    window.after(1000, check_type)


window = Tk()
window.title("The Most Dangerous Writing App")

window.configure(bg="#3A3A3A")
window.config(padx=50, pady=50)

title = Label(text="The Most Dangerous Writing App", font=("Helvetica", 60, "bold"), fg="#8B0000", bg="#3A3A3A")
title.grid(column=0, row=0, pady=10)

notes = Text(height=30, width=100, fg="white", bg="#3A3A3A",font=("Helvetica", 20))
notes.grid(column=0, row=1, padx=20, pady=10)

helper = Label(
    text="Don't worry: If you lost your work, it's on your clipboard.",
    font=("Helvetica", 8),
    fg="white",
    bg="#3A3A3A",
)
helper.grid(column=0, row=2, pady=10)

timer = Label(text="5", font=("Helvetica", 60),fg="white", bg="#3A3A3A")
timer.grid(column=2, row=0)

check_type()
window.mainloop()

