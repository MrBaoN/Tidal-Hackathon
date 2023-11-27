import tkinter as tk
from tkinter import filedialog
import os
import predict as jk


def button_press_no():
    """Add 0 to list button_presses when pressed no"""
    global button_presses
    button_presses.append(0)

def button_press_yes():
    """Add 1 to list button_presses when pressed yes"""

    global button_presses
    button_presses.append(1)


def question(question_text):
    """Load GUI for each question"""

    q = tk.Label(master=frame_b, text=question_text, pady=7)
    q.pack()
    q_frame = tk.Frame(master=frame_b, pady=3)
    option_1 = tk.Button(master=q_frame, text="Yes", command=button_press_yes)
    option_1.pack(side="left")
    option_2 = tk.Button(master=q_frame, text="No", command=button_press_no)
    option_2.pack(side="left")
    q_frame.pack()


def last_page():
    """Loading result page and show improvement page as well."""

    global frame_a, frame_b, button_presses, final
    print(button_presses)
    frame_b.destroy()
    frame_b = tk.Frame()
    for i, val in enumerate(improvement(button_presses)):
        if val == 0:
            continue
        else:
            label = tk.Label(master=frame_b, text=improvement_text[i], pady=2, font=("Times New Roman", 16))
            label.pack()
    if final:
        final_result = tk.Label(master=frame_b, text="Your students think you are good", pady=3,
                                font=("Times New Roman", 18))
    else:
        final_result = tk.Label(master=frame_b, text="Your students think you need improvement", pady=3,
                                font=("Times New Roman", 18))
    final_result.pack()
    frame_b.pack()


def next_screen():
    global frame_a, frame_b, next_frame
    frame_b.destroy()
    next_frame.destroy()
    frame_b = tk.Frame()
    question("Do you teach with a presentation?")
    question("Are you interested in other approach of teaching?")
    question("Do you upload slides online?")
    question("Does your class require students to spend extra time outside of classes?")
    question("Do you have good TA?")
    question("Do students find your assignments hard?")
    question("Does your student find your quizzes hard?")
    question("Are your student passing?")
    submit_frame = tk.Frame(master=frame_b, height=15, pady=10)
    submit_frame.pack(side="bottom")
    submit_button = tk.Button(master=submit_frame, text="Submit", height=1, width=8, command=last_page)
    submit_button.pack()
    frame_b.pack()


def UploadAction(event=None):
    """Uploading csv file of google doc survey to train model"""

    global file, final
    filename = filedialog.askopenfilename(title="Select a File")
    print('Selected:', filename)

    # input file path to predict.h5 into file
    file = "predict.h5"
    final = jk.main(file)


def improvement(answer_list):
    """Based on answer, provide what needs to be improved upon"""

    improve_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for answer in range(len(answer_list)):
        if not answer_list[answer] and answer < 5:
            improve_list[answer] = 1
        elif answer_list[answer] and answer < 7:
            improve_list[answer] = 1
        elif not answer_list[answer] and answer > 6:
            improve_list[answer] = 1
    return improve_list


final = True  # from roshaan's file
file = ''  # to roshan's file after selecting file
improvement_text = ['Add more presentation', 'Try other approach of teaching', 'Upload slides online',
                    'Encourage students to study outside of class', 'Get better TA', 'Lower difficulty of assignment',
                    'Lower difficulty of quizzes', 'Encourage students to go to office hour',
                    'Lower the class difficulty']
button_presses = []

# Creating GUI for the program
window = tk.Tk()
screen_width = 800
screen_length = 800
window.resizable(False, False)
window.geometry(str(screen_width) + "x" + str(screen_length))
window.title("Home page")
frame_a = tk.Frame(padx=5, pady=5)
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="LikeYourProfessor", background="lightblue", foreground="blue",
                   height=screen_length // 150, width=screen_width // 8,
                   font=("Times New Roman", screen_length // 35, "bold"))
label_a.pack()

label_b = tk.Label(master=frame_b, text="Upload .csv File: ", height=screen_length // 100, width=screen_width // 8,
                   font=("Times New Roman", screen_length // 50, "bold"))
text_box = tk.Button(master=frame_b, width=50, text="Select File", command=UploadAction)
label_b.pack(pady=1)
text_box.pack()

next_frame = tk.Frame(height=30, pady=10)
next_frame.pack(side="bottom")

next_button = tk.Button(master=next_frame, text="Next", height=screen_length // 200, width=screen_width // 50,
                        command=next_screen)
next_button.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
