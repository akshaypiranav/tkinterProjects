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




name=StringVar()
email=StringVar()
address=StringVar()
nearby=StringVar()
state=StringVar()


userName=name.get()
userEmail=email.get()
userAddress=address.get()
userNearby=nearby.get()
userState=state.get()


preferredTime=IntVar()
preferredTime1=IntVar()
preferredPlace1=IntVar()
preferredPlace2=IntVar()
preferredPlace3=IntVar()


drowsy=IntVar()
fire=IntVar()
accident=IntVar()
sosHard=IntVar()
sosSoft=IntVar()



orderedProducts=[]
prefferedSets=[]
#FUNCTIONS
def database(orderedThings,prefferedThings):
    try:
        userName = name.get()
        userEmail = email.get()
        userAddress = address.get()
        userNearby = nearby.get()
        userState = state.get()
        con = sqlite3.connect('vbx.db')
        qry = "insert into orderPage (name,email,address,landmark,state,orderedItems,prefferedItems) values (?,?,?,?,?,?,?);"

        con.execute(qry, (userName,userEmail,userAddress,userNearby,userState,orderedThings,prefferedThings))
        con.commit()
        messagebox.showinfo("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇","𝙾𝚁𝙳𝙴𝚁𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈")
        root.destroy()
        import orderConfirmationPage
    except:
        messagebox.showinfo("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇","𝙿𝚁𝙾𝙱𝙻𝙴𝙼 𝙾𝙲𝙲𝚄𝚁𝙴𝙳 𝙸𝙽 𝙾𝚁𝙳𝙴𝚁𝙸𝙽𝙶")

def back():
    root.destroy()
    import homePage


def drowsy1():
    orderedProducts.append("DROWSINESS DETECTION SYSTEM\n")


def fire1():
    orderedProducts.append("FIRE DETECTION SYSTEM\n")


def sosSoft1():
    orderedProducts.append("SOS EMERGENCY SYSTEM SOFTWARE\n")


def sosHard1():
    orderedProducts.append("SOS EMERGENCY SYSTEM HARDWARE\n")


def accident1():
    orderedProducts.append("ACCIDENT DETECTION SYSTEM\n")


def am():
    prefferedSets.append("AM\n")


def pm():
    prefferedSets.append("PM\n")


def door():
    prefferedSets.append("DOOR STEP\n")


def security():
    prefferedSets.append("SECURITY ROOM\n")


def mailbox():
    prefferedSets.append("MAIL BOX\n")



def order():
    userName = name.get()
    userEmail = email.get()
    userAddress = address.get()
    userNearby = nearby.get()
    userState = state.get()



    orderedThings=""
    for value in orderedProducts:
        orderedThings+=value
    prefferedThings=""
    for things in prefferedSets:
        prefferedThings+=things

    if (len(userName)!=0 and len(userEmail)!=0 and len(userAddress)!=0 and len(userNearby)!=0 and len(userState)!=0):
        database(orderedThings,prefferedThings)
    else:
        messagebox.showinfo("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇","𝙵𝙸𝙻𝙻 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙸𝙴𝙻𝙳𝚂")


