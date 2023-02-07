from tkinter import *
from Translate_2 import to_latin
from Translate_2 import to_cyrillic

root = Tk()
root.title('Translater lt - kr')
root.geometry('400x200')
root.resizable(width=False, height=False)
root['bg'] = 'White'


def trans(a):
    a = str(a)
    if a.isascii():
        result = to_cyrillic(a)
    else:
        result = to_latin(a)
    label = Label(root, text=result)
    label.pack()


label = Label(root, text='Translate', font = ('Comic Sans MS', 20, 'italic'))
label.pack()

entery = Entry(root,width='50', bg='LightBlue')
entery.pack()

btn = Button(root, text= ' ♻️Translate♻️ ',  bg='Red', activebackground='Lime', command=lambda: trans(entery.get()))
btn.pack()

root.mainloop()


