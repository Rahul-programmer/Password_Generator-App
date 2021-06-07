from tkinter import *
import random
import tkinter.messagebox as msg
root =Tk()
root.geometry("800x500")
root.title("Entry Widget")
def clickMe():
    var=int(Name.get())
    print(var)
    print(type(var))
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    password=""
    if var1.get()==1:
     for x in range (0,var):
            password=password+random.choice(lower)
     msg.showinfo("Your password",f"{password}")
    elif var1.get()==2:
        for x1 in range(0,var):
            password=password+random.choice(upper)
        msg.showinfo("Your password is ",f"{password}")
    elif var1.get()==3:
        for x2  in range(0,var):
            password=password+random.choice(digits)
        msg.showinfo("Your password is ",f"{password}")
    else:
        msg.showinfo("Error","Invalid Options")
Name = StringVar()
var1=IntVar
Name_label= Label(root,text="Enter Your password length:",fg="red",font=("bold",20)).grid(row=0,column=0)
Name_entry=Entry(root,textvariable=Name).grid(row=1,column=0,padx=10,pady=10)
password_strength=Label(root,text="Strength of the password",font=("bold",20)).grid(row=2,column=0)
button=Button(root,text="click me",command=clickMe).grid(row=3,column=1)
low_radiobutton=Radiobutton(root,text="LOW",variable=var1,value=1).grid(row=2,column=1)
medium_radiobutton=Radiobutton(root,text="MEDIUM",variable=var1,value=2).grid(row=2,column=2)
high_radiobutton=Radiobutton(root,text="HIGH",variable=var1,value=3).grid(row=2,column=3)

root.mainloop()