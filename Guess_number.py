""" A number genrated by python , user have to guess it . """

import random

x = random.randint(1 , 100)
count = 0
i = 0

for i in range(5) :

      y = int(input("guess a number (1 to 100) : "))
      count += 1

      if( x > y ) :
            print("you guess small number , try big number\n")

      elif(x < y ):
            print("you guess big number , try small number\n")

      else :
            print("Congratulation !  you guessed it .")
            break

if(x == y) :
      print("you did it in " , count , " times")
else :
      print("Better luck next time ! ")
      print("The number was : " , x , "." )

