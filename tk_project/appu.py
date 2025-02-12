import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
import sqlite3


questions = ["“What is the maximum length of a Python identifier?",
             " How is a code block indicated in Python?",
             "_______ are software which is used to do a particular task.",
             "Father of ‘python’ programming language?",
             "Which of the following types of loops are not supported in Python?",
             "Which of the following functions converts date to corresponding time in Python?",
             "Who is the father of computer ethics?",
             "As what datatype are the *args stored, when passed into a function?",
             " What keyword is used in Python to raise exceptions?",
             "Which of the following is not a valid set operation in python?"]
            
choices = [["A. 16 ", "B. No fixed length is specified", "C. 32", "D. 128"],
           ["A. Indentation", "B. Uniform Resource Link", "C. Key", "D. Brackets"],
           ["A. Operating system", "B. Program", "C. Data", "D. Software"],
           ["A. Guido van Rossum", "B. Prof John Kemeny", "C. Thomas Kurtz", "D. Bill Gates"],
           ["A. for", "B. While", "C. do-while", "D. None of the above"],
           ["A. strptime()", "B. strftime()", "C. Both A and B", "D. None of the above"],
           ["A. Frederick Morton Eden", "B. Nell Mary Dunn", "C. Norbert Weiner", "D. Susannah Dobson"],
           ["A. List", "B. Dictionary", "C. Tuple", "D. None of the above"],
           ["A. raise ", "B. Try", "C. Goto", "D. Except"],
           ["A.Union", "B. Difference", "C. Intersection", "D.None of the above"]]
           
answers = [1, 0, 1, 0, 2, 0, 2, 2, 0, 3]

user_answers = []

indexes = []

def login():
    username ="deepak"
    password = "1"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        
        # Create a new window for courses
        a = tk.Toplevel()  # Use Toplevel instead of Tk() to create a new window
        a.title("Courses")
        a.geometry('800x600')
        a.configure()
        
        # Centralize the new window
        window_width = a.winfo_reqwidth()
        window_height = a.winfo_reqheight()
        position_right = int(a.winfo_screenwidth()/2 - window_width/2)
        position_down = int(a.winfo_screenheight()/2 - window_height/2)
        a.geometry("+{}+{}".format(position_right, position_down))
        
        course_label = tk.Label(a, text="Courses", bg='#333333', fg="#FFFFFF", font=("Arial", 35))
        options_list = ["PYTHON USING PROGRAMMING","OPERATING SYSTEM"]
        value_inside = tk.StringVar(a)
        value_inside.set("Select an Option")
        question_menu = tk.OptionMenu(a, value_inside, *options_list)
        question_menu.pack(pady=50)
        
        def print_answers():
            print("Selected Option: {}".format(value_inside.get()))
        
        submit_button = tk.Button(a, text='Submit', command=print)
        submit_button.pack()
     

    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def locals():
    local_window = tk.Toplevel()
    local_window.title("Local Information")
    local_window.geometry('400x400')
    local_window.configure(bg="#AD8B65")

    # Labels and Entry fields for different fields
    name_label = tk.Label(local_window, text="Name", font=("Arial", 16))
    name_label.pack(pady=10)
    name_entry = tk.Entry(local_window, font=("Arial", 14))
    name_entry.pack(pady=10)

    email_label = tk.Label(local_window, text="Email ID", font=("Arial", 16))
    email_label.pack(pady=10)
    email_entry = tk.Entry(local_window, font=("Arial", 14))
    email_entry.pack(pady=10)

    address_label = tk.Label(local_window, text="Address",   font=("Arial", 16))
    address_label.pack(pady=10)
    address_entry = tk.Entry(local_window, font=("Arial", 14))
    address_entry.pack(pady=10)

    phone_label = tk.Label(local_window, text="Phone Number",  font=("Arial", 16))
    phone_label.pack(pady=10)
    phone_entry = tk.Entry(local_window, font=("Arial", 14))
    phone_entry.pack(pady=10)

    college_label = tk.Label(local_window, text="College Name",  font=("Arial", 16))
    college_label.pack(pady=10)
    college_entry = tk.Entry(local_window, font=("Arial", 14))
    college_entry.pack(pady=10)

    password_label = tk.Label(local_window, text="Password",  font=("Arial", 16))
    password_label.pack(pady=10)
    password_entry = tk.Entry(local_window, show="*", font=("Arial", 14))
    password_entry.pack(pady=10)

    # Submit button with validation
    def submit_local_info():
        if name_entry.get() and email_entry.get() and address_entry.get() and phone_entry.get() and college_entry.get() and password_entry.get():
            # Perform validation or processing with the retrieved information if needed
            
            # Display a message indicating successful submission
            messagebox.showinfo("Success", "Local information submitted successfully!")
        else:
            # Display an error message if any field is empty
            messagebox.showerror("Error", "All fields are required!")

    submit_button = tk.Button(local_window, text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=submit_local_info)
    submit_button.pack(pady=20)


           

    






def print():
   appu=tk.Tk()
   appu.configure()
   label = tk.Label(appu, text="PYTHON USING PROGRAMMING")
   label1=tk.Label(appu,text="Python can be broadly divided into several key areas based on its usage and applications:",bg='#FFF8DC')
   label2=tk.Label(appu,text="Web Development: Python is widely used for web development. Frameworks like Django and Flask provide developers with powerful tools to create robust, scalable, and secure web applications and APIs")
   label3 = tk.Label(appu, text="Data Science and Analysis: Python is a go-to language for data scientists and analysts due to libraries such as NumPy, Pandas, and SciPy. These libraries provide efficient data manipulation, analysis, and visualization capabilities, making Python a top choice for data-related tasks.")
   label4 = tk.Label(appu, text="Machine Learning and Artificial Intelligence: Python offers extensive libraries like TensorFlow, Keras, and scikit-learn, enabling developers and researchers to build machine learning models, deep learning neural networks, and AI applications.")
   label5 = tk.Label(appu, text="Automation and Scripting: Python is excellent for writing scripts and automating repetitive tasks. Its simplicity and ease of use make it a preferred choice for tasks like file manipulation, data processing, and system automation.")
   label6 = tk.Label(appu, text="Game Development: While not as common as some other languages, Python is used in game development. Libraries like Pygame provide a foundation for creating 2D games and simulations.")
   label7 = tk.Label(appu, text="Desktop Applications: Python can be used for creating desktop applications with graphical user interfaces (GUI). The Tkinter library, which is part of the standard library, allows developers to build desktop applications with ease.")
   label8 = tk.Label(appu, text="Network Programming: Python is often used for network programming tasks due to its simplicity and support for networking protocols. Libraries like Twisted enable developers to create network servers, clients, and protocols efficiently.")
   label9 = tk.Label(appu, text="Scripting for Other Software: Python can be embedded in other software applications to allow users to script and automate tasks within those applications.")
   continue_button = tk.Button(appu, text='CONTINUE', bg="#FF3399", fg="#FFFFFF", command=callable)
        
   label.pack()
   label1.pack(padx=10,pady=10)
   label2.pack(padx=10,pady=30)
   label3.pack(padx=10,pady=30)
   label4.pack(padx=10,pady=30)
   label5.pack(padx=10,pady=30)
   label6.pack(padx=10,pady=30)
   label7.pack(padx=10,pady=30)
   label8.pack(padx=10,pady=30)
   label9.pack(padx=10,pady=30)
   continue_button.pack()

  





       
# Main window
window = tk.Tk()
window.title("Login form")ṣ
window.geometry('340x440')
window.configure()

def callabl():
    while len(indexes) < 10:
        x = random.randint(0, 9)
        if x not in indexes:
            indexes.append(x)


def show_result(score):
    messagebox.showinfo("Result", f"Your Score is {score}/10")


def calculate_score():
    global indexes, user_answers, answers
    score = 0
    for i in range(10):
        if user_answers[i] == answers[indexes[i]]:
            score += 1
    show_result(score)


ques = 1


def select(choice_index):
    global ques
    user_answers.append(choice_index)
    if ques < 10:
        l1.config(text=questions[indexes[ques]])
        for i in range(4):
            radio_buttons[i].config(text=choices[indexes[ques]][i])
        ques += 1
    else:
        calculate_score()


def callable():
    global win2, l1, radio_buttons, ques
    win2 = tk.Toplevel()
    win2.title("Quiz Window")
    win2.geometry("800x600")
    win2.configure()
    ques = 1
    indexes.clear()
    user_answers.clear()
    callabl()

    l1 = tk.Label(win2, text=questions[indexes[0]],bg='#FFF8DC',font=("arial", 25, "bold"))
    l1.pack(pady=20)

    radio_buttons = []
    for i in range(4):
        radio_button = tk.Radiobutton(win2, text=choices[indexes[0]][i], value=i,bg='#FFF8DC', font=("Arial", 16),
                                      command=lambda i=i: select(i))
        radio_button.pack(anchor="w")
        radio_buttons.append(radio_button)

    next_button = tk.Button(win2, text="Next", command=any)
    next_button.pack(pady=20)

def any():
    ao=tk.Tk()
    completion_label = tk.Label(ao, text="Completion Certification will be mailed soon", font=("cambria", 14))
    completion_label.pack(pady=20,padx=100)



# Create a frame for login widgets
frame = tk.Frame(window, bg='#333333')
frame.pack(expand=True)

# Creating login widgets
username_label = tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
login_button = tk.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)
create_button = tk.Button(frame, text="Create", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=locals)

# Placing login widgets
username_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
username_entry.grid(row=0, column=1, pady=10, sticky="w", padx=10)
password_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
password_entry.grid(row=1, column=1, pady=10, sticky="w", padx=10)
login_button.grid(row=2, column=0, columnspan=2, pady=20)
create_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the Tkinter main loop
window.mainloop()