#TITLE
titleLabel=Label(text="𝙵𝙸𝙻𝙻 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙳𝙴𝚃𝙰𝙸𝙻𝚂",foreground="#ffffff",bg="#000000",font="bold")
titleLabel.place(x=180,y=10)
#USERNAME
nameLabel=Label(text="𝙽𝙰𝙼𝙴",foreground="#ffffff",bg="#000000",font="bold")
nameLabel.place(x=30,y=60)
nameEntry=Entry(textvariable=name,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
nameEntry.place(x=270,y=60)

#PASSWORD
emailLabel=Label(text="𝙴-𝙼𝙰𝙸𝙻",foreground="#ffffff",bg="#000000",font="bold")
emailLabel.place(x=30,y=100)
emailEntry= Entry(root,textvariable=email,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
emailEntry.place(x=270,y=100)


addressLabel=Label(text="𝙰𝙳𝙳𝚁𝙴𝚂𝚂",foreground="#ffffff",bg="#000000",font="bold")
addressLabel.place(x=30,y=140)
addressEntry= Entry(root,textvariable=address,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
addressEntry.place(x=270,y=140)


nearbyLabel=Label(text="𝙻𝙰𝙽𝙳𝙼𝙰𝚁𝙺",foreground="#ffffff",bg="#000000",font="bold")
nearbyLabel.place(x=30,y=180)
nearbyEntry= Entry(root,textvariable=nearby,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
nearbyEntry.place(x=270,y=180)


stateLabel=Label(text="𝚂𝚃𝙰𝚃𝙴",foreground="#ffffff",bg="#000000",font="bold")
stateLabel.place(x=30,y=220)
stateEntry= Entry(root,textvariable=state,font=("arial",13,"bold"),width=23,bg="#cccccc",fg="#000000",border=0)
stateEntry.place(x=270,y=220)

timeLabel=Label(text="𝙿𝚁𝙴𝙵𝙵𝙴𝚁𝙴𝙳 𝚃𝙸𝙼𝙴  ",foreground="#ffffff",bg="#000000",font="bold")
timeLabel.place(x=30,y=260)

Checkbutton(root, text='𝙰𝙼', variable=preferredTime,onvalue=1,offvalue=0,bg="black",fg="#cccccc",font="BOLD",activebackground="#cccccc",command=am).place(x=270,y=260)
Checkbutton(root, text='𝙿𝙼', variable=preferredTime1,onvalue=1,offvalue=0,bg="black",fg="#cccccc",font="BOLD",activebackground="#cccccc",command=pm).place(x=370,y=260)

placeLabel=Label(text="𝙿𝚁𝙴𝙵𝙵𝙴𝚁𝙴𝙳 𝙿𝙻𝙰𝙲𝙴 ",foreground="#ffffff",bg="#000000",font="bold")
placeLabel.place(x=30,y=300)

Checkbutton(root, text='𝙳𝙾𝙾𝚁 𝚂𝚃𝙴𝙿', variable=preferredPlace1,onvalue=1,offvalue=0,bg="black",fg="#cccccc",font="BOLD",activebackground="#cccccc",command=door).place(x=270,y=300)
Checkbutton(root, text='𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈', variable=preferredPlace2,onvalue=1,offvalue=0,bg="black",fg="#cccccc",font="BOLD",activebackground="#cccccc",command=security).place(x=430,y=300)
Checkbutton(root, text='𝙼𝙰𝙸𝙻 𝙱𝙾𝚇', variable=preferredPlace3,onvalue=1,offvalue=0,bg="black",fg="#cccccc",font="BOLD",activebackground="#cccccc",command=mailbox).place(x=270,y=340)

selectProducts=Label(text="𝚂𝙴𝙻𝙴𝙲𝚃 𝙿𝚁𝙾𝙳𝚄𝙲𝚃𝚂",foreground="#ffffff",bg="#000000",font="bold")
selectProducts.place(x=30,y=380)

Checkbutton(root, text='𝙳𝚁𝙾𝚆𝚂𝚈', variable=drowsy,onvalue=1,offvalue=0,bg="black",fg="#cccccc",font="BOLD",activebackground="#cccccc",command=drowsy1).place(x=270,y=380)
Checkbutton(root, text='𝙵𝙸𝚁𝙴 𝙳𝙴𝚃𝙴𝙲𝚃𝙸𝙾𝙽', variable=fire,bg="black",onvalue=1,offvalue=0,fg="#cccccc",font="BOLD",activebackground="#cccccc",command=fire1).place(x=390,y=380)
Checkbutton(root, text='𝚂𝙾𝚂 𝙷𝙰𝚁𝙳𝚆𝙰𝚁𝙴', variable=sosHard,bg="black",onvalue=1,offvalue=0,fg="#cccccc",font="BOLD",activebackground="#cccccc",command=sosHard1).place(x=270,y=420)
Checkbutton(root, text='𝚂𝙾𝚂 𝚂𝙾𝙵𝚃𝚆𝙰𝚁𝙴', variable=sosSoft,bg="black",onvalue=1,offvalue=0,fg="#cccccc",font="BOLD",activebackground="#cccccc",command=sosSoft1).place(x=270,y=460)
Checkbutton(root, text='𝙰𝙲𝙲𝙸𝙳𝙴𝙽𝚃 𝙳𝙴𝚃𝙴𝙲𝚃𝙸𝙾𝙽', variable=accident,onvalue=1,offvalue=0,bg="black",fg="#cccccc",font="BOLD",activebackground="#cccccc",command=accident1).place(x=270,y=500)







#BUTTON
backButton=Button(text="𝙱𝙰𝙲𝙺",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=back)
backButton.place(x=170,y=555)

orderButton=Button(text="𝙾𝚁𝙳𝙴𝚁",font="bold",width=7,height=0,border=0,bg="#cccccc",fg="#000000",command=order)
orderButton.place(x=340,y=555)



root.mainloop()