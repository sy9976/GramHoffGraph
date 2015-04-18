#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
# if you are working under Python 3, comment the previous line and comment out the following line
#from tkinter import *

root = Tk() #initialize Tkinter
root.title("GramHoffGraph")
size = 400, 400
#w = Label(root, text="Hello Tkinter!")
#w.pack() #tells Tk to fit the size of the window to the given text


image = Image.open('data/image.jpg')
image.thumbnail(size, Image.ANTIALIAS)
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
logo = ImageTk.PhotoImage(image)
#logo = PhotoImage(file='data/image.jpg')
w1 = Label(root, image=logo).pack(side="right")
explanation = """Zdjęcie rentegowskie 
zgrabnej nogi Szymona Gramzy, 
który uległ kontuzji 
z winy architektury byłej szkoły."""
w2 = Label(root, 
           justify=LEFT,
           padx = 10, 
           fg='green',
           text=explanation).pack(side="left")
def callback():
    print "click!"

b = Button(root, text="OK", pady=60, command=callback)
b.pack()
#b.pack()
l =Label(root, text="Starting...")
#l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))

c = Checkbutton(root, text='testing', padx=20)
l.pack()
c.pack()
root.mainloop()
