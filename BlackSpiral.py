# import turtle
import turtle

# initialising variables
dist = 1
flag = 500

# initialising turtle
spiral = turtle.Turtle()

# changing speed of turtle
spiral.speed(10)

# making patten
while flag:
	
	# makes the turtle to move forward
	spiral.forward(dist)
	
	# makes the turtle to move left
	spiral.left(120)
	spiral.left(1)
	dist += 1
	flag -= 1

turtle.done()
