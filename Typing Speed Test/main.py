import random
import tkinter

from words import everyday_words
from tkinter import *

# ----- LOGIC -----#
def get_content():
    global seconds
    content = text_box.get("1.0", tkinter.END)
    if len(content.strip().split()) >= len(list_words):
        check_speed(content)
        return
    elif seconds >= 60:
        check_speed(content)
        return
    if len(content) > 2:
        seconds += 1
    window.after(1000, get_content)


def check_speed(data):
    count = 0
    for typed_word, actual_word in zip(data.strip().split(), list_words):
        if typed_word == actual_word:
            count +=1
    wpm = count / seconds * 60
    label = Label(text=f"You type at {wpm} words per minute")
    label.grid(column=1, row=10 , rowspan=3)
    text_box.config(state="disabled")
#-- GUI -- #

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

title = Label(text="Typing Speed Test", font=("Helvetica", 30, "bold"))
title.grid(column=1, row=0 , rowspan=3)

seconds = 0
text = ''

list_words = random.sample(everyday_words,50)
i = 0
for word in list_words:
    x = ''
    if i % 5 == 0 and i != 0:
        x = '\n'
    text += f'{word} {x}'
    i += 1

typing_text = Label(text=f"{text}", font=("Courier", 12), bg="#f4f4f4", fg="#333", justify="left", anchor="nw", padx=10, pady=10)
typing_text.grid(column=1, row=3, rowspan=3)

text_box = Text(height=10, width=50, font=("Arial", 12))
text_box.grid(column=1, row=11 , rowspan=3)
get_content()


window.mainloop()
