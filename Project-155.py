from tkinter import *
import random

root=Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {"color" : ["deep pink","cyan","purple1","maroon1","lawn green","magenta2"]} 

def changebgcolor():
    random_number = random.randint(0,5)
    print(dictionary["color"][random_number])
    root.configure(background = dictionary["color"][random_number])
    
btn = Button(root, text = "Click me",command = changebgcolor)
btn.place(relx = 0.5,rely = 0.5,anchor = CENTER)

root.mainloop()