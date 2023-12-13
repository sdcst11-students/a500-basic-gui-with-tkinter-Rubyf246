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
dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto)
bluetext = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg="#aaffff", )
pochacco = tk.Label(window, text= "Pochacco!" )
dog.grid(row = 1, column = 3)
bluetext.grid(row =2, column =1, columnspan=5)
pochacco.grid(row= 1, column = 4)



window.mainloop()
