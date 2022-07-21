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
    
root = Tk()

root.title('Wallpaper Viewer - Made by @Imransh1 Github')
root.configure(background= '#66DDAA')
root.geometry('800x960')


files = os.listdir('Wallpapers')
image_array = []

for i in files:
    img = Image.open(os.path.join('Wallpapers', i))
    resize_img = img.resize((780, 810))
    image_array.append((ImageTk.PhotoImage(resize_img)))

image_label = Label(root, image = image_array[0])
image_label.pack(pady = (15,0))

prev_btn = Button(root,text= 'Previous',width = 20 ,command = handle_previous,fg = 'White', bg = '#FA9A00')
prev_btn.configure(font = ('verdana',10))
prev_btn.pack(pady = (40, 0))

next_button = Button(root,text='Next',width = 20,command = handle_next,fg = 'white', bg = '#FA9A00')
next_button.configure(font = ('verdana',10))
next_button.pack()


root.mainloop()
