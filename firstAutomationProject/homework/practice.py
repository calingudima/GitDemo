import random
import turtle

turtle.color("yellow")
turtle.bgcolor("black")
#turtle.speed(0)
#turtle.hideturtle()

def starmaker(step, angle):
    for iter in range(5):
        turtle.forward(step)
        turtle.right(angle)

for i in range(10):
    turtle.penup()
    turtle.setpos(random.randint(-350, 350), random.randint(100, 300))
    turtle.pendown()
    starmaker(10.144)





turtle.exitonclick()








