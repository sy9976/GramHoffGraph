#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk

root = Tk() #initialize Tkinter
root.title("GramHoffGraph")
size = 400, 400
input_frame = LabelFrame(root, text='input data')
input_frame.grid(row=0,column=0)
params_frame = LabelFrame(root,
                 
                text='parameters')
params_frame.grid(row=0,column=1)
output_frame = LabelFrame(root, text='output data')
output_frame.grid(row=0,column=2)

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
    print spinval

insert_btn = Button(input_frame, 
              text="Wczytaj", 
              padx=60, 
              command=insert, 
              justify=LEFT).grid(row=2, column=0)

#FILTER
def get_params():
   print "Alfa = " + str(alpha.get()) + "  Beta = " +  str(beta.get()) + "  Filtr " + str(filter_value.get())

filter_value = IntVar()
filter_chck = Checkbutton(params_frame, 
                text='filtr Hoffmanna', 
                variable = filter_value,
                justify=LEFT,
                padx=20).grid(row=0, column=0, sticky=E, columnspan=2)

alpha = DoubleVar()
slider = Scale(params_frame,
    from_=1, 
    to=180, 
    resolution=0.1,
    variable=alpha,
    orient=HORIZONTAL)
slider.set(20)
slider.grid(row=1, column=1)
  
alpha_lbl = Label(params_frame, 
           justify=LEFT,
           padx = 10, 
           text='kąt alfa').grid(row=1, column=0) 

beta = DoubleVar()
beta_slider = Scale(params_frame,
    from_=1, 
    to=180, 
    resolution=0.1,
    variable=beta,
    orient=HORIZONTAL)
beta_slider.set(20)
beta_slider.grid(row=2, column=1)
  
beta_lbl = Label(params_frame, 
           justify=LEFT,
           padx = 10, 
           text='kąt beta').grid(row=2, column=0) 
           
run = Button(params_frame,
    text="Generuj",
    command=get_params,
    padx=60).grid(row=4, column=0,columnspan=2)
     

#OUTPUT
output_display = Label(output_frame, image=data).grid(row=0, column=0)
explanation = """Just some picture info"""
output_info = Label(output_frame, 
              justify=LEFT,
              padx = 10, 
              fg='green',
              text=explanation).grid(row=1, column=0)
save_btn = Button(output_frame, 
              text="Zapisz", 
              padx=60, 
              command=insert, 
              justify=LEFT).grid(row=2, column=0)

#input_frame.pack()
#params_frame.pack()
#output_frame.pack()
root.mainloop()
