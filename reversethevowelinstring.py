st=input("enter the string")
s=list(st)
v=['a','e','i','o','u','A','E','I','O','U']
t=[]
for i in s:
    if i in v:
        t.append(i)
t.reverse()
k=j=0
for i in s:
    if i in v:
        s[k]=t[j] 
        k=k+1
        j=j+1
    else:
        k=k+1    
print("".join(s))  
