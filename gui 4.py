from tkinter import *

def MyButtonClicked(event):
  print("The MyButtonClicked function was called.")

window=Tk()
btn = Button(window, text='OK')
btn.bind('<Return>', MyButtonClicked)

window.mainloop()