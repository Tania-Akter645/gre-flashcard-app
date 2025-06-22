import tkinter as tk
import csv
import random

# GRE word load
def load_words():
    with open("gre_words.csv", mode="r") as file:
        reader = csv.DictReader(file)
        return list(reader)

# for Timer Stop
def cancel_timer():
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

# show the next word
def next_card():
    global current_word, word_index, timer_id

    cancel_timer()

    if not words:
        word_label.config(text="Well done! 🎉")
        meaning_label.config(text="You've reviewed all words.")
        disable_buttons()
        return

    if shuffle_enabled.get():
        current_word = random.choice(words)
    else:
        if word_index >= len(words):
            word_label.config(text="Well done! 🎉")
            meaning_label.config(text="You've reviewed all words.")
            disable_buttons()
            return
        current_word = words[word_index]
        word_index += 1

    word_label.config(text=current_word["Word"])
    meaning_label.config(text="")

    # Start Countdown
    timer_id = root.after(5000, mark_unknown)  # 5 seconds

def disable_buttons():
    show_button.config(state=tk.DISABLED)
    know_button.config(state=tk.DISABLED)
    dont_know_button.config(state=tk.DISABLED)

def show_meaning():
    cancel_timer()
    meaning_label.config(text=current_word["Meaning"])

def mark_known():
    global score
    cancel_timer()
    if current_word in words:
        words.remove(current_word)
        score += 1
        score_label.config(text=f"Score: {score}")
    next_card()

def mark_unknown():
    cancel_timer()
    next_card()

# UI শুরু
root = tk.Tk()
root.title("GRE Flashcard App")
root.geometry("450x420")
root.config(bg="#2e2e2e")

words = load_words()
current_word = {}
word_index = 0
score = 0
timer_id = None

# Shuffle Toggle
shuffle_enabled = tk.BooleanVar(value=True)

word_label = tk.Label(root, text="", font=("Helvetica", 24), bg="#2e2e2e", fg="white")
word_label.pack(pady=30)

meaning_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#2e2e2e", fg="lightgreen")
meaning_label.pack()

score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14), bg="#2e2e2e", fg="orange")
score_label.pack(pady=5)

shuffle_check = tk.Checkbutton(root, text="Shuffle Mode", variable=shuffle_enabled,
                                bg="#2e2e2e", fg="white", selectcolor="#2e2e2e",
                                font=("Helvetica", 12), command=next_card)
shuffle_check.pack(pady=5)

button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(pady=20)

show_button = tk.Button(button_frame, text="Show Meaning", command=show_meaning, width=15)
show_button.grid(row=0, column=0, padx=5)

know_button = tk.Button(button_frame, text="I Know", command=mark_known, width=15, bg="green", fg="white")
know_button.grid(row=0, column=1, padx=5)

dont_know_button = tk.Button(button_frame, text="I Don't Know", command=mark_unknown, width=15, bg="red", fg="white")
dont_know_button.grid(row=0, column=2, padx=5)

next_card()
root.mainloop()

