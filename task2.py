#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

'''
##### Task 2
Create the user interface described in the image task2.png.
This image was created using the .grid() method, but you can
use .pack() or .place() also
(5 points)

'''
window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto) 
cd= tk.Label(window, text = "Client Database")
name= tk.Label(window, text = "Name")
type= tk.Label (window, text= "Type")
breed= tk.Label(window, text= "Breed")
owner = tk.Label (window, text = "Owner")
bd= tk.Label (window, text= "Birthdate")

ne = tk.Entry (window, borderwidth= 2,width = 20)
te = tk.Entry (window,borderwidth= 2, width = 20)
be = tk.Entry (window,borderwidth= 2, width = 20)
oe = tk.Entry (window, borderwidth= 2, width = 20)
bde = tk.Entry (window, borderwidth= 2, width = 20)

sbn= tk.Button (window, text= "Search by Name")
sbne= tk.Entry (window, width = 20 )


dog.grid(row = 1, column = 1, rowspan = 3)
cd.grid(row = 2, column = 3 )
name.grid (row = 4, column = 1)
type. grid (row = 4, column = 2)
breed.grid(row= 4, column= 3)
owner.grid (row= 4, column = 4)
bd.grid (row =4, column = 5)

ne.grid (row= 5, column = 1)
te.grid (row= 5, column = 2)
be.grid (row= 5, column = 3)
oe.grid (row= 5, column = 4)
bde.grid (row=5, column = 5)

sbn.grid (row= 1, column=4)
sbne.grid(row=1, column = 5)


window.mainloop()
