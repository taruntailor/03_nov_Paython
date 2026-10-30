import turtle
import math
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=800, height=800)
t.speed(0)
t.width(2)
t.hideturtle()
h=0
for i in range(720):
    c=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    r = 200*math.sin(math.radians(6*i))
    x = r*math.cos(math.radians(i))
    y=r*math.sin(math.radians(i))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(2)
    h += 0.005
t.penup()
t.goto(0,-20)
t.color("white")
t.write("Petter", align="center", font=("Arial", 24, "bold"))
turtle.done()