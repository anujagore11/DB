
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():

    bid = en1.get()
    title = en2.get()
    subject = en3.get()
    author = en4.get()

    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+subject+"','"+author+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
    except:
        messagebox.showinfo("Error","Can't add data into Database")

    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)

def addBooks():

    global en1,en2,en3,en4,en5,Canvas1,con,cur,bookTable,root

    root = Tk()
    root.title("PhoneBook")
    root.minsize(width=400,height=400)
    root.geometry("560x500")

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase="rpcl_db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

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

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#F8EFBA",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7)

    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)

    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25)

    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.25, relwidth=0.62)

    # Book Subject
    lb3 = Label(labelFrame,text="Subject : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4)

    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.4, relwidth=0.62)

    # Book Author
    lb4 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.55)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.55, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(root,text="Add",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.35,rely=0.7, relwidth=0.18,relheight=0.08)



    root.mainloop()
