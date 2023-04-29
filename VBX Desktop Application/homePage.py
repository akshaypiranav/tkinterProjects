from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root=Tk()
root.title("𝚅𝙴𝙷𝙸𝙲𝙻𝙴 𝙱𝙻𝙰𝙲𝙺 𝙱𝙾𝚇")
root.geometry("700x700+440+45")
#root.state("zoomed")
root.resizable(False,False)
root.config(bg="#000000")


photo=PhotoImage(file='blackbox.png')
root.iconphoto(False,photo)

#FUNCTIONS
def drowsy():
    root.destroy()
    import drowsinessDetectionSystem as ds
    ds


def hardware():
    root.destroy()
    import sosDetectionSystemHardware


def accident():
    root.destroy()
    import accidentDetectionSystem


def fire():
    root.destroy()
    import fireDetectionSystem


def software():
    root.destroy()
    import sosDetectionSystemSoftware


def order():
    root.destroy()
    import orderDetails

#HOME PAGE
homePageTitle=Label(text="𝙷𝙾𝙼𝙴 𝙿𝙰𝙶𝙴",bg="black",fg="#cccccc",font="BOLD").place(x=283,y=15)
productTitle=Label(text="""𝙿
𝚁
𝙾
𝙳
𝚄
𝙲
𝚃
𝚂""",bg="black",fg="#cccccc",font="BOLD").place(x=330,y=266)




#IMAGE BUTTON
drowsinessDetectionImage=Button(width=25,height=10,border=0,text="DDS",command=drowsy).place(x=80,y=50)
emergencyHardware=Button(width=25,height=10,border=0,text="SOS H",command=hardware).place(x=80,y=275)
accidentDetector=Button(width=25,height=10,border=0,text="AD",command=accident).place(x=420,y=50)
fireDetector=Button(width=25,height=10,border=0,text="FD",command=fire).place(x=420,y=275)
emergencySoftware=Button(width=25,height=10,border=0,text="SOS S",command=software).place(x=80,y=500)
orderNow=Button(width=25,height=10,border=0,text="ORDER",command=order).place(x=420,y=500)

drowsinessLabel=Label(text="𝙳𝚁𝙾𝚆𝚂𝙸𝙽𝙴𝚂𝚂 𝙳𝙴𝚃𝙴𝙲𝚃𝙸𝙾𝙽",bg="black",fg="#cccccc",font="BOLD").place(x=52,y=225)
hardwareLabel=Label(text="𝙴𝙼𝙴𝚁𝙶𝙴𝙽𝙲𝚈 𝙷𝙰𝚁𝙳𝚆𝙰𝚁𝙴",bg="black",fg="#cccccc",font="BOLD").place(x=405,y=225)
accidentLabel=Label(text="𝙰𝙲𝙲𝙸𝙳𝙴𝙽𝚃 𝙳𝙴𝚃𝙴𝙲𝚃𝙾𝚁",bg="black",fg="#cccccc",font="BOLD").place(x=68,y=450)
fireLabel=Label(text="𝙵𝙸𝚁𝙴 𝙳𝙴𝚃𝙴𝙲𝚃𝙾𝚁",bg="black",fg="#cccccc",font="BOLD").place(x=430,y=450)
softwareLabel=Label(text="𝙴𝙼𝙴𝚁𝙶𝙴𝙽𝙲𝚈 𝚂𝙾𝙵𝚃𝚆𝙰𝚁𝙴",bg="black",fg="#cccccc",font="BOLD").place(x=60,y=670)
orderLabel=Label(text="𝙾𝚁𝙳𝙴𝚁 𝙽𝙾𝚆",bg="black",fg="#cccccc",font="BOLD").place(x=450,y=670)


root.mainloop()