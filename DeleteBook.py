from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="rpcl_db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table

def deleteBook():

    bid = en1.get()
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
    except:
        messagebox.showinfo("Check Credentials","Please check Book ID")

    en1.delete(0, END)

def delete():

    global en1,en2,en3,en4,en5,Canvas1,con,cur,bookTable,root

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    same=True
    n=0.3

    # Adding a background image
    background_image =Image.open("library.jpg")
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
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.3)

    headingFrame1 = Frame(root,bg="#333945",bd=3)
    #headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingFrame1.place(relx=0.36,rely=0.1,relwidth=0.3,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    #headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="DELETE BOOK", fg='black', bg="#EAF0F1",font = "Verdana 17 bold")
    #headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    headingLabel.place(relx=0.20,rely=0.15, relwidth=0.6, relheight=0.6)

    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.5, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(root,text="Delete",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)



    root.mainloop()
