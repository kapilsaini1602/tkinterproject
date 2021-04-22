# import smtplib
#
# s = smtplib.SMTP('smtp.gmail.com',587)  ###  FOR PORT NUMBER
#
# s.starttls()
#
# To=input("Enter Reciever Mail Address")
# Sub=input("Enter Subject")
# bdy=input("Enter Message")
#
# s.login("kapilsaini4848@gmail.com","8607696626")
#
# message ="Hey How Are You!!"
# subject ="intro"
# mess = 'subject:{}\n\n{}'.format(Sub,bdy)         ### IT WILL ADD SUBJECT..
# #message="HELLO"  it will display only message not subject
#
# s.sendmail("kapilsaini4848@gmail.com",To,mess)
#
# s.quit()
# print("Mail Sent")

import smtplib

s = smtplib.SMTP('smtp.gmail.com',587)  ###  FOR PORT NUMBER

s.starttls()

To=input("Enter Reciever Mail Address")
Sub=input("Enter Subject")
bdy=input("Enter Message")

s.login("kapilsaini4848@gmail.com","8607696626")

message ="Hey How Are You!!"
subject ="intro"
mess = 'subject:{}\n\n{}'.format(Sub,bdy)         ### IT WILL ADD SUBJECT..
#message="HELLO"  it will display only message not subject

s.sendmail("kapilsaini4848@gmail.com",To,mess)

s.quit()
print("Mail Sent")