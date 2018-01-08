from Tkinter import *
import tkMessageBox
import shelf
import personalDICT

def go():
     splash.destroy()
     root1=Tk()
     root1.title("My Book Shelf")
     root1.state("zoomed")
     root1.configure(background='aliceblue')

     n=StringVar()

     def about():
          tkMessageBox.showinfo("Creator","Mrigank Singh - 161B124")

     def  but ():
          s=n.get()
          if  s=="":
              tkMessageBox.showerror("!!!", "Enter Your Name")
              return
          v1=int(v.get()) 
          if  v1==0:
              tkMessageBox.showerror("!!!", "Select your Choice")
          if  v1==1:
               root1.destroy()
               shelf.win1(s)
          if  v1==2:
               root1.destroy()
               personalDICT.dictio(s)

     v=IntVar()

     fr1=Frame(root1,height=400,width=400,bg='royalblue')
     fr1.place(relx=.37,rely=.25)

     Label(fr1,text="My Book Shelf",font="Arial 30 bold underline",fg='aliceblue',bg='royalblue').place(relx=.15,rely=.1)
     Label(fr1,text="Enter Your Name",font='Arial 10 bold',bg='royalblue').place(relx=.37,rely=.3)

     name=Entry(fr1,bd=4,width=15,font='Arial 15',justify='center',textvariable=n).place(relx=.29,rely=.37)

     Radiobutton(fr1,text='Book Shelf',font='Arial 10 bold',bg='royalblue',variable=v,value=1).place(relx=.39,rely=.5)

     Radiobutton(fr1,text='My word space',font='Arial 10 bold',bg='royalblue',variable=v,value=2).place(relx=.39,rely=.55)

     Button(fr1,text="Enter Shelf",bd=5,height=2,width=15,command=but).place(relx=.365,rely=.65)
     Button(fr1,text="About Creator",relief='flat',bd=3,bg='royalblue',height=1,width=15,command=about).place(relx=.365,rely=.8)

     mainloop()

splash=Tk()
splash.attributes("-fullscreen",True)
img=PhotoImage(file="splash1.gif")
spla=Label(splash,image=img)
spla.pack()
spla.after(5000,go)
splash.mainloop()
