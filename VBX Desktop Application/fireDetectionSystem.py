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

#FIRE DETECTION SYSTEM TITLE
fireTitle=Label(text="𝙵𝙸𝚁𝙴 𝙳𝙴𝚃𝙴𝙲𝚃𝙸𝙾𝙽 𝚂𝚈𝚂𝚃𝙴𝙼",bg="black",fg="#cccccc",font="BOLD").place(x=173,y=15)


#IMAGE LABEL(DROWSY)


#DESCRIPTION
fireAccidentDescription=Label(text="""AN ACTIVE FLAME SENSOR TRIES TO FIND FIRE IN MOTION
AND ALSO DURING IN NOT MOTION IF HELDS IT ALERTS""",bg="black",fg="#cccccc",font="BOLD").place(x=12,y=70)

logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoLabel = Label(image=logo)
logoLabel.place(x=230,y=220)

#PRICE LABEL
priceLabel=Label(text="𝙿𝚁𝙸𝙲𝙴 : 𝚁𝚂.4𝟬𝟬",bg="black",fg="#cccccc",font="BOLD").place(x=230,y=170)
#BUTTONS
back=Button(text="𝙱𝙰𝙲𝙺",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=back).place(x=150,y=450)

buyNow=Button(text="𝙱𝚄𝚈 𝙽𝙾𝚆",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=order).place(x=400,y=450)

root.mainloop()