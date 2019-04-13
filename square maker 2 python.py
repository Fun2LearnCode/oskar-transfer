#Draw square loop.py
import turtle
t = turtle.Pen()
for x in range(400):
    t.forward(1.5555555555555)
    t.left(1)
    t.speed(0)
    
for x in range(365):
    t.forward(3.5555555555555)
    t.left(1)
    t.speed(0)

for x in range(400):
    t.forward(0.5)
    t.left(1)
    t.speed(0)

for x in range(400):
    t.forward(0.3)
    t.left(1)
    t.speed(-500)
