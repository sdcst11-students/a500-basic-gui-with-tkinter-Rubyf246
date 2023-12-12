#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

'''
##### Task 3
Create the user interface described in the image task3.png
using the .grid() method
(3 points)
'''

window = tk.Tk()
window.title("Example")
window.geometry("350x150")
window.resizable(False,False)

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="A cuddly little puppy! This is from the same creators who brought you Keropi and Kero Kero", bg="#aaffff")

label1.grid(row = 1, column = 3)
label2.grid(row =1, column =1, rowspan=4)



window.mainloop()
