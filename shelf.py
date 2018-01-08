from Tkinter import *
import tkMessageBox
import os
import sqlite3

conn=sqlite3.connect("shelf.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title varchar(30),author varchar(30),year integer(10),isbn integer(20))")

def  win1(s1):
    root=Tk()
    ss=s1
    root.title('Welcome '+ss)
    root.minsize(width=1320,height=800)
    root.configure(background='aliceblue')
    root.state("zoomed")

    
    def  ins():
        if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="":
            tkMessageBox.showinfo("Attention","Fill all the entries.")
        else:
            cur.execute("select * from book where title=(?) OR isbn=(?)",(e2.get(),int(e4.get())))
            rows=cur.fetchall()
            if(len(rows)!=0):
                tkMessageBox.showinfo("Attention !","Entry already EXISTS.")
            else:
                cur.execute("insert into book values(NULL,?,?,?,?)",(e2.get(),e1.get(),int(e3.get()),int(e4.get())))
                tkMessageBox.showinfo("Success.","Book Added to your Shelf.")
                conn.commit ()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

    def  dispall():
        lb.delete(0, END)
        cur.execute("select * from book")
        rows=cur.fetchall()
        if(len(rows)==0):
            tkMessageBox.showinfo("Attention !","Shelf Empty.")
        for i in rows:
            r0=str(i[0])
            r1=str(i[4])
            r2=i[1]
            r3=i[2]
            lb.insert(END,r0+'. '+"ISBN: "+r1+" - "+r2+' by '+r3)

    def disp():
        lb.delete(0, END)
        if e3.get() ==  "":
            yr=0
        else:
            yr=int(e3.get())
        if e4.get()=="":
            isb=0
        else:
            isb=int(e4.get())
        cur.execute("select * from book where title=? OR author=? OR year=? OR isbn=?",(e2.get(),e1.get(),yr,isb))
        rows=cur.fetchall()
        for i in rows:
            r0=str(i[0])
            r1=str(i[4])
            r2=i[1]
            r3=i[2]
            lb.insert(END,r0+'. '+"ISBN : "+r1+" - "+r2+' by '+r3)

    def delete():
        select=lb.get(ACTIVE)
        id1=select[0]+select[1]
        id1=select[0]
        select=lb.curselection()
        lb.delete(select[0])
        cur.execute("delete from book where id=?",(id1,))
        cur.execute("delete from book where id=?",(id1,))
        conn.commit()    

    def back():
        root.destroy()
        os.startfile("start.py")

    Button(root,text="Add Book",bg='royalblue',bd=5,height=2,width=10,command=ins).place(relx=.2,rely=.7)
    Button(root,text="Delete",bg='royalblue',bd=5,height=2,width=10,command=delete).place(relx=.5,rely=.7)    
    Button(root,text="View All",bg='royalblue',bd=5,height=2,width=10,command=dispall).place(relx=.3,rely=.7)
    Button(root,text="Search",bg='royalblue',bd=5,height=2,width=10,command=disp).place(relx=.4,rely=.7)
    Button(root,text="Back",bg='royalblue',bd=5,height=2,width=10,command=back).place(relx=.6,rely=.7)

    fr = Frame(root,height=80,width=2000,bg='royalblue')
    fr.place(rely=.1)
    labelfr=Label(fr,text='Add Book to Your Shelf',font='Arial 30 bold italic',bg='royalblue')
    labelfr.place(relx=.05,rely=.2) 

    label1=Label(root,text='AUTHOR :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
    label1.place(relx=.065,rely=.301)
    e1=Entry(root,bd=4,width=15,font='Arial 15')
    e1.place(relx=.15,rely=.307)

    label2=Label(root,text='TITLE :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
    label2.place(relx=.085,rely=.401)
    e2=Entry(root,bd=4,width=15,font='Arial 15')
    e2.place(relx=.15,rely=.406)
    
    label3=Label(root,text='YEAR :',font='arial 18 bold',bg='aliceblue',fg='royalblue')
    label3.place(relx=.087,rely=.501)
    e3=Entry(root,bd=4,width=15,font='Arial 15')
    e3.place(relx=.15,rely=.506)

    label4=Label(root,text='ISBN :',font='arial 18 bold',bg='aliceblue',fg='royalblue')
    label4.place(relx=.093,rely=.601)
    e4=Entry(root,bd=4,width=15,font='Arial 15')
    e4.place(relx=.15,rely=.606)

    sb=Scrollbar(root,width=20)
    sb.place(relx=.738,rely=.445)
    lb=Listbox(root,height=11,width=60,bd=4,bg='whitesmoke',font="arial 15",yscrollcommand=sb.set)
    lb.place(relx=.301,rely=.3)
    sb.config(command=lb.yview)

    fr1 = Frame(root,height=1000,width=80,bg='royalblue',bd=10)
    fr1.place(relx=.85)
    
    mainloop()
