import turtle as t 




def fractale(n, cote):
    if n == 0:
        t.forward(cote)
    else:
        fractale(n-1, cote/3)
        t.left(60)
        fractale(n-1, cote/3)
        t.right(120)
        fractale(n-1, cote/3)
        t.left(60)
        fractale(n-1, cote/3)

def flocon(n, cote):
    for i in range(3):
        fractale(n, cote)
        t.right(120)


t.penup()
t.goto(-100,  0)
t.pendown()
t.hideturtle()
t.speed(0)
t.color('red')
t.pensize(3)

flocon(4, 400)  

       
        
