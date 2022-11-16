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


print("abc changes")
print("abc changes1")
print("abc changes2")
print("abc changes3")
print("abc changes4")
print("abc changes5")

print("abc changes6")
print("abc changes7")


print("abc changes8")
print("abc changes9")
print("abc changes10")

print("CD ")
print("fjk")
turtle.exitonclick()








