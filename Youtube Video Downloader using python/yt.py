from tkinter import *
from pytube import YouTube
from tkinter import messagebox
root=Tk()
root.geometry("400x300+570+200")
root.resizable(False,False)
root.config(bg="#000000")
root.title("YOUTUBE DOWNLOADER")
def link():
        try:
                ytlink=entry.get()
                process=YouTube(ytlink)
                stream=process.streams.get_highest_resolution()
                stream.download()
                messagebox.showinfo("Yt Video Downloader","VIDEO SUCCESSFULLY DOWNLOADED")
        except:
                messagebox.showerror("Yt Video Downloader","PASTE A VALID LINK")

label1=Label(root,text="ENTER THE LINK BELOW",font="arial",background="black",foreground="white",width=23)
label1.place(x=85,y=60)
button1=Button(root,text="DOWNLOAD",fg="white",bg="black",font="arial",command=link)
button1.place(x=130,y=150)
button2=Button(root,text="EXIT",fg="white",bg="black",highlightbackground="black",activebackground="black",activeforeground="white",font="roboto",command=root.quit)
button2.place(x=162,y=200)
entry=Entry(root,width=50)
entry.place(x=60,y=100)
root.mainloop()