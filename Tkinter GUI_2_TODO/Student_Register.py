# import tkinter as tk

import csv
import os
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar
from tkcalendar import DateEntry

from Student import Student

# window = tk.Tk()
# window.title("Register")
#
# width = 600
# height = 500
# window.geometry(f"{width}x{height}")
#
# text = tk.Label(window, text="Hello world!")
# # text.pack()
#
# # text.grid(row=1, column=0)
# text.place(x=100, y=100)
#
# if __name__ == "__main__":
#     window.mainloop()

window = Tk()
window.title("Register")

width = 600
height = 300
window.geometry(f"{width}x{height}")
window['bg'] = 'LightBlue'

students = []


# def add():
#     student = Student(
#         fullname_entry.get(),
#         email_entry.get(),
#         dob_entry.get(),
#         gender_entry.get(),
#         phone_entry.get(),
#         course_entry.get(),
#         datetime.now(),
#
#     )
#     students.append(student.get_attrs(as_dict=True))
#     messagebox.showinfo('Information', 'The data has been added successfully')


def save():
    student = Student(
        fullname_entry.get(),
        email_entry.get(),
        dob_entry.get(),
        gender_entry.get(),
        phone_entry.get(),
        course_entry.get(),
        datetime.now(),

    )
    students.append(student.get_attrs(as_dict=True))
    messagebox.showinfo('Information', 'The data has been added successfully')

    with open('Students.csv', 'a', newline='\n') as file:
        header = ['Fullname', 'Email', 'DOB', 'Gender', 'Phone', 'Course', 'DOJ']
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize('Students.csv') == 0:
            csv_writer.writeheader()
        csv_writer.writerows(students)
        messagebox.showinfo('Information', 'Save successfully')


def clear():
    fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    course_entry.delete(0, END)


# Fullname
fullname_label = Label(window, text="Your name:", bg='LightBlue')
fullname_label.place(x=165, y=10)
# fullname_label.grid(row=0, column=0)
fullname_entry = Entry(window, width=20)
fullname_entry.place(x=250, y=10)
# fullname_entry.grid(row=0, column=1)

# Email
email_label = Label(window, text="Email:", bg='LightBlue')
email_label.place(x=165, y=45)
# email_label.grid(row=1, column=0)
email_entry = Entry(window, width=20)
email_entry.place(x=250, y=45)
# email_entry.grid(row=1, column=1)

# DOB: Date of birth
dob_label = Label(window, text="DOB:", bg='LightBlue')
dob_label.place(x=165, y=80)
# dob_label.grid(row=2, column=0)
dob_entry = DateEntry(window)
dob_entry.place(x=250, y=80)
# dob_label.grid(row=2, column=1)

# Gender
gender = StringVar()
GENDER_TYPES = {'male': 'Male', 'femail': 'Female'}
gender_label = Label(window, text="Gender:", bg='LightBlue')
gender_label.place(x=165, y=115)
gender_entry = Entry(window, width=20)
gender_entry.place(x=250, y=115)
male_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("male"), value="male", variable=gender
)
male_radio_btn.place(x=600, y=125)
female_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("female"), value="female", variable=gender
)
female_radio_btn.place(x=750, y=125)

# Phone
phone_label = Label(window, text="Phone:", bg='LightBlue')
phone_label.place(x=165, y=150)
phone_entry = Entry(window, width=20)
phone_entry.place(x=250, y=150)

# Course
course_label = Label(window, text="Course:", bg='LightBlue')
course_label.place(x=165, y=185)
course_entry = Entry(window, width=20)
course_entry.place(x=250, y=185)

# Save button
save_btn = Button(window, text="Save",  command=save)
save_btn.place(x=190, y=225)

# Add button
# add_btn = Button(window, text="Add", command=add)
# add_btn.place(x=240, y=225)

# Clear button
clear_btn = Button(window, text="Clear", command=clear)
clear_btn.place(x=245, y=225)

# Exit button
clear_btn = Button(window, text="Exit", bg='Red', command=window.quit)
clear_btn.place(x=300, y=225)


window.mainloop()
