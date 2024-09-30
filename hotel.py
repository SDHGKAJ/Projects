from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector as sqltor
from PIL import ImageTk
mycon=sqltor.connect(host="localhost",user="root",passwd="root")
mc=mycon.cursor()

mc.execute("create database if not exists myproject10")
mc.execute("use myproject10")
mc.execute("create table if not exists user(name varchar(30),userid int(6) primary key,passwd varchar(20),position varchar(20))")
q1="insert into user(name,userid,passwd,position) values(%s,%s,%s,%s)"
v1=[("Ramki",1001,"Ram01","manager"),("Akshay",1002,"Aks02","manager"),("Balram",1003,"Bal03","staff"),("Manish",1004,"Man04","staff")]
mc.executemany(q1,v1)
mc.execute("create table if not exists customer(name varchar(30),phone int(15),address varchar(50),noofdays int(3),room int(10) primary key,roomtype varchar(20) )")
mc.execute("create table if not exists payment as select name,room,roomtype,noofdays from customer")
mc.execute("alter table payment add fee int")
mc.execute("create table if not exists service(foodtype varchar(30),cuisine varchar(30),price int(6))")
q="insert into service(foodtype,cuisine,price) values (%s,%s,%s)"
v=[("Breakfast","Indian",500),("Breakfast","Italian",750),("Lunch","North Indian",500),("Lunch","South Indian",300),("Lunch","Italian",1000),("Dinner","Indian",500),("Dinner","Italian",750)]
mc.executemany(q,v)

root=Tk()
root.title("Hotel Sacerdote")
root.geometry("1177x615")
root.configure(bg="#00FFFF")
root.resizable(width=False,height=False)
usr=StringVar()
pwd=StringVar()
name=StringVar()
phone=StringVar()
address1=StringVar()
address2=StringVar()
noofdays=StringVar()
roomno=StringVar()
roomtype=StringVar()
khana=StringVar()
mlc=StringVar()
Pri=StringVar()
rtno=StringVar()

BGImage = ImageTk.PhotoImage(file = r"C:\Users\Asus\Downloads\test\hotelbg1.jpg")
BG = Label(root,image = BGImage)
BG.place(x=0,y=0)

def check(rt):
 us=usr.get()
 pw=pwd.get()
 mc.execute('select * from user')
 r=mc.fetchall()
 for i in r:
    us=int(us)
    if i[1]==us and i[2]==pw:
        if i[3]=='manager' or i[3]=='staff' :
            rt.destroy()
            return mainpage()

 else:
      messagebox.showinfo('warning','incorrect username or password')


def rtype(a,ch):
    if a=="Suite":
        return ch*1000
    if a=="Regular":
        return ch*500



def mainpage(*event):

    root1 = Tk()
    root1.title('reservation booking')
    root1.geometry("1022x609")
    root1.configure(bg="#FAD8AD")
    root1.resizable(width=False,height=False)

    BGImage1 = ImageTk.PhotoImage(file = r"C:\Users\Asus\Downloads\test\hall.jpg")
    BG1 = Label(root1,image = BGImage1)
    BG1.place(x=0,y=0)

    newcust=Button(root1,text='New Customer',padx=10,pady=30,height = 1,width = 10,bg='#FFD58F',fg='black',command=lambda:booking(root1))
    newcust.place(x=300,y=50)
    newcust.tkraise()
    detail=Button(root1,text='Room Details',padx=10,pady=30,height = 1,width = 10,bg='#FFD58F',fg='black',command=lambda:details(root1))
    detail.place(x=600,y=50)
    detail.tkraise()
    payment=Button(root1,text='Check Out',padx=10,pady=30,height = 1,width = 10,bg='#FFD58F',fg='black',command=lambda:pay(root1))
    payment.place(x=300,y=350)
    payment.tkraise()
    display1=Button(root1,text='Staff Details',padx=10,pady=30,height = 1,width = 10,bg='#FFD58F',fg='black',command=lambda:display(root1))
    display1.place(x=600,y=350)
    display1.tkraise()
    roomsv=Button(root1,text='Room Service',padx=10,pady=30,height = 1,width = 10,bg='#FFD58F',fg='black',command=lambda:rservice(root1))
    roomsv.place(x=465,y=200)
    roomsv.tkraise()

    root1.mainloop()




