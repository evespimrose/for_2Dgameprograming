import turtle

def set0():
    turtle.setheading(0)
    turtle.penup()

def set1():
    turtle.setheading(0)
    turtle.pendown()

def nextword():
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(225)
    set1()

def undercircle():
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(125)
    set1()
    turtle.circle(50)
    set0()
    nextword()




turtle.penup()
turtle.goto(-400,200)
turtle.pendown()

turtle.forward(100)
turtle.backward(50)
turtle.right(120)
turtle.forward(75)
turtle.backward(75)
turtle.left(60)
turtle.forward(75)
turtle.backward(75)
set0()

turtle.forward(100)
set1()

turtle.right(90)
turtle.forward(100)
turtle.backward(50)
turtle.left(90)
turtle.forward(50)
turtle.penup()
turtle.backward(50)
turtle.right(90)
turtle.forward(50)
set0()

undercircle()



turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.backward(75)
turtle.right(90)
turtle.forward(25)
set1()
turtle.forward(100)
turtle.penup()
turtle.backward(50)
turtle.right(90)
turtle.forward(75)
set1()
turtle.circle(30)
set0()

turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
set1()

turtle.forward(50)
turtle.penup()
turtle.backward(50)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.left(90)
turtle.forward(75)
turtle.right(180)
turtle.pendown()
turtle.forward(125)
set0()

undercircle()




for n in [1,2]:
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
turtle.forward(100)
set0()

turtle.forward(50)
turtle.left(90)
turtle.forward(100)
set1()

turtle.right(90)
turtle.forward(100)
turtle.backward(50)
turtle.penup()
turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(100)
set0()

turtle.backward(150)
turtle.right(90)
turtle.forward(25)
set1()

turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.setheading(0)

turtle.exitonclick()
