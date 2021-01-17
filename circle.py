#Hoc lession : spiral
#Author : Anson

import turtle as t
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle( size + 5, angle + 1, shift + 1)
     
t.bgcolor('pink')
t.pensize(4)
t.speed(5)

draw_circle( 10, 0, 1)