def booking(r):
    def submit(rt):
        na=l1.get()

        ph=l2.get()
        p=int(ph)
        a1=l3.get()
        a2=l4.get()
        ad=a1+a2
        che=l5.get()
        ch=int(che)
        rn=l6.get()
        r=int(rn)
        ty=l7.get()
        f=rtype(ty,ch)

        q2="insert into customer(name,phone,address,noofdays,room,roomtype) values(%s,%s,%s,%s,%s,%s)"

        q3="insert into payment(name,room,roomtype,noofdays,fee) values(%s,%s,%s,%s,%s)"

        v2=(na,p,ad,ch,r,ty)
        v3=(na,r,ty,ch,f)
        mc.execute(q2,v2)
        mc.execute(q3,v3)
        mycon.commit()
        rt.destroy() 


    root2=Tk()
    root2.geometry("1100x1100")
    root2.configure(bg="#FAD8AD")
    root2.resizable(width=False,height=False)
    x0=Label(root2,text='CUSTOMER DETAILS',font=('arial',14),bg='#FFFF80')
    x0.place(x=450,y=110)
    x1=Label(root2,text='NAME',font=('arial',14),bg='#FFFF80')
    x1.place(x=395,y=210)
    x2=Label(root2,text='PHONE NUMBER',font=('arial',14),bg='#FFFF80')
    x2.place(x=395,y=260)
    x3=Label(root2,text='ADDRESS(in 2 lines)',font=('arial',14),bg='#FFFF80')
    x3.place(x=395,y=310)
    x4=Label(root2,text='NO OF DAYS',font=('arial',14),bg='#FFFF80')
    x4.place(x=395,y=410)
    x5=Label(root2,text='ROOM-NO',font=('arial',14),bg='#FFFF80')
    x5.place(x=395,y=460)
    x6=Label(root2,text='ROOM TYPE',font=('arial',14),bg='#FFFF80')
    x6.place(x=395,y=510)
    x7=Label(root2,text='(Suite/Regular)',font=('arial',10),bg='#FFFF80')
    x7.place(x=395,y=530)

    l1=Entry(root2,width=20,bd=3,textvariable=name,font=('arial',14),bg='#FFFF80')
    l1.place(x=610,y=210)
    l2=Entry(root2,width=20,bd=3,textvariable=phone,font=('arial',14),bg='#FFFF80')
    l2.place(x=610,y=260)
    l3=Entry(root2,width=20,bd=3,textvariable=address1,font=('arial',14),bg='#FFFF80')
    l3.place(x=610,y=310)
    l4=Entry(root2,width=20,bd=3,textvariable=address2,font=('arial',14),bg='#FFFF80')
    l4.place(x=610,y=360)
    l5=Entry(root2,width=20,bd=3,textvariable=noofdays,font=('arial',14),bg='#FFFF80')
    l5.place(x=610,y=410)
    l6=Entry(root2,width=20,bd=3,textvariable=roomno,font=('arial',14),bg='#FFFF80')
    l6.place(x=610,y=460)
    l7=Entry(root2,width=20,bd=3,textvariable=roomtype,font=('arial',14),bg='#FFFF80')
    l7.place(x=610,y=510)

    back=Button(root2,text='Entry',padx=40,pady=20,height = 1,width = 5,bg='#FFD58F',fg='black',command=lambda:submit(root2))
    back.place(x=620,y=570)



def details(r):

    root2=Tk()
    root2.geometry("1000x1000")
    frame=Frame(root2,height=700,width=1000,bg='#d3d3d3')
    frame.place(x=0,y=0)
    mc.execute('select * from customer')
    r1=mc.fetchall()

    listBox=Text(root2,height = 38, width = 155,fg="white",bg="blue",font="Helvetica")
    listBox.grid(row = 2,column= 0, columnspan = 2)
    listBox.insert(END, "  \t\t\t Customer information\t\t\n\n")
    listBox.insert(END," ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    listBox.insert(END,"\tName\t\tPhone\t\tAddress\t\t\t\tNo of days\t\tRoom no\t\tRoom Type\n")
    listBox.insert(END," -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    for i in r1:
        listBox.insert(END,"\t")
        listBox.insert(END,i[0])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[1])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[2])
        listBox.insert(END,"\t\t\t\t")
        listBox.insert(END,i[3])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[4])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[5])
        listBox.insert(END,"\n\n")
        listBox.insert(END," ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")


