from tkinter import *
import pytube

window = Tk()
window.title('YouTube download')
window.geometry('600x200')
window['bg'] = 'LightBlue'


def downloader():
    url = pytube.YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    label = Label(window, text='Downloaded', font=('Comic Sans MS', 15))
    label.place(x=250, y=100)


label = Label(window, text='Downloader', font=('Comic Sans MS', 20), bg='LightBlue')
label.pack()

link = StringVar()
label = Label(window,
              text='Write youtube link: ',
              font=('comic Sans MS', 15),
              bg='LightBlue'
              )
label.place(x=20, y=60)

entery = Entry(window, width=35, font=('Comic Sans MS', 12))
entery.place(x=225, y=65)


btn = Button(window,
             text='Download video',
             font=('Comic Sans MS', 15),
             bg='Lime',
             width=30,
             command=downloader
             )
btn.place(x=100, y=120)

window.mainloop()



