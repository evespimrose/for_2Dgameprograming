import turtle


for a in [0,1,2,3,4,5]:
    turtle.penup()
    turtle.goto(a * 60,0)
    turtle.pendown()
    turtle.goto(a * 60,300)

for a in [0,1,2,3,4,5]:
    turtle.penup()
    turtle.goto(0,a * 60)
    turtle.pendown()
    turtle.goto(300,a * 60)

turtle.exitonclick()
