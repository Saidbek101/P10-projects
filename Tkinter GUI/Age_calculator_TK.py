from tkinter import *
from datetime import date

root = Tk()
root.title('Age Calculator')
root.geometry('500x200')
root.resizable(width=False, height=False)


def calcus_age():
    today = date.today()
    year = int(entery.get())
    if year <= 0 or year >= 2023:
        label['text'] = 'Error'
    else:
        result = today.year - year
        label['text'] = 'You ' + str(result) + ' years old'


label = Label(root,
              text='Age Calculator',
              font=('Comic Sans MS', 20, 'bold')
              )
label.pack()

label_1 = Label(root,
                text='Enter your age:',
                font=('Comic Sans MS', 20),
                )
label_1.place(x=30, y=45)
# label_1.pack()

entery = Entry(root, width=25, font=('Comic Sans MS', 12))
entery.place(x=235, y=60)

btn = Button(root,
             text='Your year',
             font=('Comic Sans MS', 12),
             bg='Red',
             activebackground='Lime',
             command=calcus_age
             )
btn.place(x=400, y=100)

root.mainloop()
