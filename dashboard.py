from tkinter import Toplevel
from tkinter import Menu
from tkinter import *
# from book_add import bookadd
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox as msg
from tkcalendar import Calendar,DateEntry


###############################################   BUILDING CONNECTION        ######################################
con = mysql.connector.connect(host='localhost',user='root',password='',database='library')
concommand = con.cursor()
###############################################   BUILDING CONNECTION        ######################################

def dash():
    dash = Toplevel()
    dash.title("Welcome To Dashboard")
    dash.geometry("1500x800+0+0")
    dash.iconbitmap('images/logo.ico')
    dash.minsize(400,500)

######################################################################################################################################################################
 #TODO:   #####################################   INSERT BOOK STARTS HERE   ####################################################

    def insert():
        bid = entry_bookid.get()
        bname = entry_bookname.get()
        bauth = entry_bookauthor.get()
        bstock = entry_spinbox.get()

        if bid.strip() != "":
            if bname.strip() != "":
                if bauth.strip() != "":
                    try:
                        concommand.execute(
                            "insert into addbook(bookid,bookname,bookauthor,bookstock)values('{}','{}','{}','{}')".format(bid, bname, bauth, bstock))
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
        entry4.set("")

    def back_insert():
        frame_bookadd.destroy()
        heading_bookadd.destroy()
    def back_delete():
        frame_bookdelete.destroy()
        heading_bookdelete.destroy()

    def bookadd():
        global frame_bookadd
        global heading_bookadd
        frame_bookadd = Frame(dash)
        frame_bookadd.place(width=600, height=470, x=450, y=170)
        ###################  HEADING PORTION   ##########
        heading_bookadd = Frame(dash, bg="lightcyan", bd=10, relief="groove")
        heading_bookadd.place(x=510, y=60, width=480, height=100)
        ###################  HEADING PORTION END  ##########
        ####################  HEADING PORTION Data  ##########
        heading_bookadd_content = Label(heading_bookadd, text="Add Books", bg='#EAF0F1', fg='black',  font=('Consolas', 26, 'bold '))
        heading_bookadd_content.place(x=0, y=0, width=460)
        ###################  HEADING PORTION END  ##########
        global entry_bookid
        global entry_bookname
        global entry_bookauthor
        global entry_spinbox
        global entry1
        global entry2
        global entry3
        global entry4


        entry1 = StringVar()
        entry2 = StringVar()
        entry3 = StringVar()
        entry4 = StringVar()

        lbl1 = Label(frame_bookadd, text="BookId:", fg="black", font=('Consolas', 22, 'bold '))
        lbl1.place(x=50, y=80)

        entry_bookid = Entry(frame_bookadd, bg='lightgray', textvariable=entry1,width=25, fg='black', font=("Helvetica", 16))
        entry_bookid.place(x=250, y=85)

        lbl2 = Label(frame_bookadd, text="BookName:", fg="black", font=('Consolas', 22, 'bold '))
        lbl2.place(x=50, y=160)

        entry_bookname = Entry(frame_bookadd, bg='lightgray', textvariable=entry2,width=25, fg='black', font=("Helvetica", 16))
        entry_bookname.place(x=250, y=165)

        lbl3 = Label(frame_bookadd, text="BookAuthor:", fg="black", font=('Consolas', 22, 'bold '))
        lbl3.place(x=50, y=240)

        entry_bookauthor = Entry(frame_bookadd, bg='lightgray',width=25, textvariable=entry3, fg='black', font=("Helvetica", 16))
        entry_bookauthor.place(x=250, y=250)

        lbl4 = Label(frame_bookadd, text="BookStock:", fg="black", font=('Consolas', 22, 'bold '))
        lbl4.place(x=50, y=320)

        entry_spinbox = Spinbox(frame_bookadd, from_=0, to=100,textvariable=entry4)
        entry_spinbox.place(x=250, y=328, width=300,height=20)

        button_insert = Button(frame_bookadd, text="Insert", bg='black', cursor="hand2", command=insert, fg='white',font=('Consolas', 22, 'bold '))
        button_insert.place(x=450, y=400)

        button_back = Button(frame_bookadd, text="< Back", bg='black', cursor="hand2", command=back_insert, fg='white',font=('Consolas', 22, 'bold '))
        button_back.place(x=50, y=400)

        ####################################################    INSERT BOOK END HERE   #######################################################


