import turtle

t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.speed(100)
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)
