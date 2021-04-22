
###############################################   BUILDING CONNECTION        ######################################
con = mysql.connector.connect(host='localhost',user='root',password='',database='library')
concommand = con.cursor()
###############################################   BUILDING CONNECTION        ######################################

def insert():
    bid = entry_bookid.get()
    bname = entry_bookname.get()
    bauth = entry_bookauthor.get()
    bdrop = dropdown.get()

    if bid.strip() != "":
        if bname.strip() != "":
            if bauth.strip() != "":
                try:
                    concommand.execute(
                        "insert into addbook(bookid,bookname,bookauthor,bookstatus)values('{}','{}','{}','{}')".format(
                            bid, bname, bauth, bdrop))
                    con.commit()
                    msg.showinfo("SUCESS", f"Book Inserted {bid}")
                    dash.focus()
                except:
                    msg.showerror("ERROR", 'BookId Already EXIST')
                    dash.focus()
            else:
                msg.showerror("ERROR", "Author Name cannot be Empty")
                dash.focus()
        else:
            msg.showerror("ERROR", "Name cannot be Empty")
            dash.focus()
    else:
        msg.showerror("ERROR", "ID cannot be Empty")
        dash.focus()

    entry1.set("")
    entry2.set("")
    entry3.set("")


def back():
    frame_bookadd.destroy()


def bookadd():
    global frame_bookadd
    frame_bookadd = Frame(dash)
    frame_bookadd.place(width=600, height=470, x=450, y=170)
    ###################  HEADING PORTION   ##########
    heading_bookadd = Frame(dash, bg="lightcyan", bd=10, relief="groove")
    heading_bookadd.place(x=510, y=60, width=480, height=100)
    ###################  HEADING PORTION END  ##########
    ####################  HEADING PORTION Data  ##########
    heading_bookadd_content = Label(heading_bookadd, text="Add Books", bg='#EAF0F1', fg='black',
                                    font=('Consolas', 26, 'bold '))
    heading_bookadd_content.place(x=0, y=0, width=460)
    ###################  HEADING PORTION END  ##########
    global entry_bookid
    global entry_bookname
    global entry_bookauthor
    global dropdown
    global entry1
    global entry2
    global entry3
    global entry4

    entry1 = StringVar()
    entry2 = StringVar()
    entry3 = StringVar()

    lbl1 = Label(frame_bookadd, text="BookId:", fg="black", font=('Consolas', 22, 'bold '))
    lbl1.place(x=50, y=80)

    entry_bookid = Entry(frame_bookadd, bg='lightgray', textvariable=entry1, fg='black', font=("Helvetica", 16))
    entry_bookid.place(x=250, y=85)

    lbl2 = Label(frame_bookadd, text="BookName:", fg="black", font=('Consolas', 22, 'bold '))
    lbl2.place(x=50, y=160)

    entry_bookname = Entry(frame_bookadd, bg='lightgray', textvariable=entry2, fg='black', font=("Helvetica", 16))
    entry_bookname.place(x=250, y=165)

    lbl3 = Label(frame_bookadd, text="BookAuthor:", fg="black", font=('Consolas', 22, 'bold '))
    lbl3.place(x=50, y=240)

    entry_bookauthor = Entry(frame_bookadd, bg='lightgray', textvariable=entry3, fg='black', font=("Helvetica", 16))
    entry_bookauthor.place(x=250, y=250)

    lbl4 = Label(frame_bookadd, text="BookStatus:", fg="black", font=('Consolas', 22, 'bold '))
    lbl4.place(x=50, y=320)

    status = ["Available",
              "NotAvailable"]
    dropdown = StringVar()
    dropdown.set(status[0])
    store = OptionMenu(frame_bookadd, dropdown, *status)
    store.place(x=250, y=328, width=250)

    button_insert = Button(frame_bookadd, text="Insert", bg='black', cursor="hand2", command=insert, fg='white',
                           font=('Consolas', 22, 'bold '))
    button_insert.place(x=450, y=400)

    button_back = Button(frame_bookadd, text="< Back", bg='black', cursor="hand2", command=back, fg='white',
                         font=('Consolas', 22, 'bold '))
    button_back.place(x=50, y=400)
