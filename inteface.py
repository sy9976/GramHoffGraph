#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
from tkFileDialog import askopenfilename
import tkFileDialog

root = Tk() #initialize Tkinter
root.title("GramHoffGraph")
size = 400, 400
input_frame = LabelFrame(root, text='input data')
input_frame.grid(row=0,column=0)
params_frame = LabelFrame(root, 
                text='parameters')
params_frame.grid(row=0,column=1)
sin_frame = LabelFrame(root, 
                text='sinogram')
sin_frame.grid(row=0,column=2)
output_frame = LabelFrame(root, text='output data')
output_frame.grid(row=0,column=3)

#INPUT


def insertt(image):
    filename = askopenfilename(parent=root)
    if filename:
      image = Image.open(filename)

def insert(image):
        ftypes = [('JPG files', '*.jpg'), ('PNG files', '*.png'), ('All files', '*')]
        dlg = tkFileDialog.Open(root, filetypes = ftypes)
        fl = dlg.show()  
        if fl != '':
            print "ok"  
            print fl
            image = Image.open(fl)  
        
            
def act(): # defines an event function - for click of button
    print "I-M-pressed"
    ftypes = [('JPG files', '*.jpg'), ('PNG files', '*.png'), ('All files', '*')]
    dlg = tkFileDialog.Open(root, filetypes = ftypes)
    fl = dlg.show()
    if fl != '':
            print "ok"  
            print fl
            global image
            image = Image.open(fl)
            image.thumbnail(size, Image.ANTIALIAS)
            #img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            global data
            data = ImageTk.PhotoImage(image)
            explanation=fl
            photo_info = Label(input_frame, 
                               justify=LEFT,
                               padx = 10, 
                               fg='green',
                               text=fl)
            photo_info.grid(row=1, column=0)
            global photo_display
            photo_display.destroy()
            photo_display = Label(input_frame, image=data)
            photo_display.configure(image = data)
            photo_display.image=data
            photo_display.grid(row=0, column=0)
            #photo_display.update()
            #root.update()
global image           
image = Image.open('data/image.jpg')
insert_btn = Button(input_frame, 
              text="Wczytaj", 
              padx=60, 
              #command=insert, 
              #command=insert(image),
              command = act,
              justify=LEFT).grid(row=2, column=0)


#image = Image.open('/home/chygra/Dropbox/semVI_Szymon/IwM lab/GramHoffGraph/data/kwadraty.png')

image.thumbnail(size, Image.ANTIALIAS)
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
data = ImageTk.PhotoImage(image)
global photo_display
photo_display = Label(input_frame, image=data)
photo_display.grid(row=0, column=0)
photo_display.image=data

explanation = """Obraz z którego powstanie sinogram"""
photo_info = Label(input_frame, 
           justify=LEFT,
           padx = 10, 
           fg='green',
           text=explanation).grid(row=1, column=0)
      
#SINOGRAM      
#w,h = 256,256
#np.random.randint(5, size=(2, 4))
#sin_matrix = np.zeros( (w,h,3), dtype=np.uint8)
#sin_matrix[253,250] = [255,0,0]
#matrix = Image.fromarray(sin_matrix, 'RGB')        
#matrix = np.zeros((200,200, 3), np.uint8)
#matrix = np.random.random((200,200))
sin_image = Image.open('data/blank.jpg')
sin_data = ImageTk.PhotoImage(sin_image)
sin_display = Label(sin_frame, image=sin_data).grid(row=0, column=0)
explanation = """Sinogram"""
output_info = Label(sin_frame, 
              justify=LEFT,
              padx = 10, 
              fg='red',
              text=explanation).grid(row=1, column=0)

def get_image():
  print 'get_image_to_sine'
  
def save_image():
  print 'save_sine_image'

insert_sin_btn = Button(sin_frame,
    text="Wczytaj",
    command=get_image,
    padx=60).grid(row=2, column=0)

save_sin_btn = Button(sin_frame,
    text="Zapisz",
    command=save_image,
    padx=60).grid(row=3, column=0) 

             

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
out_image = Image.open('data/blank.jpg')
out_data = ImageTk.PhotoImage(out_image)
output_display = Label(output_frame, image=out_data)
output_display.grid(row=0, column=0)
#photo_display.grid(row=0, column=0)
output_display.image=data
explanation = """Zrekonstruowany obraz"""
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
