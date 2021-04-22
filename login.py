from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as msg
import mysql.connector
from dashboard import dash
from student import student
from signup import signup
root = Tk()

#####################  VARIABLES FOR USERNAME ENTRY AND PASSOWRD STARTS###############################
username_user = StringVar()
password_pass = StringVar()
#####################  VARIABLES FOR USERNAME ENTRY AND PASSOWRD END###############################

#########################FUNCTION FOR CLEARING DATA FROM ENTRY FIELDS###########################
def clear():
    username_user.set("")
    password_pass.set("")
#########################FUNCTION FOR CLEARING DATA FROM ENTRY FIELDS###########################entry_spinbox

#########################  LOGIN STARTS  ###################################################

def login():
    username_login=username_user.get()
    userpass_login=password_pass.get()


    if username_login=="" or userpass_login =="":
        msg.showerror("error","Enter User Name And Password")
    else:
        con = mysql.connector.connect(host='localhost',user='root',password='',database='library')
        concommand=con.cursor()
        concommand.execute("select user and pass from login where user=%s and pass = %s", (username_login, userpass_login) )
        result_login = concommand.fetchone()
        concommand.execute("select username and password from register where username=%s and password = %s", (username_login, userpass_login) )
        result_register = concommand.fetchone()

        if result_login:
            msg.showinfo("SUCESS", "Welcome Admin")
            dash()
        else:
            if result_register:
                msg.showinfo("SUCESS","Welcome Student")
                student()
            else:
                msg.showerror("Error", "Invalid Details")


    clear()

#########################  LOGIN END  ###################################################



###################################   DESIGN START          ##############################

root.title("Log In")
root.geometry("1500x800+0+0")
root.minsize(400,500)
root.iconbitmap('images/logo.ico')
image = Image.open("images/seepicres.jpeg")
image = image.resize((1500,800),Image.ANTIALIAS)
imagetk = ImageTk.PhotoImage(image)
Label(image=imagetk).pack()

frame1 = Frame(root,bg='white')
frame1.place(x=540,y=218,width=420,height=300)

frame2 = Frame(frame1,bg='white')
frame2.place(x=0,y=0,width=420,height=50)

label_login = Label(frame2,text="Login",font="impact 30 italic bold",bg='white',fg='#d77337')
label_login.place(x=140)

label_email = Label(frame1,text="UserName:",fg="black",bg="white",font=("Goudy old style", 22, "bold"))
label_email.place(x=5,y=70)

############################  ENTRY FOR USERNAME   ########################################
entry_user = Entry(frame1,fg='black',bg='lightgray',textvariable=username_user,font=("Helvetica", 16))
entry_user.place(x=5,y=110,width=370,height=30)
############################  ENTRY FOR USERNAME END    ########################################


password_user = Label(frame1,text="Password:",fg="black",bg="white",font=("Goudy old style", 22, "bold"))
password_user.place(x=5,y=150)

############################  ENTRY FOR PASSWORD   ########################################
entry_password = Entry(frame1,fg='black',bg='lightgray',textvariable=password_pass,font=("Helvetica", 16))
entry_password.place(x=5,y=190,width=370,height=30)
############################  ENTRY FOR PASSWORD   ########################################

forget_btn = Button(frame1,text='New User?',bg='white',fg='#d77337',command=signup,bd=0,cursor="hand2",activebackground='black',activeforeground='white',font=("aerial", 13,'bold', 'underline')).place(x=5,y=230)
#############################    LOGIN BUTTON   ############################
login_btn = Button(root,text='Login',bg='#d77337',fg='white',bd=0,width=10,cursor="hand2",command=login,font=("times new roman", 20)).place(x=660,y=490)

    # root.attributes("-alpha",0.8) it will make transparent background
root.mainloop()
