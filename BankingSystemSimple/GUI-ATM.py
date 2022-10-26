import tkinter as tk
from tkinter import *
from tkinter import messagebox
from time import gmtime, strftime
'''import subprocess
import sys'''
import tkinter.font as tkFont
from PIL import ImageTk,Image


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
    try:
        fpin=open(num+".txt",'r')
    except FileNotFoundError:
        messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
        return 0
    fpin.close()
    return 

def home_return(master):
    master.destroy()
    Main_Menu()

def write(master,name,oc,pin):
    
    if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return 

    f1=open("Accnt_Record.txt",'r')
    accnt_no=int(f1.readline())
    accnt_no+=1
    f1.close()

    f1=open("Accnt_Record.txt",'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet=open(str(accnt_no)+".txt","w")
    fdet.write(pin+"\n")
    fdet.write(oc+"\n")
    fdet.write(str(accnt_no)+"\n")
    fdet.write(name+"\n")
    fdet.close()

    frec=open(str(accnt_no)+"-rec.txt",'w')
    frec.write("Date                                                     Credit                         Debit                          Balance"+"\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]",gmtime()))+"                         "+oc+"                         "+oc+'\n')
    frec.close()

    messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
    master.destroy()
    return

def crdt_write(master,amt,accnt,name):

    

    if(is_number(amt)==0):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return 

    fdet=open(accnt+".txt",'r')
    pin=fdet.readline()
    camt=int(fdet.readline())
    fdet.close()
    amti=int(amt)
    cb=amti+camt
    fdet=open(accnt+".txt",'w')
    fdet.write(pin)
    fdet.write(str(cb)+"\n")
    fdet.write(accnt+"\n")
    fdet.write(name+"\n")
    fdet.close()
    frec=open(str(accnt)+"-rec.txt",'a+')
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S] ",gmtime()))+"                     "+str(amti)+"                                                              "+str(cb)+"\n")
    frec.close()
    messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
    master.destroy()
    return

