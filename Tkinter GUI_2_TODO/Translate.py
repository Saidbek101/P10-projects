from tkinter import *
from googletrans import Translator


def trans():
    text = texts.get('1.0', END)
    translt = translator.translate(text, dest='en')
    texts_1.delete('1.0', END)
    texts_1.insert('1.0', translt.text)


root = Tk()
root.geometry('500x350')
root.title('Translator')
root.resizable(width=False, height=False)
root['bg'] = 'Black'
translator = Translator()

label = Label(root, fg='white', bg='Black', font='Arial 15 bold', text='Write sentences English')
label.place(relx=0.5, y=30, anchor=CENTER)
texts = Text(root, width=35, height=5, font='Arial 12 bold')
texts.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='Translator', command=trans)
btn.place(relx=0.5, y=180, anchor=CENTER)

texts_1 = Text(root, width=35, height=5, font='Arial 12 bold')
texts_1.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()
