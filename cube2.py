import turtle
my_pen=turtle.Turtle()

for i in range(4): 
    my_pen.forward(100) 
    my_pen.left(90) 
  
# bottom left side 
my_pen.goto(50,50) 
  
# forming back square face 
for i in range(4): 
    my_pen.forward(100) 
    my_pen.left(90) 
  
# bottom right side 
my_pen.goto(150,50) 
my_pen.goto(100,0) 
  
# top right side 
my_pen.goto(100,100) 
my_pen.goto(150,150) 
  
# top left side 
my_pen.goto(50,150) 
my_pen.goto(0,100)

turtle.done()