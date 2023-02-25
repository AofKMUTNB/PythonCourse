import turtle
t = turtle.Pen()
t.shape('turtle')
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.clear()
for i in range(4): #ทำซ้ำ4ครั้ง
    t.forward(100)
    t.left(90)

t.penup()           #ยกปากกาขึ้น
t.goto(200,200)     #ไปยังจุดที่200,200
t.pendown()         #เอาปากกาลง
for i in range(4):
    t.forward(100)
    t.left(90)