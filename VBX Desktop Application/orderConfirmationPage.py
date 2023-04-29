from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root=Tk()
root.title("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇")
root.geometry("600x600+470+100")
#root.state("zoomed")
root.resizable(False,False)
root.config(bg="#000000")
photo=PhotoImage(file='blackbox.png')
root.iconphoto(False,photo)


logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoLabel = Label(image=logo)
logoLabel.place(x=213,y=120)
titleLabel=Label(text="𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇",bg="black",fg="#cccccc",font="BOLD").place(x=190,y=40)
#LABELS
confirmedLabel=Label(text="𝙾𝚁𝙳𝙴𝚁 𝙲𝙾𝙽𝙵𝙸𝚁𝙼𝙴𝙳",bg="black",fg="#cccccc",font="BOLD").place(x=205,y=300)
soonLabel=Label(text="𝚆𝙴 𝚆𝙸𝙻𝙻 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝚈𝙾𝚄 𝚂𝙾𝙾𝙽 𝚃𝙷𝚁𝙾𝚄𝙶𝙷 𝙼𝙰𝙸𝙻",bg="black",fg="#cccccc",font="BOLD").place(x=90,y=350)
contactLabel=Label(text="𝙵𝙾𝚁 𝙵𝚄𝚁𝚃𝙷𝙴𝚁 𝙴𝙽𝚀𝚄𝚁𝙸𝙴𝚂 : 𝚊𝚔𝚜𝚑𝚊𝚢𝚙𝚒𝚛𝚊𝚗𝚊𝚟𝚋@𝚐𝚖𝚊𝚒𝚕.𝚌𝚘𝚖",bg="black",fg="#cccccc",font="BOLD").place(x=30,y=380)



root.mainloop()
