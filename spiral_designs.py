import turtle as t 
t.bgcolor('black')
t.color('red')
t.speed(0)
for i in range(270):
    t.forward(i)
    t.right(130)
    t.setpos(0 , 0)
    t.right(120)
    t.forward(i)
    t.right(120)