# Sahar Olaya
# 3/20/2025
# P4LAB1
# Learning turtle graphics and loops

import turtle
# create drawing window
win = turtle.Screen()
# create turtle object
timmy = turtle.Turtle()

# set some attributes
timmy.pensize(7)
timmy.pencolor('blue')
timmy.shape('arrow')
win.bgcolor('pink')

#Test
#timmy.forward(70)


# For loop to draw traingle
for i in range(0,3):
    timmy.forward(200)
    timmy.left(120)

# while loop to drsw a square
side_num = 0 

while side_num <= 3:
    timmy.forward(200)
    timmy.right(90)
    side_num += 1



# Keeps the window open
win.mainloop()

