import tkinter as tk
from tkinter import *
import random
import time

def main():
    program = GraphMaker

    program.window.mainloop()

class GraphMaker(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack( side = TOP )
        self.master.title("Window")
        self.button1 = Button(self,)
        self.quit_button = Button(self, text="Quit" )
        self.quit_button.grid(row=2, column=0)
        self.quit_button['command'] = self.close_window
        self.place(bordermode=OUTSIDE, height=100, width=100)

    def close_window(self):
        self.destroy()


def main():
    GraphMaker().mainloop()
if __name__ == '__main__':
    main()