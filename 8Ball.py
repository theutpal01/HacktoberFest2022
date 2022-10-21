import random
#future: name can be changed to input to get a name from the users input
name = "YourName"
#future: question as above can be redone to ask user
question="Are we living in a simulation?"
#sets up empty string for answer is then populated with the elif statements
answer=""
#random number assigner between 1 and 9
random_number =random.randint(1,9)

#print(random_number)
print(name + " asks: " + question)
if name =="":
  print("Question" + question)
if question=="":
  print("Error no question asked")
if random_number==1:
  answer="Yes - definitely."
elif random_number==2:
  answer="It is decidedly so."
elif random_number==3:
  answer="Without a doubt."
elif random_number==4:
  answer="Reply hazy, try again."
elif random_number==5:
  answer="Ask again later."   
elif random_number==6:
  answer="Better not tell you now."
elif random_number==7:
  answer="My sources say no."   
elif random_number==8:
  answer="Outlook not so good."
elif random_number==9:
  answer="Very doubtful."

else:
  print("Error")

print("Magic 8 Ball's Answer: " + answer)