def debit_write(master,amt,accnt,name):

    if(is_number(amt)==0):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return 
            
    fdet=open(accnt+".txt",'r')
    pin=fdet.readline()
    camt=int(fdet.readline())
    fdet.close()
    if(int(amt)>camt):
        messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
    else:
        amti=int(amt)
        cb=camt-amti
        fdet=open(accnt+".txt",'w')
        fdet.write(pin)
        fdet.write(str(cb)+"\n")
        fdet.write(accnt+"\n")
        fdet.write(name+"\n")
        fdet.close()
        frec=open(str(accnt)+"-rec.txt",'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"                                                 "+str(amti)+"                          "+str(cb)+"\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
        master.destroy()
        return

def Cr_Amt(accnt,name):

    creditwn=tk.Tk()
    creditwn.geometry("600x300")
    
    creditwn.resizable(False, False)
    window_height = 500
    window_width = 900
    screen_width = creditwn.winfo_screenwidth()
    screen_height = creditwn.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    creditwn.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    creditwn.title("Credit Amount")
    creditwn.configure(bg="#b3b3ff")
    fr1=tk.Frame(creditwn,bg="black")
    l_title=tk.Message(creditwn,text="BANK",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="white",justify="center",anchor="center")
    l_title.config(font=("simsun","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be credited: ")
    e1=tk.Entry(creditwn,relief="raised",bd=4)
    l1.pack(pady=7,side="top")
    e1.pack(pady=10,side="top")
    creditwn.after(1,lambda: creditwn.focus_force())
    e1.focus_set()
    b=tk.Button(creditwn,text="Credit",relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
    b.pack(side="top")
    creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


def De_Amt(accnt,name):
    debitwn=tk.Tk()
    debitwn.geometry("600x300")

    debitwn.resizable(False, False)
    window_height = 500
    window_width = 900
    screen_width = debitwn.winfo_screenwidth()
    screen_height = debitwn.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    debitwn.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    debitwn.title("Debit Amount")   
    debitwn.configure(bg="#b3b3ff")
    fr1=tk.Frame(debitwn,bg="black")
    l_title=tk.Message(debitwn,bd=4,text="BANK",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="white",justify="center",anchor="center")
    l_title.config(font=("simsun","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(debitwn,relief="raised",text="Enter Amount to be debited: ")
    e1=tk.Entry(debitwn,relief="raised",bd=4)
    e1.focus_set()
    l1.pack(pady=7,side="top")
    e1.pack(pady=10,side="top")
    debitwn.after(1,lambda: debitwn.focus_force())
    e1.focus_set()
    b=tk.Button(debitwn,text="Debit",relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
    b.pack(side="top")
    debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))




def disp_bal(accnt):
    fdet=open(accnt+".txt",'r')
    fdet.readline()
    bal=fdet.readline()
    fdet.close()
    messagebox.showinfo("Your Balance",bal)




def disp_tr_hist(accnt):
    disp_wn=tk.Tk()
    disp_wn.geometry("900x600")
    
    disp_wn.resizable(False, False)
    window_height = 700
    window_width = 1300
    screen_width = disp_wn.winfo_screenwidth()
    screen_height = disp_wn.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    disp_wn.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    disp_wn.title("Transaction History")
    fr1=tk.Frame(disp_wn,bg="black")
    frec=open(accnt+"-rec.txt",'r')
    #l1=tk.messagebox.showinfo('Your Transaction History ',frec.read())
    
    for l in frec:
            lk=tk.Message(disp_wn,anchor='w',text=l,width=3000,font=('Times New Roman','15','bold')).pack(side='top')
    frec.close()
    #l_title.pack(side="top")
    '''fr1=tk.Frame(disp_wn)
    fr1.pack(side="top")
    
    fr2=tk.Frame(disp_wn)
    fr2.pack(side="top")
    l=tk.Message(disp_wn,anchor="w",text=lines,relief="raised",width=2000)
    l.pack(side="top")
    b=tk.Button(disp_wn,text="Exit",relief="raised",command=disp_wn.destroy,height=2,width=25,bg='#b3b3ff')
    b.pack(side="top")
    b.place(x=550,y=555)'''
    frec.close()

def logged_in_menu(accnt,name):
    rootwn=tk.Tk()

    photo = PhotoImage(file = "icon.gif")
    rootwn.iconphoto(False, photo)
    
    rootwn.geometry("1600x700")
    rootwn.state('zoomed')
    
    rootwn.title("BANK-"+name)
    rootwn.configure(background='#00004d')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    
    l_title=tk.Message(rootwn,text="BANK\n SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#00004d",justify="center",anchor="center")
    l_title.config(font=("simsun","50","bold"))
    l_title.pack(side="top")
    label=tk.Label(text="Logged in as: "+name,relief="raised",bg="red",fg="white",anchor="center",justify="center")
    label.pack(side="top")

    
    img2=tk.PhotoImage(file="credit.gif")
    myimg2=img2.subsample(4,4)
    img3=tk.PhotoImage(file="debit.gif")
    myimg3=img3.subsample(4,4)
    img4=tk.PhotoImage(file="balance1.png")
    myimg4=img4.subsample(4,4)
    img5=tk.PhotoImage(file="transaction.gif")
    myimg5=img5.subsample(4,4)
    
    b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
    b2.image=myimg2
    b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
    b3.image=myimg3
    b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
    b4.image=myimg4
    b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
    b5.image=myimg5
    
    img6=tk.PhotoImage(file="logout.gif")
    myimg6=img6.subsample(2,2)
    b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
    b6.image=myimg6

    b2.place(x=900,y=200)
    b3.place(x=900,y=320)
    b4.place(x=900,y=440)
    b5.place(x=900,y=560)
    b6.place(x=300,y=325)
    
def logout(master):
    
    messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()

def check_log_in(master,name,acc_num,pin):
    if(check_acc_nmb(acc_num)==0):
        master.destroy()
        Main_Menu()
        return

    if( (is_number(name))  or (is_number(pin)==0) ):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        Main_Menu()
    
    else:
        master.destroy()
        logged_in_menu(acc_num,name)

'''def check_log_in(master,name,accnt,pin):
    f=open(accnt+".txt",'r')
    pn = int(f.readline())
    f.readline()
    acc=int(f.readline())
    nam=str(f.readline())

    if ( (pin==pn) and (accnt==acc) and (name==nam) ):
        master.destroy()
        logged_in_menu(accnt,name)
    
    else:
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        Main_Menu()
        return'''

def log_in(master):
    master.destroy()
    loginwn=tk.Tk()
    loginwn.geometry("1000x600")
    loginwn.resizable(False, False)
    window_height = 500
    window_width = 900
    screen_width = loginwn.winfo_screenwidth()
    screen_height = loginwn.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    loginwn.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    photo = PhotoImage(file = "icon.gif")
    loginwn.iconphoto(False, photo)

    loginwn.title("Log in")
    loginwn.configure(bg="#00004d")
    fr1=tk.Frame(loginwn,bg="#3d3d5c")
    
    l_title=tk.Message(loginwn,text="BANK",relief="raised",width=2000,padx=600,pady=0,fg="#99b3ff",bg="#00004d",justify="center",anchor="center")
    l_title.config(font=("simsun","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(loginwn,text="Enter Name:",relief="raised")
    l1.pack(side="top")

    '''def go_to_next_entry_1(event):
        loginwn.after(1,lambda: loginwn.focus_force())
        e2.focus_set()'''
    
    e1=tk.Entry(loginwn,bd=4)
    loginwn.after(1,lambda: loginwn.focus_force())
    e1.focus_set()
    e1.pack(side="top",pady=10)
    
    l2=tk.Label(loginwn,text="Enter account number:",relief="raised")
    l2.pack(side="top")
    e2=tk.Entry(loginwn,bd=4)
    e2.pack(side="top",pady=10)
    e1.bind('<Return>', lambda e: e2.focus_set())
    
    l3=tk.Label(loginwn,text="Enter your PIN:",relief="raised")
    l3.pack(side="top")
    
    e3=tk.Entry(loginwn,show="*",bd=4)
    e3.pack(side="top",pady=10)
    
    b=tk.Button(loginwn,bd=5,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.pack(side="top")
    
    b1=tk.Button(text="HOME",bd=7,relief="raised",bg="yellow",fg="black",command=lambda: home_return(loginwn),height=2,width=10)
    b1.pack(side="top")
    
    loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    

def Create():
    crwn=tk.Tk()
    
    crwn.geometry("1000x600")
    crwn.state('zoomed')    
    
    crwn.title("Create Account")
    crwn.configure(bg="#99b3ff")
    fr1=tk.Frame(crwn,bg="black")
    
    l_title=tk.Message(crwn,text="BANK",relief="raised",width=2000,padx=600,pady=0,fg="#99b3ff",bg="#00004d",justify="center",anchor="center")
    l_title.config(font=("simsun","50","bold"))
    l_title.pack(side="top")
    
    l1=tk.Label(crwn,text="Enter Name:",relief="raised").pack(side="top")
    e1=tk.Entry(crwn,bd=4)
    e1.pack(side="top",pady=7)
    crwn.after(1, lambda: crwn.focus_force())
    e1.focus_set()
    
    l2=tk.Label(crwn,text="Enter opening credit:",relief="raised")
    l2.pack(side="top",pady=3)
    e2=tk.Entry(crwn,bd=4)
    e2.pack(pady=5,side="top")
    
    l3=tk.Label(crwn,text="Enter desired PIN:",relief="raised")
    l3.pack(side="top")
    e3=tk.Entry(crwn,show="*",bd=4)
    e3.pack(side="top")
    
    b=tk.Button(crwn,text="Submit",pady=3,bd=5,width=10,command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.pack(side="top",pady=10)
    b1=tk.Button(crwn,text="HOME",bd=7,relief="raised",bg="#00004d",fg="#99b3ff",font=('bold'),command=crwn.destroy,height=3,width=7)
    b1.pack(side="top",pady=15)
    crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    #return
    

def Main_Menu():
    

    rootwn=tk.Tk()
    
    #rootwn.geometry("1366x768")
    rootwn.state('zoomed')

    photo = PhotoImage(file = "icon.gif")
    rootwn.iconphoto(False, photo)

    '''l_title=tk.Message(text="BANK\n SYSTEM",relief="raised",width=1000,padx=100,pady=-1,fg="#00004d",bg='#d1ccbb',justify="center",anchor="center")
    l_title.config(font=("simsun","40","bold"))
    l_title.pack(side="top")'''
    
    rootwn.title("BANK")
    rootwn.configure(background='#00004d')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    bg_image=tk.PhotoImage(file='bank icon.png')
    #bg_image2 = bg_image.resize((450, 350), bg_image.ANTIALIAS)
    
    x=tk.Label(image=bg_image,bd=0,bg='grey12')
    x.place(x=0, y=0, relwidth=1, relheight=1.12)
    x.pack(fill='both',expand='yes')
    
    imgc1=tk.PhotoImage(file="create.png")
    imglo=tk.PhotoImage(file="login.png")
    
    imgc=imgc1.subsample(3,3)
    imglog=imglo.subsample(3,3)

    b1=tk.Button(image=imgc,command=Create)
    b1.image=imgc
    b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
    b2.image=imglog
    img6=tk.PhotoImage(file="quit.gif")
    myimg6=img6.subsample(7,7)

    b6=tk.Button(image=myimg6,command=rootwn.destroy)
    b6.image=myimg6
    
    b1.place(x=945,y=300)
    b2.place(x=135,y=300)   
    b6.place(x=1240,y=640)

    rootwn.mainloop()

Main_Menu()
