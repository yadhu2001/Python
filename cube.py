import turtle

t=turtle.Turtle()
t.fillcolor("red")

t.begin_fill()
for i in range(4):
    
    t.forward(90)
    t.right(90)

t.goto(50,50)
t.end_fill()

t.begin_fill()
for i in range(4):
    t.forward(90)
    t.right(90)
t.end_fill()

t.begin_fill()
t.goto(140,50)
t.goto(90,0)
t.end_fill()
 
t.begin_fill()
t.right(90)
t.forward(90)
t.end_fill()

t.begin_fill()
t.right(225)
t.forward(70)
t.end_fill()

t.begin_fill()
t.penup()
t.left(135)
t.forward(90)
t.pendown()
t.left(45)
t.forward(70)

t.end_fill()

turtle.done()
