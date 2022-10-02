#Linear Search on input array by user

def linearSearch(element):
    for i in range(len(arr)):
        if arr[i]==element:
            return i
    return "not found"
    
    
size=int(input("Enter the size "))
arr=[]
for i in range(size):
    arr.append(int(input("Enter elements ")))

#array has been created 
element=int(input("enter the element you want find"))
if linearSearch(element)=="not found":
    print("element not found")
else:
    print("element found at ",i)


        
