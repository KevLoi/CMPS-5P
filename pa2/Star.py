# Kevin Loi
# kloi@ucsc.edu
# pa2
# Draws an n-pointed star

import turtle


# function -----------------------------------------------------------
def draw_Star(t, s):
    # Make turtle t draw a star with s points

    turn = 180 - 180/s

    t.begin_fill()
    for i in range(s):
        t.forward(300)
        t.right(turn)
        t.dot(10, "red")
    t.end_fill()

    # end of draw_Star function
        
# main program -------------------------------------------------------
n = int(input("Enter an odd integer greater than or equal to 3: "))
wn = turtle.Screen()
wn.title(str(n)+"-pointed star")

bob = turtle.Turtle()
bob.color("blue", "green")
bob.shape("blank")
bob.pensize(2)
bob.speed(5)
bob.setpos(-150, 0)

draw_Star(bob, n)

wn.mainloop()