####################################################################################################################################################################
        ################################ ##########todo:  BOOK DELETE STARTS HERE  ##################################################
    def delete():
        bookdel = entry_bookdel.get()
        if bookdel.strip()!="":
            concommand.execute("select * from addbook where bookid={}".format(bookdel))
            result = concommand.fetchone()
            if result==None:
                msg.showerror("Error", "BookId does not exist")
                dash.focus()
            else:
                concommand.execute("delete from addbook where bookid={}".format(bookdel))
                con.commit()
                msg.showinfo("SUCESS","Book Record Deleted Sucessfully")
                dash.focus()
        else:
            msg.showerror("Error","BookId cannot be Empty")
            dash.focus()

        var_delete.set("")






    def bookdelete():
        global var_delete
        global heading_bookdelete
        var_delete=StringVar()
        global frame_bookdelete
        frame_bookdelete = Frame(dash)
        frame_bookdelete.place(width=600, height=470, x=450, y=170)
        ###################  HEADING PORTION   ##########
        heading_bookdelete = Frame(dash, bg="lightcyan", bd=10, relief="groove")
        heading_bookdelete.place(x=510, y=60, width=480, height=100)
        ###################  HEADING PORTION END  ##########
        ####################  HEADING PORTION Data  ##########
        heading_bookadd_content = Label(heading_bookdelete, text="Delete Book", bg='#EAF0F1', fg='black', font=('Consolas', 26, 'bold '))
        heading_bookadd_content.place(x=0, y=0, width=460)
        ###################  HEADING PORTION END  ##########
        lbl_del = Label(frame_bookdelete, text="BookId:", fg="black", font=('Consolas', 22, 'bold '))
        lbl_del.place(x=50, y=80)

        global entry_bookdel
        entry_bookdel = Entry(frame_bookdelete, bg='lightgray', textvariable=var_delete,fg='black', font=("Helvetica", 16))
        entry_bookdel.place(x=250, y=85)


        button_insert = Button(frame_bookdelete, text="Delete", bg='black', cursor="hand2", command=delete, fg='white',font=('Consolas', 22, 'bold '))
        button_insert.place(x=450, y=400)

        button_back = Button(frame_bookdelete, text="< Back", bg='black', cursor="hand2", command=back_delete, fg='white',font=('Consolas', 22, 'bold '))
        button_back.place(x=50, y=400)
        ################################   BOOK DELETE ENDS  HERE  ######################################


