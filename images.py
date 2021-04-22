import tkinter
from PIL import Image,ImageTk
root=tkinter.Tk()

root.geometry("1300x244")
photo=tkinter.PhotoImage(file='logo1.png')

#FOR JPG IMAGES
# image=Image.open("shoe.jpg")
# photo=ImageTk.PhotoImage(image)

label=tkinter.Label(image=photo)
label.pack()


root.mainloop()