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
        self.pack()
        self.master.title("Window")
        self.button1 = Button(self,)
        self.quit_button = Button(self, text="Quit" )
        self.quit_button.grid(row=2, column=0)
        self.quit_button['command'] = self.close_window

    def close_window(self):
        self.destroy()


def main():
    GraphMaker().mainloop()
if __name__ == '__main__':
    main()