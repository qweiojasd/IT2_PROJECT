import tkinter as tk

def process_event(event):
  print("The process_event function was called.")

application_window = tk()
my_button = tk.Button(application_window, text="Example")
my_button.bind("<Enter>", process_event)