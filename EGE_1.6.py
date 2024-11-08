import turtle

scale = 15

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.pendown()

# рисуем rectangle-1
for i in range(2):
    t.forward(17 * scale)
    t.left(90)
    t.forward(10 * scale)
    t.left(90)

# передвижение в начальную точку rectangle-2
t.penup()
t.backward(4 * scale)
t.right(90)
t.backward(3 * scale)
t.left(90)

# рисуем rectangle-2
t.pendown()
for i in range(2):
    t.forward(40 * scale)
    t.right(90)
    t.forward(10 * scale)
    t.right(90)

# ставим dot
t.pencolor('red')
for i in range(0, (17 + 1) * scale, scale):
    for j in range(0, (10 + 1) * scale, scale):
        t.penup()
        t.goto(i, j)
        t.pendown()
        t.dot()

turtle.mainloop()