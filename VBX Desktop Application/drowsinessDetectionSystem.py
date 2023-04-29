from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root=Tk()
root.title("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇")
root.geometry("500x500+530+100")
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


#DROWSINESS TITLE
drowsinessTitle=Label(text="𝙳𝚁𝙾𝚆𝚂𝙸𝙽𝙴𝚂𝚂 𝙳𝙴𝚃𝙴𝙲𝚃𝙸𝙾𝙽 𝚂𝚈𝚂𝚃𝙴𝙼",bg="black",fg="#cccccc",font="BOLD").place(x=90,y=15)
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoLabel = Label(image=logo)
logoLabel.place(x=160,y=185)

#IMAGE LABEL(DROWSY)




#DESCRIPTION
drowsyDescription=Label(text="""DETECTOR USED TO PREVENT FROM ACCIDENT
AND INCREASE THE POSSIBILITY OF LIVING""",bg="black",fg="#cccccc",font="BOLD").place(x=15,y=60)
priceLabel=Label(text="PRICE : RS.6000",bg="black",fg="#cccccc",font="BOLD").place(x=160,y=130)
#BUTTONS
back=Button(text="𝙱𝙰𝙲𝙺",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=back).place(x=100,y=400)
order=Button(text="𝙾𝚁𝙳𝙴𝚁",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=order).place(x=310,y=400)



root.mainloop()