from tkinter import *
import os
import json
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
YELLOW = "#f7f5dd"
PINK = "#e2979c"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

base_file = os.path.dirname(__file__)
file_path = os.path.join(base_file, "data", "french_words.csv")

current_card = {}
to_learn = {}
try:
    content = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pd.read_csv(file_path)
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = content.to_dict(orient="records")


def change_card():
    global current_card, flip_timmer
    windows.after_cancel(flip_timmer)
    current_card = random.choice(to_learn)
    data = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=data, fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timmer = windows.after(3000, flip_card)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_card()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
base_path = os.path.dirname(__file__)
card_front = os.path.join(base_path, "images", "card_front.png")
card_back = os.path.join(base_path, "images", "card_back.png")
correct_button = os.path.join(base_path, "images", "right.png")
wrong_button = os.path.join(base_path, "images", "wrong.png")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
windows = Tk()
windows.title("Flash Card")
windows.minsize(width=600, height=500)
windows.config(bg=BACKGROUND_COLOR)
windows.config(padx=50, pady=50)

flip_timmer = windows.after(3000, flip_card)
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0)

front_image = PhotoImage(file=card_front)
back_image = PhotoImage(file=card_back)
card_background = canvas.create_image(400, 250, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 250, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file=wrong_button)
wrong_image = wrong_image.subsample(2, 2)
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1, padx=100)

correct_image = PhotoImage(file=correct_button)
correct_image = correct_image.subsample(2, 2)
correct_button = Button(image=correct_image, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1, padx=100)


change_card()
windows.after(3000, flip_card)

windows.mainloop()
