import tkinter as tk
from tkinter import messagebox
import random

# ... (questions, choices, answers, user_answers, indexes, and other functions remain unchanged) ...

# Function to handle the quiz completion message
def show_completion_message():
    completion_window = tk.Toplevel()
    completion_window.title("Completion Message")
    completion_window.geometry("400x200")
    completion_window.configure(bg='#333333')

    completion_label = tk.Label(completion_window, text="Completion Certification will be mailed soon", font=("Arial", 16), bg='#333333', fg="#FFFFFF")
    completion_label.pack(expand=True, padx=20, pady=40)

# Function to handle the quiz questions and answers
def start_quiz():
    global win2, l1, radio_buttons, ques
    win2 = tk.Toplevel()
    win2.title("Quiz Window")
    win2.geometry("800x600")

    ques = 1
    indexes.clear()
    user_answers.clear()
    callabl()

    l1 = tk.Label(win2, text=questions[indexes[0]], font=("arial", 25, "bold"))
    l1.pack(pady=20)

    radio_buttons = []
    for i in range(4):
        radio_button = tk.Radiobutton(win2, text=choices[indexes[0]][i], value=i, font=("Arial", 16),
                                      command=lambda i=i: select(i))
        radio_button.pack(anchor="w")
        radio_buttons.append(radio_button)

    next_button = tk.Button(win2, text="Next", command=any)
    next_button.pack(pady=20)

# ... (other functions remain unchanged) ...

# Main window
window = tk.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')

# Create a frame for login widgets
frame = tk.Frame(window, bg='#333333')
frame.pack(expand=True)

# ... (other login widgets remain unchanged) ...

# Placing login widgets
username_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
username_entry.grid(row=0, column=1, pady=10, sticky="w", padx=10)
password_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
password_entry.grid(row=1, column=1, pady=10, sticky="w", padx=10)
login_button.grid(row=2, column=0, columnspan=2, pady=20)
create_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the Tkinter main loop
window.mainloop()
