from tkinter import Toplevel
from tkinter import Menu
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox as msg
from tkcalendar import Calendar,DateEntry
import re
import smtplib
###############################################   BUILDING CONNECTION        ######################################
con = mysql.connector.connect(host='localhost',user='root',password='',database='library')
concommand = con.cursor()
###############################################   BUILDING CONNECTION        ######################################

def student():
    stud = Toplevel()
    stud.title("Welcome To Library")
    stud.geometry("1500x800+0+0")
    stud.iconbitmap('images/logo.ico')
    stud.minsize(400,500)
    pic = ImageTk.PhotoImage(file="images/pexels-cottonbro-4855428.jpg")
    label = Label(stud,image=pic)
    label.pack()


    ######################  CONTENT FRAME   ############
    frame_dash = Frame(stud ,bg='#f7f1e3')
    frame_dash.place(width=400,height=320,x=560,y=180)
    ###################  HEADING PORTION   ##########
    heading_bookadd = Frame(stud, bg="lightcyan", bd=10, relief="groove")
    heading_bookadd.place(x=510, y=60, width=480, height=100)
    ###################  HEADING PORTION END  ##########
    ####################  HEADING PORTION Data  ##########
    heading_bookadd_content = Label(heading_bookadd, text="Welcome To \nLibrary", bg='#EAF0F1', fg='black',font=  ("Goudy old style", 26, "bold"))
    heading_bookadd_content.place(x=0, y=0, width=460)

    ###################  HEADING PORTION END  ##########
    ######################  CONTENT FRAME END   ############

    ######################  CONTENT in FRAME   ############
    def bookstock():
        global frame_bookview
        global heading_bookview
        frame_bookview = Frame(stud)
        frame_bookview.place(width=600, height=470, x=450, y=170)
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

    def view_back():
        frame_bookview.destroy()
    def bookview():
        global frame_bookview
        global heading_bookview
        frame_bookview = Frame(stud)
        frame_bookview.place(width=600, height=470, x=450, y=170)
        e = Label(frame_bookview, width=22, text='      BookId',height=1,borderwidth=2, relief='ridge', anchor='w', bg='lightgray',font=('Consolas', 12, 'bold '))
        e.grid(row=0, column=0)
        e = Label(frame_bookview ,width=22, text='      BookName',height=1,borderwidth=2, relief='ridge', anchor='w', bg='lightgray',font=('Consolas', 13, 'bold '))
        e.grid(row=0, column=1)
        e = Label(frame_bookview, width=22, text='      BookAuthor', height=1,borderwidth=2, relief='ridge', anchor='w',bg='lightgray',font=('Consolas', 12, 'bold '))
        e.grid(row=0, column=2)


        concommand.execute("select bookid,bookname,bookauthor from addbook")
        i=1
        res = concommand.fetchall()
        for display in res:
            for columns in range(len(display)):
                e = Label(frame_bookview,text = display[columns],width=28,height=2,borderwidth=2,relief='ridge')
                e.grid(row=i,column = columns)
            i = i+1

        button_view_back = Button(frame_bookview, text="< Back", bg='black',command = view_back,cursor="hand2", fg='white',font=('Consolas', 21, 'bold '))
        button_view_back.place(x=50, y=400)


        ################################  BOOK VIEW ENDS  ######################################################
    def subs():
        subs_entry = entry_user.get()
        pattern = regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(pattern, subs_entry):
            if subs_entry.strip()!="":
                concommand.execute("insert into subscribe (email) values ('{}')".format(subs_entry))
                con.commit()
                msg.showinfo("Sucessfull","Thankyou for Subscribing!!")
                frame_bookview.focus()

                s = smtplib.SMTP('smtp.gmail.com',587)  ###  FOR PORT NUMBER
                s.starttls()
                s.login("kapilsaini4848@gmail.com","8607696626")
                message = f"Hey {subs_entry},\n Thankyou for Subscribing us!\n\n\n Get Ready To Recieve all news and important announcement of your Favourite library at you fingertips.\n\n\n\n\nThankyou:)\nHave a Good One!!!"
                subject ="Library"
                mess = 'subject:{}\n\n{}'.format(subject,message)         ### IT WILL ADD SUBJECT..
                s.sendmail("kapilsaini4848@gmail.com",subs_entry,mess)
                s.quit()
                print("Mail Sent")



                labelclass.set('')
                entryclass.set('')

            else:
                print("blank")
        else:
            labelclass.set("****** Invalid Email Id")









    def subscribe():
        global frame_bookview

        frame_bookview = Frame(stud)
        frame_bookview.place(width=600, height=320, x=450, y=170)
        label = Label(frame_bookview,text="Enter Your Email in\n order to Catch\n our all new Announcements.",bg="white",fg="green",font=("aerial", 18, 'bold italic'))
        label.pack(pady=10)

        label1 = Label(frame_bookview,text="Email:",fg="black",font=("Goudy old style", 22, "bold"))
        label1.place(x=50,y=150)
        global entry_user
        global entryclass
        entryclass=StringVar()
        entry_user = Entry(frame_bookview, fg='black', textvariable=entryclass,bg='lightgray',  font=("Helvetica", 16))
        entry_user.place(x=160, y=155, width=350, height=30)
        global labelclass
        labelclass = StringVar()
        labelclass.set('')
        Label(frame_bookview,fg='red',textvariable=labelclass, font="calibiri 14 bold italic").place(x=160,y=210)


        Button(frame_bookview, text="Subscribe",  fg='green', command=subs, cursor="hand2",  font=('aerial', 20,'bold')).place(x=420,y=260)
        Button(frame_bookview, text="< Back",  fg='green', command=view_back, cursor="hand2",  font=('aerial', 20,'bold')).place(x=20,y=260)


    def quitt():
        c=msg.askyesno("Logout","Are you sure you want to Logout")
        if c==True:
            stud.destroy()
        else:
            stud.focus()





    btn1 = Button(frame_dash,text="View Books",bg='black', fg='white',command=bookview,cursor="hand2",font=('Consolas',22))
    btn1.place(x=0,y=0,width=400)

    btn2 = Button(frame_dash,text="Availability of Books",bg='black', fg='white',command=bookstock,cursor="hand2",font=('Consolas',22))
    btn2.place(x=0,y=80,width=400)

    btn3 = Button(frame_dash,text="Subscribe",bg='black', fg='white',command=subscribe,cursor="hand2",font=('Consolas',22))
    btn3.place(x=0,y=160,width=400)

    btn4 = Button(frame_dash,text="Logout",bg='black', fg='white',command=quitt,cursor="hand2",font=('Consolas',22))
    btn4.place(x=0,y=240,width=400)


    menubar = Menu(stud)
    m1 = Menu(menubar,tearoff=0,font=('Calibiri',11))
    m1.add_command(label="View Books",command=bookview)
    menubar.add_cascade(label='View',menu=m1)

    m2 = Menu(menubar,tearoff=0,font=('Calibiri',11))
    m2.add_command(label="Availability of Books",command=bookstock)
    menubar.add_cascade(label='Availability', menu=m2)

    m3 = Menu(menubar,tearoff=0,font=('Calibiri',11))
    m3.add_command(label="Subscribe Us",command=subscribe)
    menubar.add_cascade(label='Subscribe', menu=m3)


    m4 = Menu(menubar,tearoff=0)
    m4.add_command(label="Logout",command=quitt)
    menubar.add_cascade(label='Logout', menu=m4)

    stud.config(menu=menubar)


    ######################  CONTENT in FRAME END   ############

    stud.mainloop()
