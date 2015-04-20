#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk

root = Tk() #initialize Tkinter
root.title("GramHoffGraph")
size = 400, 400
input_frame = LabelFrame(root, text='input data')
input_frame.grid(row=0,column=0)
params_frame = LabelFrame(root, text='parameters')
params_frame.grid(row=0,column=5)
output_frame = LabelFrame(root, text='output data')
output_frame.grid(row=0,column=10)

#INPUT
image = Image.open('data/image.jpg')
image.thumbnail(size, Image.ANTIALIAS)
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
data = ImageTk.PhotoImage(image)
photo_display = Label(input_frame, image=data).grid(row=0, column=0)
explanation = """Just some picture info"""
photo_info = Label(input_frame, 
           justify=LEFT,
           padx = 10, 
           fg='green',
           text=explanation).grid(row=1, column=0)

def insert():
    print "click insert!"

insert_btn = Button(input_frame, 
              text="Wczytaj", 
              padx=60, 
              command=insert, 
              justify=LEFT).grid(row=2, column=0)

#FILTER
filter_chck = Checkbutton(params_frame, 
                text='filtr', 
                padx=20).grid(row=0, column=1)
#filter_chck.pack()

#OUTPUT

#input_frame.pack()
#params_frame.pack()
#output_frame.pack()
root.mainloop()
