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
           text=explanation).pack(side="left")
root.mainloop()
