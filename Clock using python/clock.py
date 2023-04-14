#author @akshaypiranav-github
#author @akshaypiranav-instagram

from tkinter import Tk,Label
from time import strftime
root=Tk()
root.title("Digital clock")
root.resizable(False,False)
def time():
    timeSet=strftime("%H:%M:%S:%p")
    label.config(text=timeSet)
    label.after(1000,time)

label=Label(root,font=("arial",40),bg="black",fg="green")
label.pack()
time()
root.mainloop()
