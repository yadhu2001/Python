import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 


from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("100x100")
def show():
   num = askinteger("Input", "Input an Integer")
   print(num)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()
