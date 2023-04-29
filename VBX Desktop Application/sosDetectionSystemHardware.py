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

#FUNCTIONS
def back():
    root.destroy()
    import homePage
def order():
    root.destroy()
    import orderDetails

#ACCIDENT DETECTION SYSTEM TITLE
sosHardwareTitle=Label(text="𝚂𝙾𝚂 𝙴𝙼𝙴𝚁𝙶𝙴𝙽𝙲𝚈 𝙰𝙻𝙴𝚁𝚃 𝙷𝙰𝚁𝙳𝚆𝙰𝚁𝙴",bg="black",fg="#cccccc",font="BOLD").place(x=140,y=15)


logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoLabel = Label(image=logo)
logoLabel.place(x=210,y=190)


#DESCRIPTION
sosHardwareDescription=Label(text="""SOS HARDWARE MEANS A PANIC BUTTON PLACED IN CAR
IF YOU PRESSED THAT IT SENDS MESSAGE TO THE 100""",bg="black",fg="#cccccc",font="BOLD").place(x=15,y=70)



#BUTTONS
back=Button(text="𝙱𝙰𝙲𝙺",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=back).place(x=130,y=450)

buyNow=Button(text="𝙱𝚄𝚈 𝙽𝙾𝚆",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=order).place(x=370,y=450)



root.mainloop()