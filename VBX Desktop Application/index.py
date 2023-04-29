from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3



root=Tk()
root.title("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇")
root.geometry("600x600+470+100")
#root.state("zoomed")
root.resizable(False,False)
root.config(bg="#000000")
photo=PhotoImage(file='blackbox.png')
root.iconphoto(False,photo)

username=StringVar()
password=StringVar()


#Login Functions

def checkDatabase():
    checkUserName=username.get()
    checkPassword=password.get()
    con = sqlite3.connect("vbx.db")
    cur = con.cursor()
    statement = f"SELECT userName from userTable WHERE username='{checkUserName}' AND Password = '{checkPassword}';"
    cur.execute(statement)
    if not cur.fetchone():
        messagebox.showwarning("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇", "𝙼𝙰𝚃𝙲𝙷 𝙽𝙾𝚃 𝙵𝙾𝚄𝙽𝙳")
    else:
        messagebox.showwarning("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇", "𝙻𝙾𝙶 𝙸𝙽 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻")
        root.destroy()
        import homePage






def login():
    checkUserName=username.get()
    checkPassword=password.get()
    if(len(checkUserName)!=0 and len(checkPassword)!=0):
        checkDatabase()
    else:
        messagebox.showwarning("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇", "𝙵𝙸𝙴𝙻𝙳 𝙽𝙾𝚃 𝙱𝙴 𝙴𝙼𝙿𝚃𝚈")
#Signup Function
def signup():
    messagebox.showinfo("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇","𝙳𝙸𝚁𝙴𝙲𝚃𝙴𝙳 𝚃𝙾 𝚂𝙸𝙶𝙽 𝚄𝙿 𝙿𝙰𝙶𝙴")
    root.destroy()
    import signUp
    signUp




#INFORMATION
titleLabel=Label(text="𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇",foreground="#ffffff",bg="#000000",font="bold")
titleLabel.place(x=200,y=50)

loginPage=Label(text="𝙻𝙾𝙶𝙸𝙽 𝙿𝙰𝙶𝙴",foreground="#ffffff",bg="#000000",font="bold")
loginPage.place(x=350,y=150)

#LOGO
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoLabel = Label(image=logo)
logoLabel.place(x=130,y=90)

#USERNAME
nameLabel=Label(text="𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴",foreground="#ffffff",bg="#000000",font="bold")
nameLabel.place(x=130,y=300)
nameEntry=Entry(textvariable=username,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
nameEntry.place(x=270,y=300)

#PASSWORD
passwordLabel=Label(text="𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳",foreground="#ffffff",bg="#000000",font="bold")
passwordLabel.place(x=130,y=350)
passwordEntry= Entry(root,show="*",textvariable=password,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
passwordEntry.place(x=270,y=350)

#BUTTON
loginButton=Button(text="𝙻𝙾𝙶 𝙸𝙽",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=login)
loginButton.place(x=200,y=420)

signupButton=Button(text="𝚂𝙸𝙶𝙽 𝚄𝙿",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=signup)
signupButton.place(x=340,y=420)


root.mainloop()