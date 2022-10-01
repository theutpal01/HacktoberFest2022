#!/usr/bin/env python
# coding: utf-8

# In[4]:


#20//3
a = 2.2
b = 3.3
a+b


# In[5]:


3+6


# In[4]:


print("ankit's 'laptop'")


# In[126]:


print('ankit \'s "laptop"') # / is used to ignore the special meaning like 's


# In[7]:


ank= [ 12, 13, 14, 15, 16]
ank


# In[8]:


ank.pop(3)


# In[9]:


ank


# In[19]:


ankit=2+3j
ankit


# In[20]:


type(ankit)


# In[21]:


bin(1234)


# In[26]:


a=5
b=7
a,b=b,a
print(a,b)


# In[29]:


import math
x=math.sqrt(64)
x


# In[30]:


y=math.pow(4,2)
y


# In[31]:


z=math.ceil(3.3) # ceil is used for rounding the no. at its higher digit
z


# In[32]:


xx=math.floor(3.3) # floor is used for roundimg the no. at its lower digit
xx


# In[34]:


help("math")


# In[1]:


x=int(input("Enter 1st number"))   # input has default string data type
y=int(input("Enter 2nd number"))
z=x+y
z


# In[6]:


character=input("enter character value")
character[2]


# In[7]:


char=input("enter character")[1]
char


# In[8]:


eq=eval(input("enter an expression"))   # eval is evaluate
eq


# In[21]:


a= int(input())
x = a % 2
if x==0:
    print("Even")
else:
    print("odd")


# In[24]:


a = int(input())
x=a%2
if x==0:
    print("even")
    print([a+1,a+3,a+5])
else:
    print("odd")
    print([a,a+2,a+4])


# In[27]:


t= int(input())
if t==1:
    print("one")
elif t==2:
    print("two")
else:
    print("no. other then one and two")


# In[33]:


# While Loop
i=1                   # initialising
while i<=5:           # condition
    print("ankit",i) 
    i=i+1             # increament


# In[61]:


i=1
while i<=5:
    print("ankit")
    j=1
    while j<=4:
        print("rock")
        j=j+1
    i=i+1 
    print()


# In[63]:


i=1
while i<=5:
    print("ankit ",end="") # run on same line so we use end=""
    j=1
    while j<=4:
        print("rock ",end="") # run on same line so we use end=""
        j=j+1
    i=i+1   
    print()


# In[41]:


# For Loop
for i in range(11,21,1):
    print(i)


# In[56]:


c=int(input("How many candy you want"))
av=5
i=1
while i<=c:
    if i>av:
        print("Out of stock")
        break # Break statement is used to stop the condition
    print("candy")
    i+=1   


# In[74]:


# Continue is use to skip the further execution
for i in range(5):
    if i==3:
        continue
    print("Hello",i)


# In[64]:


for i in range(1,101):
    if (i%2==0):
        pass # Pass is used to skip the no.
        
    else:
        print(i)
    


# In[125]:


i=1

while i<=4:
    j=1
    while j<=4:
        print("* ",end="")
        j=j+1
    i=i+1
    print()
        


# In[103]:


for i in range(4):
    for j in range(4):
        print("* ",end="")
    print()    


# In[2]:


for i in range(4):
    for j in range(i+1):
        print("* ",end="")
    print()  


# In[109]:


for i in range(4):
    for j in range(4-i):
        print("* ",end="")
        
    print()


# In[112]:


# Prime no.
i=10
for n in range(2,i):
    if i%n==0:
        print(" Not prime no.")
        break
else:
    print("Prime no.")


# In[124]:


i=1

while i<=4:
    j=1
    while j<=i:
        print("* ",end="")
        j=j+1
    i=i+1
    print()


# In[123]:



i=1
while i<=4:
    j=4
    while j>=i:
        print("* ",end="")
        j=j-1
    i=i+1
    print()


# In[15]:


import array as arr
arr= array('i',[])    # i represent int data type
n=int(input("Enter the length of array"))
for i in range(n):
    x=int(input("Enter the no."))
    arr.append(x)     # append is used to add values
print(arr)    
    

        


# In[27]:


# Numpy
from numpy import*
arr=array([1,2,3]) # in numpy we don't mention the data type to make an array
print(arr)


# In[30]:


arr=arange(1,20,2)
print(arr)


# In[40]:


m=matrix('1,2,3; 4,5,6; 7,8,9')
print(m)


# In[ ]:


# creating new function
def ankit():
    print("Hello")       # Function content
    print("Everyone")
ankit()    


# In[23]:


from numpy import*
arr2 =array([12,23,45,67])
print(arr)
arr1 = arr2.copy()
print(arr1)


# In[32]:


# position argument
def person(name,age):
    print(name)
    print(age)
person("ankit",12)    


# In[29]:


# Keword argument
def person(name,age):
    print(name)
    print(age)
person(name="ankit",age=12) 


# In[30]:


# Default argument
def person(name,age=18):  # default age is 18
    print(name)
    print(age)
person("ankit") 


# In[38]:


# Default argument
def person(name,age=18):  # default age is 18
    print(name)
    print(age)
person("ankit")


# In[39]:


# vaiable length argument
def person(name,*data):  # * passes multiple values
    print(name)
    print(data)
person("ankit",18,"noida",345678) 


# In[40]:


# Keyword Variable length argument
def person(name,**data):  # ** passes multiple values with keyword
    print(name)
    print(data)
person("ankit",age=18,city="noida",pin=285678)


# In[48]:


a=10               # Global value (outside the function)
def anki():
    a=15              # Local value (inside the function)
    print("local",a)
anki()
print("global",a)
    
    


# In[32]:


a=10
def anki():
    a=15
    globals()['a']= 20          # it is used to change the value of global within a function
    print("local",a)
anki()
print("global",a)
    
    


# 

# In[62]:



def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd 
lst=[12,13,14,15,1,5,5,6]
even,odd= count(lst)
print("Even:{} and Odd:{}".format(even,odd))


# In[68]:


# Fibonacci Series
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(7)        
        


# In[77]:


# Factorial no.
def fac(i):
    f=1
    for n in range(1,i+1):
        f=f*n
    return f
x=5
result=fac(x)
print(result)


# In[84]:


def fac(i):
    if i==0:
        return 1      # finding factorial by recursiom
    return i*fac(i-1)
result=fac(4)
result


# In[86]:


# Anonymous function (lambda)
f=lambda a,b:a+b              # define the function does not having a function name
result=f(5,11)
result


# In[90]:


def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd 
lst=[]
n = int(input("enter the size of list "))
for j in range(n):
    x=int(input("enter the next string "))
    lst.append(x)
print(lst)    
even,odd= count(lst)
print("Even:{} and Odd:{}".format(even,odd))


# In[25]:


# Creating File
f = open("ankit.txt",'a') # in W = write overwrite occur so we use a = append
def fac(i):
    f=1
    for n in range(1,i+1):
        f=f*n
    return f
x=5
result=fac(x)
print(result,file=f)  # print the output of factorial in file
f.close()


# In[31]:


# print the output in file
f = open("ankit.txt",'a') # in W = write overwrite occur so we use a = append
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd 
lst=[]
n = int(input("enter the size of list "))
for j in range(n):
    x=int(input("enter the next string "))
    lst.append(x)
print(lst,file=f)    
even,odd= count(lst)
print("Even:{} and Odd:{}".format(even,odd),file=f)
f.close()


# In[27]:


list=[]
n=int(input("enter the no. od data in a list"))
for i in range(n):
    x=int(input("Enter the no. in a string"))
    list.append(x)
print(list)    


#     

# 
# 

# In[ ]:


f=open("ankit.txt",'a')


# In[5]:


nums = [2,3,6,8,4,10]
even = list(filter(lambda n : n%2==0 ,nums))   # filter function
even
double=list(map(lambda a : a*2,even))  # map function
double


# In[9]:


# Decorator
def div(a,b):
    print(a/b)                   
def smart_div(func):          # Decorator means assigning multiple functions inside a function
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1= smart_div(div)    # link two functions
div1(2,4)


# In[64]:


# Module
from calcu import *  # import from calcu.py file
sum=add(10,17)
divi=div(50,2)
print(sum,divi)


# In[2]:


class computer:        # defining a class
    def config(self):  # self is default used in class
        print("i5,16gb,1TB")
com1=computer()
com1.config()


# In[8]:


class compu:
    def __init__(self,cpu,ram):    # in __init__ method it was automatically call during run time
        self.cpu=cpu
        self.ram=ram               
    def config(self):               # in config we were call the config for execution
        print("config is",self.cpu,self.ram)