def stype(a,ch,ch1):
    mc.execute('select * from service where foodtype = "{}"'.format(a.split()[0]))
    r1=mc.fetchall()
    if len(r1) != 0:
        mc.execute('update payment set fee={}+fee where room={}'.format(ch,ch1))    
        messagebox.showinfo('ON THE WAY','ON THE WAY')       
    else:
        messagebox.showinfo('warning','invalid input')


def rservice(r):
    root2=Tk()
    root2.geometry("1200x1200")
    frame=Frame(root2,height=700,width=1000,bg='#d3d3d3')
    frame.place(x=0,y=0)

    mc.execute('select * from service')
    r1=mc.fetchall()
    listBox=Text(root2,height = 38, width = 155,fg="white",bg="blue",font="Helvetica")
    listBox.grid(row = 2,column= 0, columnspan = 5)
    listBox.insert(END, "  \t\t\t Service \t\t\n\n")
    listBox.insert(END," --------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    listBox.insert(END,"\tMeal\t\tCuisine\t\tPrice\n")
    listBox.insert(END," ----------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    for i in r1:
        listBox.insert(END,"\t")
        listBox.insert(END,i[0])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[1])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[2])
        listBox.insert(END,"\n\n")
        listBox.insert(END," ----------------------------------------------------------------------------------------------------------------------------------------\n\n")

    y=Label(root2,text='Meal and cuisine',font=('arial',12))
    y.place(x=800,y=600)
    z=Entry(root2,textvariable=khana,font=('arial',12))
    z.place(x=940,y=600)
    y1=Label(root2,text='Price',font=('arial',12))
    y1.place(x=800,y=625)
    z1=Entry(root2,textvariable=Pri,font=('arial',12))
    z1.place(x=940,y=625)
    y2=Label(root2,text='Room no',font=('arial',12))
    y2.place(x=800,y=650)
    z2=Entry(root2,textvariable=rtno,font=('arial',12))
    z2.place(x=940,y=650)

    #v=int(v)
    #v1=int(v1)
    B1 = Button(root2,text = "Confirm",command = lambda:stype(z.get(),z1.get(),z2.get()))
    B1.place(x=995,y=675)




def pay(r):
    root2=Tk()
    root2.geometry("1000x1000")
    frame=Frame(root2,height=700,width=1000,bg='#d3d3d3')
    frame.place(x=0,y=0)
    mc.execute('select * from payment')
    r1=mc.fetchall()

    listBox=Text(root2,height = 38, width = 155,fg="white",bg="blue",font="Helvetica")
    listBox.grid(row = 2,column= 0, columnspan = 5)
    listBox.insert(END, "  \t\t\t Check out \t\t\n\n")
    listBox.insert(END," --------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    listBox.insert(END,"\tName\t\tRoom\t\tRoom Type\t\tNo of days\t\tFee\n")
    listBox.insert(END," ----------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    for i in r1:
        listBox.insert(END,"\t")
        listBox.insert(END,i[0])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[1])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[2])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[3])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[4])
        listBox.insert(END,"\n\n")
        listBox.insert(END," ----------------------------------------------------------------------------------------------------------------------------------------\n\n")


    e=Label(root2,text = "Select Room Number",font=('arial',15))
    e.place(x=200,y=500)
    E1 = Entry(root2,font=('arial',14))
    E1.place(x=400,y=500)
    B1 = Button(root2,height = 2,width = 15,text = "Confirm",command = lambda: remove(E1.get(),root2))
    B1.place(x=400,y=550)


def remove(x,rt):
    mc.execute("delete from payment where room = {}".format(int(x)))
    mc.execute("delete from customer where room = {}".format(int(x)))
    rt.destroy()
    mycon.commit()


