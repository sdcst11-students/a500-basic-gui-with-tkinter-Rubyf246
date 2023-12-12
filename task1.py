#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

'''
##### Task 1
Create the user interface described in the image task1.png.
You should use only the .pack() or .grid() methods
(2 points) 

'''

window = tk.Tk()
window.title("tk!")
window.geometry("420x25")
window.resizable(False,False)

button1 = tk.Button(window,text="x")
button2 = tk.Button(window,text="=")
text1= tk.Entry(window, width=20 )
text2 = tk.Entry (window, width = 20)
text3 = tk.Entry(window, width = 20 )

text1.grid(row = 1, column = 1)
text2.grid(row= 1, column =3 )
text3.grid(row=1, column=5)
button1.grid(row = 1, column = 2)
button2.grid(row = 1, column = 4)





window.mainloop()
