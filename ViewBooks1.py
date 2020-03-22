from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import tkinter.font as tkFont
import tkinter.ttk as ttk

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="rpcl_db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table

def View():

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
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="VIEW BOOKs", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)

    y = 0.25

    #Label(labelFrame, text="%-10s%-30s%-20s%-30s"%('BID','Title','Subject','Author'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    #Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable

    msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6))
    msg.pack(fill='x')
    car_header = ['bid', 'title', 'subject', 'author']
    container = ttk.Frame()
    container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
    tree = ttk.Treeview(Canvas1,columns=car_header, show="headings")
    vsb = ttk.Scrollbar(orient="vertical",
        command=tree.yview)
    hsb = ttk.Scrollbar(orient="horizontal",
        command=tree.xview)
    tree.configure(yscrollcommand=vsb.set,
        xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew', in_=container)
    vsb.grid(column=1, row=0, sticky='ns', in_=container)
    hsb.grid(column=0, row=1, sticky='ew', in_=container)
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            tree.insert('', 'end', values=i)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if tree.column(car_header[ix],width=None)<col_w:
                    tree.column(car_header[ix], width=col_w)
            #Label(labelFrame, text="%-10s%-30s%-20s%-30s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            #y += 0.1
    except:
        messagebox.showinfo("Bad Format","Can't fetch files from database")

    root.mainloop()
