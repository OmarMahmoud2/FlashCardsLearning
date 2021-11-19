from tkinter import *
import pandas as pd
import random 
import json
from tkinter import messagebox

###########################################
try:
  data = pd.read_csv('words_to_learn.csv')
except:
  data = pd.read_csv('french_words.csv')



flst = data.to_dict('records')

rword = ''
fword = ''
eword = ''


def learn():
  try:
    flst.remove(rword)
  except ValueError:
    messagebox.showinfo(title='Well Done', message="You've finished all the \n Flash cards \n App will Reset to original state \n when Run again.")
    window.destroy()
  else:
    df = pd.DataFrame(flst)
    df.to_csv('words_to_learn.csv', index=False )

def flip():
  canvas.itemconfig(img, image= backimg)
  canvas.itemconfig(title, text='English', fill = 'white')
  canvas.itemconfig(word, text=eword, fill = 'white')
  
  
def next():
  global rword, fword, eword, flipper
  window.after_cancel(flipper)
  try:
    rword = random.choice(flst)
  except IndexError:
    canvas.itemconfig(title, text='Bravo')
    canvas.itemconfig(word, text="You've finished all the \n Flash cards", font=('ariel', 20, 'italic'))
  else:
    fword = rword['French']
    eword = rword['English']
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=fword, fill='black')
    canvas.itemconfig(img, image= frontimg)
    flipper = window.after(5000, flip)
   

def combfunc():
  next()
  learn() 
  
############################################
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('French Flash Cards')
window.minsize(500, 350)
window.config(padx=50, pady= 50, bg = BACKGROUND_COLOR)

canvas = Canvas(width=500, height =300, highlightthickness=0, bg= BACKGROUND_COLOR )
frontimg= PhotoImage(file='card_front-1.png')
backimg= PhotoImage(file='card_back.png')
img =canvas.create_image(250, 150, image= frontimg)
canvas.grid(column= 0, row=0, columnspan=2)

title = canvas.create_text(240, 80, text='French', fill='Black', font=('ariel', 25, 'italic'))
word = canvas.create_text(240, 180, text=fword, fill='black', font=('times new roman', 35, 'bold'))

right = PhotoImage(file='right.png')
wrong= PhotoImage(file='wrong.png')

rightbutt= Button(image=right, highlightthickness=0, command=combfunc)
rightbutt.grid(column=0, row=1)

wrongbutt= Button(image=wrong, highlightthickness=0,command= next)
wrongbutt.grid(column=1, row=1)
flipper = window.after(5000, flip)
next()

###########################################








window.mainloop()