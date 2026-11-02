import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()
t.width(2)
h=0
for i in range(220):
    c=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.forward(i*2)
    t.left(59)
    t.circle(i / 3)
    h+=0.008
turtle.done()