com1=compu('i5',16)
com2=compu('i7',8)
com1.config()
com2.config()


# In[26]:


class car:
    Colour="RED"           # class or static variable
    def __init__(self):
        self.mil=10        # instance variable
        self.com="Audi"    # instance variable
c1=car()
c1.mil=8
car.Colour="Blue"
print(c1.com,c1.mil,c1.Colour)


# In[38]:


class student:
    school="Modern"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):         # instance method
        return(self.m1+self.m2+self.m3)/3
s1=student(12,23,45)
s1.avg()
    


# In[ ]:


# two types of instance method : 1. Accessor method     2. Mutator method

    # def get_m1(self):       \\ Accessor method (get the value)
        return self.m1
    # def set_m1(self,value)   \\ Mutator method (set the value)
        self.m1=value
    


# In[54]:


class student:
    school="Modern"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @classmethod      # Decorator
    def getinfo(cls):     # Class Method
        return cls.school
print(student.getinfo())    


# 

# In[55]:


class student:
    school="Modern"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @staticmethod    # Decorator
    def info():              # Static Method
        print("This is Student class")
student.info()    


# In[60]:


class student:                         # Outer class
    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno
        self.lap= self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:                       # Inner class
        def __init__(self):
            self.brand= "HP"
            self.ram= 16
            self.cpu="i5"
        def show(self):
            print(self.brand,self.ram,self.cpu)
s1=student("Ankit",21)
s1.show()
        
        
    


# In[63]:


a,b='5','6'
print(str.__add__(a,b))            # print(a+b)


# In[69]:


# Iterator (it is used for fetching onebvalue at a time)
nums=[12,13,14,15]
it=iter(nums)         # iter = iteration
print(it.__next__())
print(next(it))
print(next(it))
print(it.__next__())


# In[70]:


# Generator Function
def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq     # yield is the special keyword of Generator function
        n+=1
values=topten()
for i in values:
    print(i)


# In[19]:


# Exception
a=0
b=1
try:
    print(a/b)
except Exception as d:
    print("No no. is divided by zero",d)
finally:
    print("output is came")
    


# In[3]:


# Main Threads
class hello:
    def run(self):
        for i in range(5):
            print("Hello")
class Ankit:
    def run(self):
        for i in range(5):
            print("Ankit")
a=hello()        
b=Ankit()
a.run()
b.run()


# In[4]:


# Threads
from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class Ankit(Thread):
    def run(self):           # run function is mention compelsary for threading
        for i in range(5):
            print("Ankit")
            sleep(1)
a=hello()        
b=Ankit()
a.start()          # in threading we use "".start" function in which
sleep(0.5)
b.start()


# In[38]:



class hello():
    def run(self):
        for i in range(4):
            j=1
            for j in range(i+1):
                print(" *",end="")  
            print()
        
class Ankit():
    def run(self):
        for i in range(4):
            j=4
            for j in range(4-i):
                print(" *",end="")
            print()    
                      
a=hello()        
b=Ankit()
a.run()         
b.run()


# In[44]:


from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(4):
            j=1
            for j in range(i+1):
                print(" *",end="") 
                
            print()
            sleep(1)
            
        
class Ankit(Thread):
    def run(self):
        for i in range(4):
            j=4
            for j in range(4-i):
                print(" *",end="")
                
            print()
            sleep(1)
            
                      
a=hello()        
b=Ankit()
a.start()          # in threading we use "".start" function in which
sleep(0.5)
b.start()


# In[47]:


from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(4):
            j=1
            for j in range(i+1):
                print(" *",end="") 
                
            print()
            sleep(1)
            
        
class Ankit(Thread):
    def run(self):
        for i in range(4):
            j=4
            for j in range(4-i):
                print(" *",end="")
                
            print()
            sleep(1)
            
                      
a=hello()        
b=Ankit()
a.start()          # in threading we use "".start" function in which
sleep(0.5)
b.start()
a.join()          # join is used for asking the main thread to wait until a & b executed
b.join()
print("Byee")


# In[54]:


f=open("calcu.py",'r')
f.readline()


# In[75]:


f=open("ankit.txt",'r')
f.readline()
f.readline()


# In[60]:


f=open("ankit.txt",'r')
f1=open("calcu.py",'a')          # extracting data from file and write in another file
for i in f:
    f1.write(i)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




