from Tkinter import *
import tkMessageBox
import sqlite3
import os

conn=sqlite3.connect("shelf.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS wor(word varchar(20) PRIMARY KEY,meaning varchar(50))")

def dictio(s1):
    root=Tk()
    ss=s1
    root.title('Welcome '+ss)
    root.state("zoomed")
    root.configure(background='aliceblue')
    
    frq= Frame(root,height=500,width=900,bg='aliceblue')
    frq.place(relx=.1,rely=.3)

    def close():
        root.destroy()
        os.startfile("start.py")

    def back():
        root.destroy()
        dictio(ss)

    def seawo():
        def disp():
            woo1=str(we1.get())
            if we1.get() ==  "":
                tkMessageBox.showinfo("Attention","Enter the Word.") 
            cur.execute("select * from wor where word=?",(we1.get(),))
            rows=cur.fetchall()
            if len(rows)==0:
                tkMessageBox.showinfo("Attention","Not Found.")
            for i in rows:
                woo=i[1]
                tkMessageBox.showinfo(woo1,woo)
        
        frq1= Frame(root,height=500,width=900,bg='royalblue')
        frq1.place(relx=.1,rely=.3)

        Label(frq1,text="Search your Personal Dictionary",font='helvetica 25 bold underline').place(relx=.2,rely=.18)

        Label(frq1,text="Your Word Goes Here",font="times 14 bold",bg='royalblue').place(relx=.38,rely=.39)
        we1=Entry(frq1,bd=4,width=15,font='Arial 15',justify='center')
        we1.place(relx=.39,rely=.46)

        Button(frq1,text="Search",height=2,width=15,command=disp).place(relx=.424,rely=.8)
        Button(frq1,text="X",fg='red',command=back).place(relx=.97,rely=.03)

    def addwo():

        def  ins():
            if we2.get()=="" or we3.get()=="":
                tkMessageBox.showinfo("Attention","Fill all the entries.")  
            else:
                cur.execute("select * from wor where word=(?)",(we2.get(),))
                rows=cur.fetchall()
                if(len(rows)!=0):
                    tkMessageBox.showinfo("Attention !","Entry already EXISTS.")
                else:
                    cur.execute("insert into wor values(?,?)",(we2.get(),we3.get()))
                    tkMessageBox.showinfo("Success.","Word Added to your Dictionary.")
                    conn.commit ()
            we2.delete(0,END)
            we3.delete(0,END)
        
        
        frq2= Frame(root,height=500,width=900,bg='royalblue')
        frq2.place(relx=.1,rely=.3)

        Label(frq2,text="Add words to your Personal Dictionary",font='helvetica 25 bold underline').place(relx=.16,rely=.18)
        
        Label(frq2,text="Your Word Goes Here",font="times 14 bold",bg='royalblue').place(relx=.38,rely=.39)
        we2=Entry(frq2,bd=4,width=15,font='Arial 15',justify='center')
        we2.place(relx=.39,rely=.46)

        Label(frq2,text="This word Stands for",font="times 18 bold",bg='royalblue').place(relx=.365,rely=.594)
        we3=Entry(frq2,bd=4,width=20,font='Arial 15',justify='center')
        we3.place(relx=.36,rely=.66)

        Button(frq2,text="Add",height=2,width=15,command=ins).place(relx=.424,rely=.8)
        Button(frq2,text="X",fg='red',command=back).place(relx=.97,rely=.03)
        

    fr = Frame(root,height=80,width=2000,bg='royalblue')
    fr.place(rely=.1)

    labelfr=Label(fr,text='This  is Your Word Shelf',font='Arial 30 bold italic',bg='royalblue')
    labelfr.place(relx=.1,rely=.2)
    
    fr1 = Frame(root,height=1000,width=80,bg='royalblue',bd=10)
    fr1.place(relx=.85)
    Button(frq,text="Add Word",bd=4,width=15,height=7,font='Arial 15',justify='center',bg='royalblue',command=addwo).place(relx=.2,rely=.3)
    Button(frq,text="Search Word",bd=4,width=15,height=7,font='Arial 15',justify='center',bg='royalblue',command=seawo).place(relx=.6,rely=.3)  
    Button(frq,text="Back",width=10,height=3,bg='royalblue',relief='ridge',bd=5,command=close).place(relx=.453,rely=.54)
    mainloop()
