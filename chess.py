import turtle

sc = turtle.Screen()
cb = turtle.Turtle()


# method to draw square
def draw():
    for i in range(4):
        cb.forward(30)
        cb.left(90)

    cb.forward(30)


# Driver Code
if __name__ == "__main__":

    # set screen
    sc.setup(400, 600)

    # set turtle object speed
    cb.speed(100)

    # loops for board
    for i in range(8):

        # not ready to draw
        cb.up()

        # set position for every row
        cb.setpos(-100, 30 * i)

        # ready to draw
        cb.down()

        # row
        for j in range(8):

            # conditions for alternative color
            if (i + j) % 2 == 0:
                col = 'black'

            else:
                col = 'white'

            # fill with given color
            cb.fillcolor(col)

            # start filling with colour
            cb.begin_fill()

            # call method
            draw()
            # stop filling
            cb.end_fill()

            # hide the turtle
    cb.hideturtle()
    turtle.done()
