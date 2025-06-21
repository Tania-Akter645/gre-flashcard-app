import tkinter as tk
import csv
import random

# GRE word load
def load_words():
    words = []
    with open("gre_words.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append(row)
    return words

# function of new word
def next_card():
    global current_word
    if words:
        current_word = random.choice(words)
        word_label.config(text=current_word["Word"])
        meaning_label.config(text="")
    else:
        word_label.config(text="Well done! 🎉")
        meaning_label.config(text="You've reviewed all words.")
        know_button.config(state=tk.DISABLED)
        dont_know_button.config(state=tk.DISABLED)

# function of word meaning
def show_meaning():
    meaning_label.config(text=current_word["Meaning"])

# remove already known word and increase score
def mark_known():
    global score
    words.remove(current_word)
    score += 1
    score_label.config(text=f"Score: {score}")
    next_card()

# donot learn — go to the next word
def mark_unknown():
    next_card()

# --- GUI start ---
root = tk.Tk()
root.title("GRE Flashcard App")
root.geometry("420x400")
root.config(bg="#2e2e2e")  # Dark Mode

words = load_words()
current_word = {}
score = 0

# label and  bottom create
word_label = tk.Label(root, text="", font=("Helvetica", 24), bg="#2e2e2e", fg="white")
word_label.pack(pady=30)

meaning_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#2e2e2e", fg="lightgreen")
meaning_label.pack()

score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14), bg="#2e2e2e", fg="orange")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(pady=20)

show_button = tk.Button(button_frame, text="Show Meaning", command=show_meaning, width=15)
show_button.grid(row=0, column=0, padx=5)

know_button = tk.Button(button_frame, text="I Know", command=mark_known, width=15, bg="green", fg="white")
know_button.grid(row=0, column=1, padx=5)

dont_know_button = tk.Button(button_frame, text="I Don't Know", command=mark_unknown, width=15, bg="red", fg="white")
dont_know_button.grid(row=0, column=2, padx=5)

# first show a word
next_card()

# run
root.mainloop()
