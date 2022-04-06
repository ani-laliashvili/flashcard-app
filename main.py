import tkinter
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
WORD = ''
WORDS_TO_LEARN = []
COL1 = ''
COL2 = ''
FILE_NAME = 'french_words.csv'

def save_progress():
    WORDS_TO_LEARN.append(WORD)

    if len(data_dict) != 0:
        data_dict.remove(WORD)

    pd.DataFrame(data_dict).to_csv("data/words_to_learn.csv", index=False)

    new_flashcard()

def read_data():
    try:
        data=pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv(f"data/{FILE_NAME}")
    except pd.errors.EmptyDataError:
        data = pd.read_csv(f"data/{FILE_NAME}")
    return data

def right_answer():
    show_answer()
    pass

def wrong_answer():
    show_answer()
    pass

#--------------Show answer-----------#
def new_flashcard():
    if len(data_dict) > 0:
        global WORD, flip_timer
        window.after_cancel(flip_timer)
        WORD = random.choice(data_dict)
        canvas.itemconfig(flashcard_image, image=card_front)

        canvas.itemconfig(title, text=COL1, fill='black')
        canvas.itemconfig(word, text=WORD[COL1], fill='black')
        flip_timer = window.after(3000, flip_card)
    else:
        messagebox.showinfo(title="Learning Complete!", message="All words have been learned. \nFlashcard app will now close.")
        quit()

def flip_card():
    canvas.itemconfig(flashcard_image, image=card_back)

    canvas.itemconfig(title, text=COL2, fill='white')
    canvas.itemconfig(word, text=WORD[COL2], fill='white')

#-----------------UI-----------------#
data = read_data()
COL1 = data.columns.values[0]
COL2 = data.columns.values[1]
data_dict = data.to_dict(orient="records")

window = tkinter.Tk()
window.title("Flash Card App")
window.minsize(width=800, height=528)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = tkinter.Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
right_image = tkinter.PhotoImage(file="images/right.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")

flashcard_image = canvas.create_image((410, 300), image=card_front)
title = canvas.create_text((400, 150), text='', font=("Arial", 40, "italic"))
word = canvas.create_text((400, 263), text='', font=("Arial", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=2)

flip_timer = window.after(3000, flip_card)

new_flashcard()

#Buttons
right = tkinter.Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=save_progress)
right.grid(row=1, column = 2)

wrong = tkinter.Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_flashcard)
wrong.grid(row=1, column = 1)

window.mainloop()