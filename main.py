from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBooks import *
from DeleteBook import *
from ViewBooks import *
from SearchBook import *


# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="rpcl_db"


root = Tk()
root.title("PhoneBook")
root.minsize(width=400,height=400)
root.geometry("560x500")
count = 0
empFrameCount = 0

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def empMenu():

    global headingFrame1,headingFrame2,headingLabel,btn1,Canvas1,labelFrame,backBtn
    headingFrame1.destroy()

    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#f7f1e3",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#333945",bd=3)
    headingFrame1.place(relx=0.36,rely=0.1,relwidth=0.3,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text=" MENU", fg='black', bg="#EAF0F1",font = "Verdana 17 bold")
    headingLabel.place(relx=0.20,rely=0.15, relwidth=0.6, relheight=0.6)

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBooks)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Search Book",bg='black', fg='white', command=searchBook)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

# Take n greater than 0.25 and less than 5
same=True
n=1.98

# Adding a background image
background_image =Image.open("book.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(280,360,image = img)
Canvas1.config(bg="black",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root)
headingFrame1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.1)

#headingFrame2 = Frame(headingFrame1)
#headingFrame2.place(relx=0.00,rely=0.05,relwidth=0.9,relheight=0.8)

headingLabel = Label(headingFrame1, text="Phone-Book", fg='black', font = "Verdana 19 bold")
headingLabel.place(relx=0.09,rely=0.21, relwidth=0.9, relheight=0.6)

btn1 = Button(root,text="Open",bg='white', fg='black', relief = RAISED,command=empMenu)
btn1.place(relx=0.40,rely=0.28, relwidth=0.2,relheight=0.08)

root.mainloop()
