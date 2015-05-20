#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
from tkFileDialog import askopenfilename
import tkFileDialog
import tomograph
def get_picture_info():
  return """Tutaj info"""
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
global photo_path
photo_path='data/image.jpg'
global sin_path
sin_path='data/blank.jpg'
#INPUT             
def insert_input():
    print "I-M-pressed"
    ftypes = [('JPG files', '*.jpg'), ('PNG files', '*.png'), ('All files', '*')]
    dlg = tkFileDialog.Open(root, filetypes = ftypes)
    global photo_path
    photo_path = dlg.show()
    if photo_path != '':
            print "ok"  
            print photo_path
            global image
            image = Image.open(photo_path)
            image.thumbnail(size, Image.ANTIALIAS)
            #img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            global data
            data = ImageTk.PhotoImage(image)
            explanation=photo_path
            global photo_info
            photo_info.destroy()
            photo_info = Label(input_frame, 
                               justify=LEFT,
                               padx = 10, 
                               fg='green',
                               text='świeżo wczytany obraz')
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
image = Image.open(photo_path)
insert_btn = Button(input_frame, 
              text="Wczytaj", 
              padx=60, 
              command = insert_input,
              justify=LEFT).grid(row=2, column=0)

image.thumbnail(size, Image.ANTIALIAS)
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
data = ImageTk.PhotoImage(image)
global photo_display
photo_display = Label(input_frame, image=data)
photo_display.grid(row=0, column=0)
photo_display.image=data


  
label_info=get_picture_info()
#explanation = get_picture_info()
photo_info = Label(input_frame, 
           justify=LEFT,
           padx = 10, 
           fg='green',
           text=label_info)
photo_info.grid(row=1, column=0)
      
#SINOGRAM   
global sin_image
sin_image = Image.open(sin_path)
sin_image.thumbnail(size, Image.ANTIALIAS)
#global sin_data
sin_data = ImageTk.PhotoImage(sin_image)
global sin_display
sin_display = Label(sin_frame, image=sin_data)
sin_display.grid(row=0, column=0)
sin_display.image=sin_data
explanation = """Rowerogram"""
global sin_info
label_info=get_picture_info()
sin_info = Label(sin_frame, 
              justify=LEFT,
              padx = 10, 
              fg='red',
              text=explanation).grid(row=1, column=0)

def get_sin_image():
  print 'get_image_to_sine'
  print 'wczytaj obraz i generate_sin'
  
  
def save_sin_image():
  print 'save_sine_image'

insert_sin_btn = Button(sin_frame,
    text="Wczytaj",
    command=get_sin_image,
    padx=60).grid(row=2, column=0)

save_sin_btn = Button(sin_frame,
    text="Zapisz",
    command=save_sin_image,
    padx=60).grid(row=3, column=0) 


#FILTER
def generate_sin():
   print "Alfa = " + str(alpha.get()) + "  Beta = " +  str(beta.get()) + "  Emiter = " + str(emiter.get())
   print "  Detector = " + str(detector.get()) + "  Filtr " + str(filter_value.get())
   global sin_image  
   arr=tomograph.generate(photo_path, emiter.get(), detector.get(), alpha.get(), beta.get())
   #sin_image = Image.open(photo_path)
   print arr.shape
   global sin_data
   #arr=np.zeros((100,100),dtype=np.uint8)
   sin_image=Image.fromarray(arr)
   #sin_image.thumbnail(size, Image.ANTIALIAS)
   sin_image.resize((400, 300),Image.ANTIALIAS)
   #sin_image = Image.open(photo_path)
   sin_data = ImageTk.PhotoImage(sin_image)
   global sin_display
   sin_display.destroy()
   sin_display = Label(sin_frame, image=sin_data)
   sin_display.configure(image = sin_data)
   sin_display.image=sin_data
   sin_display.grid(row=0, column=0)
   explanation = """Sinogramik"""
   global sin_info
   sin_info = Label(sin_frame, 
                 justify=LEFT,
                 padx = 10, 
                 fg='red',
                 text=explanation)
   sin_info.grid(row=1, column=0)
   print photo_path
   
filter_value = IntVar()
filter_chck = Checkbutton(params_frame, 
                text='filtr Hoffmanna', 
                variable = filter_value,
                justify=LEFT,
                padx=20).grid(row=0, column=0, sticky=E, columnspan=2)

alpha = IntVar()
slider = Scale(params_frame,
    from_=1, 
    to=180, 
    resolution=1,
    variable=alpha,
    orient=HORIZONTAL)
slider.set(5)
slider.grid(row=1, column=1)
  
alpha_lbl = Label(params_frame, 
           justify=LEFT,
           padx = 10, 
           text='kąt alfa').grid(row=1, column=0) 

beta = IntVar()
beta_slider = Scale(params_frame,
    from_=1, 
    to=180, 
    resolution=1,
    variable=beta,
    orient=HORIZONTAL)
beta_slider.set(50)
beta_slider.grid(row=2, column=1)
  
beta_lbl = Label(params_frame, 
           justify=LEFT,
           padx = 10, 
           text='kąt beta').grid(row=2, column=0) 
           
detector = IntVar()
detector_slider = Scale(params_frame,
    from_=1, 
    to=180, 
    resolution=1,
    variable=detector,
    orient=HORIZONTAL)
detector_slider.set(10)
detector_slider.grid(row=3, column=1)
  
detector_lbl = Label(params_frame, 
           justify=LEFT,
           padx = 10, 
           text='szerokość detektora').grid(row=3, column=0) 
           
emiter = IntVar()
emiter_slider = Scale(params_frame,
    from_=1, 
    to=180, 
    resolution=1,
    variable=emiter,
    orient=HORIZONTAL)
emiter_slider.set(20)
emiter_slider.grid(row=4, column=1)
  
emiter_lbl = Label(params_frame, 
           justify=LEFT,
           padx = 10, 
           text='odległość emitera').grid(row=4, column=0) 
           
run = Button(params_frame,
    text="Generuj",
    command=generate_sin,
    padx=60).grid(row=6, column=0,columnspan=2)
     

#OUTPUT
out_image = Image.open('data/blank.jpg')
out_image.thumbnail(size, Image.ANTIALIAS)
out_data = ImageTk.PhotoImage(out_image)
output_display = Label(output_frame, image=out_data)
output_display.grid(row=0, column=0)
output_display.image=data
explanation = """Zrekonstruowany obraz"""
output_info = Label(output_frame, 
              justify=LEFT,
              padx = 10, 
              fg='green',
              text=explanation).grid(row=1, column=0)

def save_output():
    print 'save output image'
    #tomograph.test()
        
save_btn = Button(output_frame, 
              text="Zapisz", 
              padx=60, 
              command=save_output, 
              height=3, 
              width=7,
              justify=LEFT).grid(row=2, column=0)

#input_frame.pack()
#params_frame.pack()
#output_frame.pack()
root.mainloop()
