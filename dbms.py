# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:36:33 2020

@author: Nitish Pratap
"""
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 
import mysql.connector

root=Tk()
root.title("Toll Management System")
root.geometry("500x500")
root.configure(bg='grey')
#root.bg=PhotoImage(file="niti.png")
heading=Label(root,text="Toll Management System",font=( 'aria' ,30, 'bold' ),bg='red',width=1600,bd=20)
global text1,text2


                    #deleting from column by driver name


def del_(top):
    text_=e10.get()
    print(text_)
    mydb=mysql.connector.connect(host='localhost',user='root',password='@Mn967055',database='toll')
    cur=mydb.cursor()
    s="DELETE FROM toll WHERE driver='%s' "%(text_)
    cur.execute(s)
    mydb.commit()
    
    
    #mydb=mysql.connector.connect(host='localhost',user='root',password='@Mn967055',database='toll')
    #cur=mydb.cursor()
   # name_search=input("Print inter the name you want to search  :")
    
    #up="SELECT * FROM toll WHERE driver LIKE '%s' "%name_search
    #cur.execute(up)
    #res=cur.fetchone()
    #new=Toplevel()
    #for row in res:
        #new=Toplevel()
        #newlevel=Label(new,text=row)
     #   print(row)
    #mydb.commit()
    
    
    #mydb=mysql.connector.connect(host='localhost',user='root',password='@Mn967055',database='toll')
    #cur=mydb.cursor()
    #name_search=input("Print inter the name you want to search  :")
    
    #up="SELECT * FROM toll WHERE driver LIKE '%s' "%name_search
    #cur.execute(up)
    #res=cur.fetchone()
    #new=Toplevel()
    #for row in res:
        #new=Toplevel()
        #newlevel=Label(new,text=row)
     #   print(row)
    #mydb.commit()
    
    
    
    
    
    

                        #deleting from column by driver name
                        
                        
def del_by_dl(top):
    text_=e11.get()
    print(text_)
    mydb=mysql.connector.connect(host='localhost',user='root',password='@Mn967055',database='toll')
    cur=mydb.cursor()
    s="DELETE FROM toll WHERE driver_dl='%s' "%(text_)
    cur.execute(s)
    mydb.commit()

                    #updating price

def update(top):
    
    mydb=mysql.connector.connect(host='localhost',user='root',password='@Mn967055',database='toll')
    cur=mydb.cursor()
    global z
    z=IntVar()
    
    z=int(e.get())
    s="UPDATE toll SET price=price+'%d' " %(z)
    cur.execute(s)
    mydb.commit()

                        #submit button
                        
                        
                        
def final_submit(top):
    global vahi
    vahi=e5.get()
    total=IntVar()
    total=0
    if(vahi=="car"):
        total=50
    if(vahi=="bus"):
        total=80
    if(vahi=="bike"):
        total=30
    if(vahi=="ViP"):
        total=0
    if(vahi=="truck"):
        total=100
    if(vahi=="other"):
        total=100
    
                       #creating Database
                       
                       
    money=Label(top,text="Total", anchor='s',padx=25,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=580,y=550)
    temp=Label(top,text=total,anchor='s',padx=25,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=660,y=550)
    #e8=Entry(top,width=30,borderwidth=3,bg='grey')
    #8.insert(0,text=total)
    #e8.place(x=630,y=650)
    mydb=mysql.connector.connect(host='localhost',user='root',password='@Mn967055',database='toll')
    cur=mydb.cursor()
#cur.execute("CREATE DATABASE toll")
#s="CREATE TABLE plaza(driver text,driver_dl text,vehicle text,vehicle_number text,date text,time text,price integer,going_toward text) "
    s="INSERT INTO toll(driver,driver_dl,vehicle,vehicle_number,date ,time ,price ,going_toward ) values(%s, %s, %s, %s, %s, %s, %s, %s)"
    #b1=("Nitish","12345","car","7071","28/11/2020","12:00",30,"Delhi")
    #b2=("Ashutosh","47896","bus","7071","28/11/2020","12:00",50,"Delhi")
    
    b3=(e1.get(),e2.get(),e5.get(),e6.get(),e3.get(),e4.get(),total,e7.get())
    #cur.execute(s,b1)
    
    #cur.execute(s,b2)
    cur.execute(s,b3)
    mydb.commit()
    
   
    
    
    mydb.commit()
    mydb=mysql.connector.connect(host='localhost',user='root',password='@Mn967055',database='toll')
    cur=mydb.cursor()
    a="SELECT * from toll"
    cur.execute(a)
    result =cur.fetchall()
    for rec in result:
        print(rec)
   
    
    
    
    
    
    
    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    
    
    
def popup():
    messagebox.showerror("Wrong Password","Try Again")

def open_():
    top=Toplevel()
    top.geometry("1600x1200")
    top.configure(bg='grey')
    
    new_heading=Label(top,text="Toll Management System",font=( 'aria' ,30, 'bold' ),bg='red',width=1600,bd=20).pack()
    sec_heading=Label(top,text="Kanpur-Delhi Expressway",font=( 'aria' ,20, 'bold' ),bg='red',width=75,bd=20).place(x=10,y=100)
    
    
    global e1
    userid=Label(top,text="Driver Name", anchor='s',padx=20,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=50,y=250)
    e1=Entry(top,width=40,borderwidth=3,bg='grey')
    
    
    
    
    e1.insert(0,"Enter Driver Name")
    e1.place(x=200,y=252)
    
    global e2
    dl_number=Label(top,text="Driver DL Number ", anchor='s',padx=20,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=800,y=250)
    e2=Entry(top,width=40,borderwidth=3,bg='grey')

    e2.insert(0,"Enter DL number")
    e2.place(x=1000,y=252)
    #mylabel=Label(top,text="",font=("Helvetica",48),fg='green').place(x=300,y=300)
    
    global e3
    date=Label(top,text="Date", anchor='s',padx=50,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=50,y=300)
    e3=Entry(top,width=40,borderwidth=3,bg='grey')
    e3.insert(0,"Enter Date")
    e3.place(x=200,y=302)
    
    global e4
    time=Label(top,text="Time", anchor='s',padx=73,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=800,y=300)
    e4=Entry(top,width=40,borderwidth=3,bg='grey')
    e4.insert(0,"Enter Time")
    e4.place(x=1000,y=302)
    
    vehicle=Label(top,text="Vehicle Type", anchor='s',padx=18,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=50,y=350)
    global e5
    e5=Entry(top,width=40,borderwidth=3,bg='grey')
    e5.insert(0,"car \ bus \ truck \ vip \ bike \other")
    e5.place(x=200,y=352)
    
    global e6
    vehicle_number=Label(top,text="Vehicle Number", anchor='s',padx=30,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=800,y=350)
    e6=Entry(top,width=40,borderwidth=3,bg='grey')
    e6.insert(0,"UP 60 AE1020")
    e6.place(x=1000,y=352)
    
    global e7
    going_toward=Label(top,text="Going Toward", anchor='s',padx=18,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove").place(x=550,y=400)
    e7=Entry(top,width=30,borderwidth=3,bg='grey')
    e7.insert(0,"Kanpur \  Delhi")
    e7.place(x=530,y=430)
    
    submit=Button(top,text="Submit",anchor='s',padx=100,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='green',borderwidth=4, relief="groove",command=lambda:final_submit(top)).place(x=500,y=495)
    
    
    
    
    update_button=Button(top,text="Update Tax", anchor='s',padx=20,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove",command=lambda:update(top)).place(x=125,y=525)
    global e
    e=IntVar()
    e=Entry(top,width=40,borderwidth=3,bg='grey')
    e.place(x=75,y=495)
    
    delete_by_driver_button=Button(top,text="Delete by driver", anchor='s',padx=20,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove",command=lambda:del_(top)).place(x=900,y=525)
    global e10
    e10=Entry(top,width=40,borderwidth=3,bg='grey')
    e10.place(x=855,y=495)
    
    delete_by_driver_button=Button(top,text="Delete by driver DL", anchor='s',padx=20,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove",command=lambda:del_by_dl(top)).place(x=570,y=600)
    global e11
    
    e11=Entry(top,width=40,borderwidth=3,bg='grey')
    e11.place(x=540,y=640)
    
   

    



def signin(root):
    text1=e1.get()
    text2=e2.get()
    if(text1=="" and text2==""):
        messagebox.showerror("Error","all field are required")
    if(text1=="admin" and text2=="12345"):
        
        open_()
        
    else:
        messagebox.showerror("Error","Invalid Username/Password")
    



heading.pack()
login=Label(root,text="Login  Here", anchor='s',padx=175,pady=10,font=( 'aria' ,15, 'bold' ),fg="green",bg="blue",borderwidth=2, relief="groove").place(x=20,y=125)

im_=ImageTk.PhotoImage(Image.open("niti.png"))
lab=Label(root,image=im_).pack()

#dis=Label(root,text="employee login panel", anchor='s',padx=175,pady=5,font=( 'aria' ,15, 'bold' ),fg="black").place(x=20,y=200)
userid=Label(root,text="username", anchor='s',padx=10,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='red',borderwidth=3, relief="groove").place(x=100,y=250)
e1=Entry(root,width=20,borderwidth=3,bg='white')

e1.insert(0,"admin")
e1.place(x=205,y=251)

password=Label(root,text="password", anchor='s',padx=10,pady=0,font=( 'aria' ,12, 'bold' ),fg="blue",bg='red',borderwidth=3, relief="groove").place(x=100,y=300)
e2=Entry(root,width=20,borderwidth=3,bg='white')
e2.insert(1,"12345")
e2.place(x=205,y=300)
#login.pack()

b=Button(root,text="signin",padx=30,font=( 'aria' ,12, 'bold' ),fg="blue",bg='grey',borderwidth=3, relief="groove",command=lambda:signin(root)).place(x=160,y=340)

root.mainloop()
