
from tkinter import Toplevel
from tkinter import *
from tkinter import messagebox as msg

from PIL import Image,ImageTk
import mysql.connector
import re
#########################################  BUTTON LOGIN ########################################
def register():
     pattern = regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
     name = label_name_entry.get()
     username = label_user_entry.get()
     password = label_password_entry.get()
     gender = genderval.get()
     contact = label_contact_entry.get()
     dropdown= variabledropdown.get()
     pattern = '^\S+@\S+$'

# if name.strip()=="" or username.strip()=='' or password.strip()=='' or contact.strip()=='':
#      msg.showerror("fuck","fuck you")
# else:


     if name.strip()!='':
          if re.search(pattern, username):
               if username.strip()!='':
                    if password.strip()!='':
                         if gender.strip()!='':
                              if contact.strip()!='':
                                   if dropdown.strip()!='':


                                        try:
                                             con = mysql.connector.connect(host='localhost',user='root',password='',database='library')
                                             concommand = con.cursor()
                                             concommand.execute("insert into register(name,username,password,gender,contact,stream)values('{}','{}','{}','{}','{}','{}')".format(name,username,password,gender,contact,dropdown))
                                             con.commit()
                                             msg.showinfo("Sucess","Registered Sucessfully")
                                        except:
                                             msg.showerror("Error","UserName is already registered")


                                   else:
                                        print("error")
                              else:
                                   label_three.set("*Contact Cannot Be Empty")
                         else:
                              print("gender")
                    else:
                         label_two.set("*Password Cannot Be Empty")
               else:
                    print("usename")
          else:
               msg.showerror("Error","Invalid EmailId")
               sign.focus()

     else:
          label_one.set("*Name Cannot Be Empty")

     if name=="":
          pass
     else:
          label_one.set("")

     if password=="":
          pass
     else:
          label_two.set("")

     if contact=="":
          pass
     else:
          label_three.set("")



#########################################  BUTTON LOGIN END  ########################################

def signup():
     global sign
     sign = Toplevel()
     sign.title("Registration Form")
     sign.iconbitmap('images/logo.ico')
     sign.geometry("1500x800+0+0")

    ################################ VARIABLE FOR ENTRIES DROP DOWN AND RADIO BUTTONS ######################


    ################################## VARIABLE FOR ENTRIES DROP DOWN AND RADIO BUTTONS ######################


     ####################################    BACKGROUND IMAGE ##########################
     # bg_picture = ImageTk.PhotoImage(file = "images/seeba.jpg")
     # label = Label(sign,image = bg_picture)
     # label.pack()
     sign.configure(bg='lightgrey')
     ####################################    BACKGROUND IMAGE ##########################
     global label_one
     global label_two
     global label_three

     label_one=StringVar()
     label_two=StringVar()
     label_three=StringVar()

     label_val_name = Label(sign,textvariable=label_one,fg='red',bg='lightgrey',font="calibiri 14 bold italic")
     label_val_name.place(x=605,y=120)

     label_val_password = Label(sign,textvariable=label_two,fg='red',bg='lightgrey',font="calibiri 14 bold italic")
     label_val_password.place(x=605,y=120)

     label_val_contact = Label(sign,textvariable=label_three,fg='red',bg='lightgrey',font="calibiri 14 bold italic")
     label_val_contact.place(x=605,y=120)
     #####################################   first main frame start########################
     frame_main = Frame(sign,bg='white')
     frame_main.place(x=480,y=180,width=430,height=400)
     #####################################   first main frame end  ########################

     #####################################  registration heading start  #################
     label_heading = Label(frame_main,text = "Registration Form",bg='white',fg='green',font=("Goudy old style", 30, "bold","italic"))
     label_heading.place(x=0,y=0,width=410,height=50)
     #####################################  registration heading END #################

     ####################################### LABEL AND ENTRIES FOR NAME ############################
     label_name = Label(frame_main,text = 'Name:',bg='white',fg='black',font=("Goudy old style", 20, "bold"))
     label_name.place(x=5,y=58)
     global label_name_entry
     label_name_entry = Entry(frame_main,bg='lightgray',fg='black',font=("Helvetica", 16))
     label_name_entry.place(x=125,y=65,width=260,height=25)
     ####################################### LABEL AND ENTRIES FOR NAME ############################

     ####################################### LABEL AND ENTRIES FOR UserName ############################

     label_user = Label(frame_main,text = 'UserName:',bg='white',fg='black',font=("Goudy old style", 18, "bold"))
     label_user.place(x=5,y=110)
     global label_user_entry
     label_user_entry = Entry(frame_main,bg='lightgray',fg='black',font=("Helvetica", 16))
     label_user_entry.place(x=125,y=117,width=260,height=25)
     ####################################### LABEL AND ENTRIES FOR UserName ############################

     ####################################### LABEL AND ENTRIES FOR PASSWORD ############################

     label_password = Label(frame_main,text = 'Password:',bg='white',fg='black',font=("Goudy old style", 20, "bold"))
     label_password.place(x=5,y=162)
     global label_password_entry
     label_password_entry = Entry(frame_main,bg='lightgray',fg='black',font=("Helvetica", 16))
     label_password_entry.place(x=125,y=169,width=260,height=25)
     ####################################### LABEL AND ENTRIES FOR PASSWORD ############################

     ####################################### LABEL AND RADIO BUTTONS OF GENDER ############################
     label_gender = Label(frame_main,text = 'Gender:',bg='white',fg='black',font=("Goudy old style", 20, "bold"))
     label_gender.place(x=5,y=214)
     global genderval
     genderval=StringVar()
     male_radio = Radiobutton(frame_main,text="Male",value="Male",variable = genderval,fg='black',bg='white',font=("Helvetica", 15))
     male_radio.place(x=120,y=218)

     female_radio = Radiobutton(frame_main,text="Female",value="Female",variable = genderval,fg='black',bg='white',font=("Helvetica", 15))
     female_radio.place(x=240,y=218)
     ####################################### LABEL AND RADIO BUTTONS OF GENDER ############################

     ####################################### LABEL AND ENTRIES FOR CONTACT ############################
     label_contact = Label(frame_main,text = 'Contact:',bg='white',fg='black',font=("Goudy old style", 20, "bold"))
     label_contact.place(x=5,y=267)
     global label_contact_entry
     label_contact_entry = Entry(frame_main,bg='lightgray',fg='black',font=("Helvetica", 16))
     label_contact_entry.place(x=125,y=273,width=260,height=25)
     ####################################### LABEL AND ENTRIES FOR CONTACT ############################

     ####################################### LABEL AND DROP DOWN FOR STREAM ############################

     label_contact = Label(frame_main,text = 'Stream:',bg='white',fg='black',font=("Goudy old style", 20, "bold"))
     label_contact.place(x=5,y=325)

     options = ["Computer",
                "Science",
                "Commerce"]
     global variabledropdown
     variabledropdown=StringVar()
     variabledropdown.set(options[0])
     w=OptionMenu(frame_main,variabledropdown,*options)
     w.place(x=125, y=331, width=260, height=25)


     ####################################### LABEL AND DROP DOWN FOR STREAM ############################

     button_register = Button(sign,text = "Register",bg='green',fg='white',command = register,width=10,cursor="hand2",font=("calibiri", 20, "bold"))
     button_register.place(x=600,y=560)

     # button_login = Button(sign,text='Login',bg='#d77337',fg='white',bd=0,width=9,cursor="hand2",font=("times new roman", 18))
     # button_login.place(x=420,y=540)

     # button_login.place(x=430, y=550)









     sign.mainloop()

