import pandas as pd
import tkinter.messagebox
from utils import get_unlocked_course, reset_completed
from tkinter import *
from tkinter import filedialog


df = pd.read_csv('course.csv')
df = df.fillna('')
df.set_index('Course', inplace=True)

completed_course = None
filepath = None

completed_course = pd.read_csv('completed_course.csv')
completed_course.replace(['YES', 'NO'], [True, False], inplace=True)
completed_course.set_index('Course', inplace=True)


def browsefunc1():
    filename = filedialog.askopenfilename(filetypes=(
        ("csv files", "*.csv"), ("All files", "*.*")))
    input1.insert(END, filename)


def submit1():
    filepath = input1.get()
    completed_course = pd.read_csv(filepath)
    completed_course.replace(['YES', 'NO'], [True, False], inplace=True)
    completed_course.set_index('Course', inplace=True)

    unlocked = get_unlocked_course(df, completed_course)
    unlocked_courses = '\n'.join(unlocked)
    tkinter.messagebox.showinfo("Unlocked Courses", unlocked_courses)
    reset_completed(completed_course)


def browsefunc2():
    filename = filedialog.askopenfilename(filetypes=(
        ("txt files", "*.txt"), ("All files", "*.*")))
    input2.insert(END, filename)


def submit2():
    filepath = input2.get()
    with open(filepath, mode='r', encoding='utf-8') as file:
        lines = list(map(lambda x: x.strip().upper(), file.read().split('\n')))
        for line in lines:
            completed_course.loc[line, 'Finished'] = True

    unlocked = get_unlocked_course(df, completed_course)
    unlocked_courses = '\n'.join(unlocked)
    tkinter.messagebox.showinfo("Unlocked Courses", unlocked_courses)
    reset_completed(completed_course)


def check(x):
    completed_course.loc[x,
                         'Finished'] = not completed_course.loc[x, 'Finished']


def submit3():
    unlocked = get_unlocked_course(df, completed_course)
    unlocked_courses = '\n'.join(unlocked)
    tkinter.messagebox.showinfo("Unlocked Courses", unlocked_courses)
    reset_completed(completed_course)


window = Tk()

photo = PhotoImage(file='folder.png')
photo = photo.subsample(13, 13)

label = Label(window, text='Use one of the methods')

frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)

label1 = Label(frame1, text='.csv file path')
input1 = Entry(frame1, width=40)
button1 = Button(frame1, image=photo, command=browsefunc1)
button2 = Button(frame1, text="Submit", command=submit1)

label2 = Label(frame2, text='.txt file path')
input2 = Entry(frame2, width=40)
button3 = Button(frame2, image=photo, command=browsefunc2)
button4 = Button(frame2, text="Submit", command=submit2)

label3 = Label(frame3, text="Choose the courses you've done so far")
checkboxes = {}
row, col = 2, 1
for i, r in df.iterrows():
    b = Checkbutton(frame3, text=i, command=lambda x=i: check(x))
    checkboxes[i] = b
    b.grid(row=row, column=col)
    row += 1
    if row > 10:
        col += 1
        row = 2


if row == 2:
    col -= 1
if col % 2 == 0:
    col = col // 2
else:
    col = col // 2 + 1


button5 = Button(frame3, text="Submit", command=submit3)

label.grid(row=1, column=1)
frame1.grid(row=2, column=1)
label1.grid(row=1, column=1)
input1.grid(row=2, column=1, columnspan=10)
button1.grid(row=2, column=11)
button2.grid(row=2, column=12)
frame2.grid(row=3, column=1)
label2.grid(row=1, column=1)
input2.grid(row=2, column=1, columnspan=10)
button3.grid(row=2, column=11)
button4.grid(row=2, column=12)
frame3.grid(row=4, column=1)
label3.grid(row=1, column=1, columnspan=5)
button5.grid(row=11, column=col, columnspan=row if row == 2 else 1)

window.mainloop()