#####################################################################################################################################################################
        ################################todo:   BOOK ISSUE STARTS  HERE  ######################################

    def issue_back():
        frame_bookissue.destroy()
        heading_bookissue.destroy()
    def issue():
        issue_bid = lbl_issue_bid_entry.get()
        issue_sid = lbl_issue_sid_entry.get()
        issue_from = lbl_issue_from_entry.get()
        issue_to = lbl_issue_to_entry.get()

        if issue_bid.strip()!="":
            if issue_sid.strip()!="":
                if issue_from.strip()!="":
                    if issue_to.strip()!="":
                        concommand.execute("select bookstock from addbook where bookid={} ".format(issue_bid))
                        store = concommand.fetchone()
                        for k in store:
                            print(k)
                            try:
                                if k>0:

                                    concommand.execute("insert into issuebook(bookid,studentid,start,end)values('{}','{}','{}','{}')".format(issue_bid,issue_sid,issue_from,issue_to))
                                    con.commit()
                                    msg.showinfo("Suceess","Book Issued")
                                    concommand.execute("update addbook set bookstock=bookstock-1 where bookid={} ".format(issue_bid))
                                    con.commit()
                                    dash.focus()
                                else:
                                    msg.showerror("Error"," Book is out of stock")
                                    dash.focus()
                            except:
                                msg.showerror("Error", "Only one book is allowed per Student")
                                dash.focus()
                    else:
                        pass
                else:
                    pass
            else:
                msg.showerror("Error","Student Id cannot be Blank")
                dash.focus()
        else:
            msg.showerror("Error","BookId cannot be Blank")
            dash.focus()
        issue1_var.set("")
        issue2_var.set("")


    def bookissue():
        global issue1_var
        global issue2_var
        issue1_var = StringVar()
        issue2_var = StringVar()
        global frame_bookissue
        global heading_bookissue
        frame_bookissue = Frame(dash)
        frame_bookissue.place(width=600, height=470, x=450, y=170)
            ###################  HEADING PORTION   ##########
        heading_bookissue = Frame(dash, bg="lightcyan", bd=10, relief="groove")
        heading_bookissue.place(x=510, y=60, width=480, height=100)
            ###################  HEADING PORTION END  ##########
            ####################  HEADING PORTION Data  ##########
        heading_bookissue_content = Label(heading_bookissue, text="Issue Book", bg='#EAF0F1', fg='black', font=('Consolas', 26, 'bold '))
        heading_bookissue_content.place(x=0, y=0, width=460)
        ###################  HEADING PORTION END  ##########
        lbl_issue_bid = Label(frame_bookissue, text="  BookId:", fg="black", font=('Consolas', 22, 'bold '))
        lbl_issue_bid.place(x=50, y=80)
        global lbl_issue_bid_entry

        lbl_issue_bid_entry = Entry(frame_bookissue, bg='lightgray',textvariable=issue1_var,fg='black', font=("Helvetica", 16))
        lbl_issue_bid_entry.place(x=250, y=85)


        lbl_issue_sid = Label(frame_bookissue, text="StudentId:", fg="black", font=('Consolas', 22, 'bold '))
        lbl_issue_sid.place(x=50, y=160)
        global lbl_issue_sid_entry
        lbl_issue_sid_entry = Entry(frame_bookissue, bg='lightgray',textvariable=issue2_var, fg='black', font=("Helvetica", 16))
        lbl_issue_sid_entry .place(x=250, y=165)

        lbl_issue_from  = Label(frame_bookissue, text="  From:", fg="black", font=('Consolas', 22, 'bold '))
        lbl_issue_from .place(x=50, y=240)

        # entry_bookname = Entry(frame_bookissue, bg='lightgray', fg='black', font=("Helvetica", 16))
        # entry_bookname.place(x=250, y=245)
        global lbl_issue_from_entry
        lbl_issue_from_entry = DateEntry(frame_bookissue,width=37,height=100,bg="darkblue",fg="white",year=2021)
        lbl_issue_from_entry.place(x=250,y=250)

        lbl_issue_to  = Label(frame_bookissue, text="   To:", fg="black", font=('Consolas', 22, 'bold '))
        lbl_issue_to .place(x=50, y=320)

        global lbl_issue_to_entry
        lbl_issue_to_entry = DateEntry(frame_bookissue,width=37,height=100,bg="darkblue",fg="white",year=2021)
        lbl_issue_to_entry.place(x=250,y=330)

        button_issue = Button(frame_bookissue, text="Issue", bg='black', cursor="hand2", command=issue, fg='white',font=('Consolas', 22, 'bold '))
        button_issue.place(x=450, y=400)

        button_issue_back = Button(frame_bookissue, text="< Back", bg='black',command = issue_back ,cursor="hand2", fg='white',font=('Consolas', 22, 'bold '))
        button_issue_back.place(x=50, y=400)

        ################################ #############  BOOK ISSUE EMDS  HERE  #############  ########################################



