from tkinter import *
from PIL import Image,ImageTk
import os

counter = 1
def handle_next():
    global counter

    image_label.config(image = image_array[counter])
    counter += 1
    if counter == len(image_array):
        counter = 0

def handle_previous():
    global counter
    if counter == 0:
        counter = len(image_array) - 1
        image_label.config(image =image_array[counter]) 
    else:
        counter -= 1
        image_label.config(image =image_array[counter])
        
def handle_slideshow():
    handle_next()
    if counter == 0:
        stop_slideshow()
    else:
        window.after(1500,handle_slideshow)

def stop_slideshow():
    image_label.config(image =image_array[len(image_array)-1])
    

window = Tk()

window.title('Wallpaper Viewer - Made by @Imransh1 Github')
window.configure(background= '#66DDAA')
window.geometry('800x960')


files = os.listdir('Wallpapers')
image_array = []

for i in files:
    img = Image.open(os.path.join('Wallpapers', i))
    resize_img = img.resize((780, 780))
    image_array.append((ImageTk.PhotoImage(resize_img)))

image_label = Label(window, image = image_array[0])
image_label.pack(pady = (15,0))

prev_btn = Button(window,text= 'Previous',width = 20 ,command = handle_previous,fg = 'White', bg = '#FA9A00')
prev_btn.configure(font = ('verdana',10))
prev_btn.pack(pady = (30, 0))

slideshow_btn = Button(window,text='Slideshow',width = 20,command = handle_slideshow,fg = 'white', bg = '#FA9A00')
slideshow_btn.configure(font = ('verdana',10))
slideshow_btn.pack(padx = 8, pady= 8)

next_button = Button(window,text='Next',width = 20,command = handle_next,fg = 'white', bg = '#FA9A00')
next_button.configure(font = ('verdana',10))
next_button.pack()



window.mainloop()
