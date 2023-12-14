#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

'''
##### Task 4
Create the user interface described in the image task3.png
using the .place() method
(3 points)

'''


window = tk.Tk()
window.title("Example")
window.geometry("260x135")
window.resizable(False,False)

dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto)
bluetext = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg="#aaffff", )
pochacco = tk.Label(window, text= "Pochacco!" )
dog.place(x=60, y=0)
bluetext.place( x= 0, y=100)
pochacco.place(x=140, y=40)


window.mainloop()