###################################################################################################################################################################
        ##########################################todo:   BOOK RETURN STARTS   ###### #################################################

    def book_return():
        return_bid = lbl_return_bid_entry.get()
        return_sid = lbl_return_sid_entry.get()


        if return_bid.strip()!="":
            if return_sid.strip()!="":
                concommand.execute("select bookid from issuebook where bookid='{}'".format(return_bid))
                result1 = concommand.fetchall()
                concommand.execute("select studentid from issuebook where studentid='{}'".format(return_sid))
                result2 = concommand.fetchall()
                if result1 and result2:
                    try:
                        concommand.execute("delete from issuebook where studentid='{}'".format(return_sid))
                        con.commit()
                        concommand.execute("update addbook set bookstock = bookstock+1")
                        con.commit()
                        msg.showinfo("Sucessfull", "Returned Sucessfully")
                        dash.focus()
                    except:
                        msg.showerror("ERROR","Something is Wrong")
                else:
                    msg.showerror("Error","Invalid Details")
                    dash.focus()
            else:
                msg.showerror("Error","StudentId Cannot Be Blank ")
                dash.focus()
        else:
            msg.showerror("Error","BookId Cannot be Blank")
            dash.focus()

        entry1.set('')
        entry2.set('')


    def button_back():
        frame_bookreturn.destroy()
        heading_bookreturn.destroy()


    def bookreturn():
        global frame_bookreturn
        global heading_bookreturn
        global entry1
        global entry2
        frame_bookreturn = Frame(dash)
        frame_bookreturn.place(width=600, height=470, x=450, y=170)
            ###################  HEADING PORTION   ##########
        heading_bookreturn = Frame(dash, bg="lightcyan", bd=10, relief="groove")
        heading_bookreturn.place(x=510, y=60, width=480, height=100)
            ###################  HEADING PORTION END  ##########
            ####################  HEADING PORTION Data  ##########
        heading_bookupdate_content = Label(heading_bookreturn, text="Return Book", bg='#EAF0F1', fg='black', font=('Consolas', 26, 'bold '))
        heading_bookupdate_content.place(x=0, y=0, width=460)
        ###################  HEADING PORTION END  ##########
        lbl_return_bid = Label(frame_bookreturn, text="  BookId:", fg="black", font=('Consolas', 22, 'bold '))
        lbl_return_bid.place(x=50, y=80)

        global lbl_return_bid_entry
        entry1 = StringVar()
        lbl_return_bid_entry = Entry(frame_bookreturn, bg='lightgray',width=25,textvariable=entry1,fg='black', font=("Helvetica", 16))
        lbl_return_bid_entry.place(x=250, y=85)

        lbl2 = Label(frame_bookreturn, text=" StudentId:", fg="black", font=('Consolas', 22, 'bold '))
        lbl2.place(x=50, y=160)

        global lbl_return_sid_entry
        entry2 = StringVar()
        lbl_return_sid_entry = Entry(frame_bookreturn, bg='lightgray', textvariable=entry2,width=25, fg='black', font=("Helvetica", 16))
        lbl_return_sid_entry.place(x=250, y=165)


        button_return = Button(frame_bookreturn, text="Return", bg='black', cursor="hand2", command=book_return, fg='white',font=('Consolas', 22, 'bold '))
        button_return.place(x=450, y=400)

        button_return_back = Button(frame_bookreturn, text="< Back", bg='black',command = button_back,cursor="hand2", fg='white',font=('Consolas', 21, 'bold '))
        button_return_back.place(x=50, y=400)



        ################################   BOOK RETURN ENDS    #################################################

#####################################################################################################################################################################
        ################################ todo: BOOK VIEW STARTS ###############################################
    def view_back():
        frame_bookview.destroy()
        heading_bookview.destroy()

    def bookview():
        global frame_bookview
        global heading_bookview
        frame_bookview = Frame(dash)
        frame_bookview.place(width=600, height=470, x=450, y=170)
        ###################  HEADING PORTION   ##########
        heading_bookview = Frame(dash, bg="lightcyan", bd=10, relief="groove")
        heading_bookview.place(x=510, y=60, width=480, height=100)
        ###################  HEADING PORTION END  ##########
        ####################  HEADING PORTION Data  ##########
        heading_bookview_content = Label(heading_bookview, text="View Books", bg='#EAF0F1', fg='black',  font=('Consolas', 26, 'bold '))
        heading_bookview_content.place(x=0, y=0, width=460)
        ###################  HEADING PORTION END  ##########
        e = Label(frame_bookview, width=21, text='      BookId',height=1,borderwidth=2, relief='ridge', anchor='w', bg='lightgray',font=('Consolas', 10, 'bold '))
        e.grid(row=0, column=0)
        e = Label(frame_bookview ,width=21, text='      BookName',height=1,borderwidth=2, relief='ridge', anchor='w', bg='lightgray',font=('Consolas', 10, 'bold '))
        e.grid(row=0, column=1)
        e = Label(frame_bookview, width=21, text='      BookAuthor', height=1,borderwidth=2, relief='ridge', anchor='w',bg='lightgray',font=('Consolas', 10, 'bold '))
        e.grid(row=0, column=2)
        e = Label(frame_bookview, width=21, text='      BookStock', height=1,borderwidth=2, relief='ridge', anchor='w', bg='lightgray',font=('Consolas', 10, 'bold '))
        e.grid(row=0, column=3)




        concommand.execute("select * from addbook")
        i=1
        res = concommand.fetchall()
        for display in res:
            for columns in range(len(display)):
                e = Label(frame_bookview,text = display[columns],width=21,height=2,borderwidth=2,relief='ridge')
                e.grid(row=i,column = columns)
            i = i+1

        button_view_back = Button(frame_bookview, text="< Back", bg='black',command = view_back,cursor="hand2", fg='white',font=('Consolas', 21, 'bold '))
        button_view_back.place(x=50, y=400)


        ################################  BOOK VIEW ENDS  ######################################################






