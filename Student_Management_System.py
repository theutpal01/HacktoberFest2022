#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Student:
 
  # Constructor
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
 
    # Function to create and append new student
    def accept(self, Name, Rollno, marks1, marks2):
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)
 
    # Function to display student details
    def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")
 
    # Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
 
    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
 
 
# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0, 0)
 
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Exit")
 
ch = int(input("Enter choice:"))
if(ch == 1):
    Name=input("Enter name of the student: ");
    Rollno=int(input("Enter roll number of the student: "))
    Marks1=int(input("Enter marks 1 of the student: "))
    Marks2=int(input("Enter marks 2 of the student"))
    obj.accept(Name, Rollno, Marks1, Marks2)

elif(ch == 2):
    print("\n")
    print("\nList of Students\n")
    for i in range(ls.__len__()):
        obj.display(ls[i])
    
elif(ch == 3):
    n=int(input("Enter the rollno of the student you want to search: "))
    s = obj.search(n)
    obj.display(ls[s])

elif(ch == 4):
    n=int(input("Enter the rollno of the student you want to delete: "))
    obj.delete(n)
    print(ls.__len__())
    print("List after deletion")
    for i in range(ls.__len__()):
        obj.display(ls[i])

else:
    print("Thank You !")


# In[ ]:





# In[ ]:




