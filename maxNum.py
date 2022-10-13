
string = "Enter a number: "

list=[]

#Give unlimited inputs, to finish giving input press Enter

while(True):
  inp=input(string)
  if(inp==""):
    break
  else:
    list.append(float(inp))

# Check weather a number is present or not

if len(list)<1: # if Not Present
  print("No Number is Entered")
else: # If Present 
  list.sort() # List is sorted in ascending order
  maxNum=list[-1] # Last element of the list is stored in maxNum
  print("The greatest number among the given is", maxNum)