#########################################todo:  CONTENT OF MAIN PAGE  ############################################
    # def qu():
    #     frame_book.destroy()
    bg_admin = ImageTk.PhotoImage(file="images/admin.jpg")
    label = Label(dash, image=bg_admin)
    label.pack()
    ###################  HEADING PORTION   ##########
    heading_frame = Frame(dash,bg="#EAF0F1",bd=10,relief="groove")
    heading_frame.place(x=510,y=60,width=480,height=100)
    ###################  HEADING PORTION END  ##########

    ####################  HEADING PORTION Data  ##########
    heading_frame_content = Label(heading_frame,text="Welcome\nAdmin",bg='#EAF0F1',fg='black',font=('Consolas',26,'bold '))
    heading_frame_content.place(x=0,y=0,width=460)
    ###################  HEADING PORTION END  ##########
    # headingFrame2 = Frame(heading_frame,bg="#EAF0F1")
    # headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    ######################  CONTENT FRAME   ############
    frame_dash = Frame(dash ,bg='#f7f1e3')
    frame_dash.place(width=400,height=450,x=560,y=180)
    ######################  CONTENT FRAME END   ############

    ######################  CONTENT in FRAME   ############

    btn1 = Button(frame_dash,text="Insert Book",bg='black', fg='white',command=bookadd,cursor="hand2",font=('Consolas',24,'bold '))
    btn1.place(x=0,y=0,width=400)

    btn2 = Button(frame_dash,text="Delete Book",bg='black', fg='white',command=bookdelete,cursor="hand2",font=('Consolas',24,'bold '))
    btn2.place(x=0,y=80,width=400)

    btn3 = Button(frame_dash,text="Issue Book",bg='black', fg='white',command=bookissue,cursor="hand2",font=('Consolas',24,'bold '))
    btn3.place(x=0,y=160,width=400)

    btn4 = Button(frame_dash,text="Return Book",bg='black', fg='white',command=bookreturn,cursor="hand2",font=('Consolas',24,'bold '))
    btn4.place(x=0,y=240,width=400)

    btn5 = Button(frame_dash,text="View Books",bg='black', fg='white',command=bookview,cursor="hand2",font=('Consolas',24,'bold '))
    btn5.place(x=0,y=320,width=400)


    ######################  CONTENT in FRAME END   ############

    menubar = Menu(dash)
    m1 = Menu(menubar,tearoff=0,font=('Calibiri',11))
    m1.add_command(label="Insert Book",command=bookadd)
    m1.add_command(label="Delete Book",command=bookdelete)
    menubar.add_cascade(label='Library',menu=m1)

    m2 = Menu(menubar,tearoff=0,font=('Calibiri',11))
    m2.add_command(label="Issue Book",command=bookissue)
    m2.add_command(label="Return Book",command=bookreturn)
    menubar.add_cascade(label='Issue', menu=m2)

    m3 = Menu(menubar,tearoff=0,font=('Calibiri',11))
    m3.add_command(label="View Books",command=bookview)
    menubar.add_cascade(label='View', menu=m3)


    m4 = Menu(menubar,tearoff=0)
    m4.add_command(label="Logout",command=quit)
    menubar.add_cascade(label='Logout', menu=m4)

    dash.config(menu=menubar)





    # def Del_delete():
    #     Emp_frame=Frame(dash,bg="black")
    #     Emp_frame.place(x=100,y=100,width=300,height=300)
    # mymenubar=Menu(dash)
    # file=Menu(mymenubar,tearoff=0)
    # file.add_command(label="Add Book",command=book_add)
    # file.add_command(label="Delete Record",command=Del_delete)
    # file.add_command(label="Update Record")
    # file.add_separator()
    # mymenubar.add_cascade(label="Employee",menu=file)
    #
    # file2=Menu(mymenubar)
    # file2.add_command(label="View Employee Record")
    # file2.add_separator()
    # file2.add_command(label="Search Employee")
    # file2.add_separator()
    # file2.add_command(label="View Department")
    # mymenubar.add_cascade(label="Employee Manage", menu=file2)
    #
    # file3=Menu(mymenubar)
    # file3.add_command(label="Change password")
    # file3.add_separator()
    # file3.add_command(label="Help")
    # file3.add_separator()
    #
    # def Close():
    #     dash.withdraw()
    #
    # file3.add_command(label="Logout",command=Close)
    #
    # mymenubar.add_cascade(label="Setting", menu=file3)
    # dash.config(menu=mymenubar)

    dash.mainloop()
