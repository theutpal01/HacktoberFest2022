from tkinter import *
rt=Tk()
rt.geometry("400x200")
rt.title("Number Convertor")

sc1=StringVar()
sc2=StringVar()
sc3=StringVar()
sc4=StringVar()

l1=Label(rt, text="Decimal")
l2=Label(rt, text="Binary")
l3=Label(rt, text="Ocatal")
l4=Label(rt, text="Hexadecimal")

l1.place(x=30, y=30)
l2.place(x=30, y=60)
l3.place(x=30, y=90)
l4.place(x=30, y=120)

en1=Entry(rt, textvariable=sc1, justify="right")
en2=Entry(rt, textvariable=sc2, justify="right")
en3=Entry(rt, textvariable=sc3, justify="right")
en4=Entry(rt, textvariable=sc4, justify="right")

en1.place(x=150, y=30)
en2.place(x=150, y=60)
en3.place(x=150, y=90)
en4.place(x=150, y=120)

def ry():
    if sc1.get()!="" and sc2.get()=="" and sc4.get()=="" and sc4.get()=="":
        #decimal to binary
        a=str(bin(int(sc1.get())))
        k=list(a)
        k.pop(0)
        k.pop(0)
        s=""
        for i in k:
            s=s+i
        #decimal to octal
        b=str(oct(int(sc1.get())))
        m = list(b)
        m.pop(0)
        m.pop(0)
        t= ""
        for j in m:
            t = t + j
        #decimal to hexadecimal
        c=str(hex(int(sc1.get())))
        n = list(c)
        n.pop(0)
        n.pop(0)
        u = ""
        for h in n:
            u = u + h
        #setting values in entry widget 2,3,4
        sc2.set(s)
        sc3.set(t)
        sc4.set(u)

    elif sc1.get()=="" and sc2.get()!="" and sc3.get()=="" and sc4.get()=="":
        #converting binary to decimal
        a=int(sc2.get(), 2)
        d=str(a)
        #decimal to octal
        b=str(oct(a))
        l=list(b)
        l.pop(0)
        l.pop(0)
        s=""
        for i in l:
            s=s+i
        #decimal to hexadecimal
        c=str(hex(a))
        m=list(c)
        m.pop(0)
        m.pop(0)
        t=""
        for j in m:
            t=t+j
        #setting all the values
        sc1.set(d)
        sc3.set(s)
        sc4.set(t)

    elif sc1.get() == "" and sc2.get() == "" and sc3.get() != "" and sc4.get() == "":
        #octal to decimal
        a=int(sc3.get(), 8)
        d=str(a)
        #decimal to binary
        b=bin(a)
        k = list(b)
        k.pop(0)
        k.pop(0)
        s = ""
        for i in k:
            s = s + i

        #decimal to hexadecimal
        c=hex(a)
        n = list(c)
        n.pop(0)
        n.pop(0)
        u = ""
        for h in n:
            u = u + h
        #setting all the values
        sc1.set(d)
        sc2.set(s)
        sc4.set(u)

    elif sc1.get() == "" and sc2.get() == "" and sc3.get() == "" and sc4.get() != "":
        #hexadecimal to decimal
        a = int(sc4.get(), 16)
        d = str(a)
        #decimal to binary
        b = bin(a)
        k = list(b)
        k.pop(0)
        k.pop(0)
        s =""
        for i in k:
            s = s + i
        #decimal to octal
        c = str(oct(a))
        l = list(c)
        l.pop(0)
        l.pop(0)
        t = ""
        for j in l:
            t= t + j
        #setting all the values
        sc1.set(d)
        sc2.set(s)
        sc3.set(t)



b=Button(rt, text="Check", command=ry)
b.place(x=30, y=150)

def er():
    sc1.set("")
    sc2.set("")
    sc3.set("")
    sc4.set("")
b1=Button(rt, text="Clear", command=er)
b1.place(x=90, y=150)

rt.mainloop()