def display(r):
    root2 = Tk()
    root2.geometry("1190x650")
    root2.configure(bg="#FAD8AD")
    root2.resizable(width=False,height=False)


    m=Label(root2,text='#ONLY MANAGERS CAN ACCESS',font=('Algerian',30,'bold'),bg='#FAD8AD')
    m.place(x=220,y=100)
    m.tkraise()
    h=Button(root2,text='STAFF',padx=30,pady=30,height = 1,width = 5,bg='#FFD58F',fg='black',command=lambda:staff(root2))
    h.place(x=720,y=420)
    h.tkraise()
    b1=Label(root2,text='USERID',font=('arial',14,),bg='#d3d3d3')
    b1.place(x=395,y=400)
    b1.tkraise()
    a2=Entry(root2,width=20,bd=3,textvariable=usr,font=('arial',13))
    a2.place(x=510,y=400)
    a2.tkraise()
    b2=Label(root2,text='PASSWORD',font=('arial',14),bg='#d3d3d3')
    b2.place(x=390,y=500)
    b2.tkraise()
    a3=Entry(root2,width=20,bd=3,textvariable=pwd,show='*',font=('arial',13))
    a3.place(x=510,y=500)
    a3.tkraise()
    login=Button(root2,text='Login',height = 2,width = 14,bg='#D59949',fg='black',command=lambda:check1(root2))
    login.place(x=540,y=550)
    login.tkraise()

    root2.mainloop()


def check1(rt):
 us=usr.get()
 pw=pwd.get()
 mc.execute('select * from user')
 r=mc.fetchall()
 for i in r:
    us=int(us)
    if i[1]==us and i[2]==pw:
        if i[3]=='manager' or i[3]=='staff' :
            rt.destroy()
            return manager()

 else:
      messagebox.showinfo('warning','incorrect username or password')


def staff(r):
    root3=Tk()
    root3.geometry("1000x1000")
    frame=Frame(root3,height=700,width=1000,bg='#d3d3d3')
    frame.place(x=0,y=0)

    mc.execute('select* from user')
    r1=mc.fetchall()
    listBox=Text(root3,height = 38, width = 155,fg="white",bg="black",font="Helvetica")
    listBox.grid(row = 2,column= 0, columnspan = 5)
    listBox.insert(END, "  \t\t\t Staff details \t\t\n\n")
    listBox.insert(END," --------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    listBox.insert(END,"\tName\t\tUserid\t\tPosition\n")
    listBox.insert(END," ----------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    for i in r1:
        listBox.insert(END,"\t")
        listBox.insert(END,i[0])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[1])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[3])
        listBox.insert(END,"\n\n")
        listBox.insert(END," ----------------------------------------------------------------------------------------------------------------------------------------\n\n")

def manager(*event):
    root3=Tk()
    root3.geometry("1000x1000")
    frame=Frame(root3,height=700,width=1000,bg='#d3d3d3')
    frame.place(x=0,y=0)
    mc.execute('select* from user')
    r1=mc.fetchall()
    listBox=Text(root3,height = 38, width = 155,fg="white",bg="black",font="Helvetica")
    listBox.grid(row = 2,column= 0, columnspan = 5)
    listBox.insert(END, "  \t\t\t Staff details \t\t\n\n")
    listBox.insert(END," --------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    listBox.insert(END,"\tName\t\tUserid\t\tPassword\t\tPosition\n")
    listBox.insert(END," ----------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    for i in r1:
        listBox.insert(END,"\t")
        listBox.insert(END,i[0])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[1])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[2])
        listBox.insert(END,"\t\t")
        listBox.insert(END,i[3])
        listBox.insert(END,"\n\n")
        listBox.insert(END," ----------------------------------------------------------------------------------------------------------------------------------------\n\n")


wc=Label(root,text='Welcome to Hotel Sacerdote',font=('Ink Free',30, 'bold'),bg='#FAD8AD',)
wc.place(x=340,y=50)
uid=Label(root,text='USERID',font=('arial',14,),bg='#FAD8AD')
uid.place(x=395,y=210)
a1=Entry(root,width=20,bd=3,textvariable=usr,font=('arial',13))
a1.place(x=510,y=214)
pd=Label(root,text='PASSWORD',font=('arial',14),bg='#FAD8AD')
pd.place(x=390,y=260)
a2=Entry(root,width=20,bd=3,textvariable=pwd,show='*',font=('arial',13))
a2.place(x=510,y=260)
login=Button(root,text='Login',height = 2,width = 14,bg='#D59949',fg='black',command=lambda:check(root))
login.place(x=540,y=310)
root.mainloop()
mc.close()
mycon.close()