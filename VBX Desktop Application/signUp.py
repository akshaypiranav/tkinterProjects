from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
def signupPage():
    root=Tk()
    root.title("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇")
    root.geometry("600x600+470+100")
    #root.state("zoomed")
    root.resizable(False,False)
    root.config(bg="#000000")
    photo=PhotoImage(file='blackbox.png')
    root.iconphoto(False,photo)

    newusername=StringVar()
    newpassword=StringVar()
    confirmPassword=StringVar()


    #Login Functions

    def database():
        try:
            userNameValue = newusername.get()
            userPasswordValue = newpassword.get()
            con = sqlite3.connect('vbx.db')
            qry = "insert into userTable (userName,passWord) values (?,?);"
            con.execute(qry, (userNameValue, userPasswordValue))
            con.commit()
            messagebox.showinfo("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇", "𝚂𝙸𝙶𝙽 𝚄𝙿 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻")

        except:
            messagebox.showwarning("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇", "𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙽𝙴𝙴𝙳 𝚃𝙾 𝙱𝙴 𝚄𝙽𝙸𝚀𝚄𝙴")
    def login():
        messagebox.showinfo("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇","𝙳𝙸𝚁𝙴𝙲𝚃𝙴𝙳 𝚃𝙾 𝙻𝙾𝙶𝙸𝙽 𝙿𝙰𝙶𝙴")
        root.destroy()
        import index
        index

    #Signup Function
    def signup():
        userNameValue = newusername.get()
        userPasswordValue = newpassword.get()
        userConfirmValue = confirmPassword.get()
        if(userPasswordValue==userConfirmValue and len(userPasswordValue)!=0 and len(userNameValue) !=0):
            database()
        else:
            messagebox.showwarning("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇","𝙵𝙸𝙻𝙻 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙳𝙴𝚃𝙰𝙸𝙻𝚂")

        print(userNameValue,userPasswordValue,userConfirmValue)
    #INFORMATION
    titleLabel=Label(text="𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇",foreground="#ffffff",bg="#000000",font="bold")
    titleLabel.place(x=200,y=50)

    loginPage=Label(text="𝚂𝙸𝙶𝙽 𝚄𝙿 𝙿𝙰𝙶𝙴",foreground="#ffffff",bg="#000000",font="bold")
    loginPage.place(x=350,y=150)

    #LOGO
    logo = ImageTk.PhotoImage(Image.open("logo.png"))
    logoLabel = Label(image=logo)
    logoLabel.place(x=130,y=90)

    #USERNAME
    nameLabel=Label(text="𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴",foreground="#ffffff",bg="#000000",font="bold")
    nameLabel.place(x=130,y=300)
    nameEntry=Entry(textvariable=newusername,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
    nameEntry.place(x=270,y=300)

    #PASSWORD
    passwordLabel=Label(text="𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳",foreground="#ffffff",bg="#000000",font="bold")
    passwordLabel.place(x=130,y=350)
    passwordEntry= Entry(root,show="*",textvariable=newpassword,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
    passwordEntry.place(x=270,y=350)

    #PASSWORD
    confirmPasswordLabel=Label(text="𝙲𝙾𝙽𝙵𝙸𝚁𝙼",foreground="#ffffff",bg="#000000",font="bold")
    confirmPasswordLabel.place(x=130,y=400)
    confirmPasswordEntry= Entry(root,show="*",textvariable=confirmPassword,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
    confirmPasswordEntry.place(x=270,y=400)


    #BUTTON
    loginButton=Button(text="𝙻𝙾𝙶 𝙸𝙽",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=login)
    loginButton.place(x=200,y=460)

    signupButton=Button(text="𝚂𝙸𝙶𝙽 𝚄𝙿",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=signup)
    signupButton.place(x=340,y=460)


    root.mainloop()
signupPage()