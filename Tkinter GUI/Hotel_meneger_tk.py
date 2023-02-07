from tkinter import *
import csv
import os
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar
from tkcalendar import DateEntry
from Hotel_meneger import HotelGuests
from datetime import datetime

root = Tk()
root.title('Hotel Meneger')
root.geometry('450x450')
root.resizable(width=False, height=False)
root['bg'] = 'LightBlue'

person_info = []


def csv_file():
    with open('HTL.csv') as file:
        csv_reader = csv.DictReader(file)
        result = [row for row in csv_reader]
        messagebox.showinfo('All Information', f'{result}')


def get_price():
    price_one_day = 300
    price = date_entery.get()
    result = int(price) * price_one_day
    messagebox.showinfo('Price', f'{result}$')


def add():
    guests = HotelGuests(
        fullname_entery.get(),
        age_entery.get(),
        place_entery.get(),
        date_entery.get(),
        datetime.now()
    )
    person_info.append(guests.get_attrs(as_dict=True))
    messagebox.showinfo('Information', 'The data has been added successfully')


def save():
    with open('HTL.csv', 'a', newline='\n') as file:
        header = ['Fullname', 'Day of birthday', 'Place', 'Date of stay', 'DOJ']
        save_writer = csv.DictWriter(file, header)
        if os.path.getsize('HTL.csv') == 0:
            save_writer.writeheader()

        save_writer.writerows(person_info)
        messagebox.showinfo('Information', 'Save successfully')


def clear():
    fullname_entery.delete(0, END)
    age_entery.delete(0, END)
    place_entery.delete(0, END)
    date_entery.delete(0, END)


label = Label(root,
              text='Hotel Meneger Welcome',
              font=('Comic Sans MS', 20, 'bold'),
              bg='LightBlue'
              )
label.pack()
# Fullname
fullname_label = Label(root, text='Full name: ', width='10', font=('Comic Sans MS', 15, 'bold'), bg='LightBlue')
fullname_label.place(x=20, y=60)
fullname_entery = Entry(root, width=40)
fullname_entery.place(x=130, y=70)

# Age
age_label = Label(root, text='Enter your age: ', width='17', font=('Comic Sans MS', 15, 'bold'), bg='LightBlue')
age_label.place(x=5, y=100)
age_entery = Entry(root, width=32)
age_entery.place(x=185, y=110)

# Place
place_label = Label(root, text='Your country: ', width='12', font=('Comic Sans MS', 15, 'bold'), bg='LightBlue')
place_label.place(x=25, y=140)
place_entery = Entry(root, width=35)
place_entery.place(x=165, y=150)

# Date of stay
date_label = Label(root, text='How many days stay: ', width='20', font=('Comic Sans MS', 15, 'bold'), bg='LightBlue')
date_label.place(x=15, y=175)
date_entery = Entry(root, width=24)
date_entery.place(x=240, y=185)

# Save
save_btn = Button(root, text='SAVE', width='10', height='2', activebackground='Lime', command=save)
save_btn.place(x=70, y=230)

# Add
add_btn = Button(root, text='ADD', width='10', height='2', activebackground='Lime', command=add)
add_btn.place(x=170, y=230)

# Clear
clear_btn = Button(root, text='CLEAR', width='10', height='2', activebackground='Lime', command=clear)
clear_btn.place(x=270, y=230)

# All information
info_btn = Button(root, text='ALL INFORMATION', width='25', height='2', activebackground='Lime', command=csv_file)
info_btn.place(x=20, y=300)

# Total price
price_btn = Button(root, text='TOTAL PRICE', width='25', height='2', activebackground='Lime', command=get_price)
price_btn.place(x=235, y=300)

# Exit
exit_btn = Button(root, text='EXIT', width='10', height='2', bg='Red', fg='Black', activebackground='Lime', command=root.quit)
exit_btn.place(x=350, y=380)


root.mainloop()

